# File: analyze.py
# Version: 3.0.0
import os
import json
from pathlib import Path
from dotenv import load_dotenv

from modules.config_loader import load_config
from modules.providers.manager import ProviderManager
from modules.agent_logic import get_agent_for_file
from modules.file_utils import get_file_hash, load_cache, save_cache
from parsers.handlers import handlers

load_dotenv()

# --- Load Configuration ---
config = load_config()
SRC_DIR = Path(config.get("src_dir", "./src"))
OUTPUT_DIR = Path(config.get("output_dir", "./output"))
CACHE_FILE = OUTPUT_DIR / "analysis_cache.json"
FILE_TYPES = config.get("file_types", [])
AGENTS_CONFIG = config.get("agents", {})
PROJECT_LEAD_TASKS = config.get("project_lead_tasks", [])
CURRENT_ENV = config.get("current_environment", "local_mac")
ENV_CAPABILITIES = config.get("system_capabilities", {}).get(CURRENT_ENV, {})
AGENT_ASSIGNMENTS = ENV_CAPABILITIES.get("agent_model_assignments", {})
EXTERNAL_APIS = config.get("external_apis", {})

# --- Initialize Provider Manager ---
provider_manager = ProviderManager(AGENT_ASSIGNMENTS, EXTERNAL_APIS)

# --- Core Functions ---

def parse_and_enrich_file(filepath):
    """Parses a file and enriches the data using the appropriate agent."""
    ext = filepath.suffix.lower().lstrip('.')
    if ext not in handlers:
        return None

    agent_name = get_agent_for_file(ext)
    
    try:
        provider = provider_manager.get_provider(agent_name)
    except ValueError as e:
        print(f"⚠️ Warning: {e}. Skipping enrichment for {filepath.name}.")
        return None

    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        parsed_data = handlers[ext](content)
        if not parsed_data:
            return None
        
        parsed_data['file'] = str(filepath)
        
        print(f"  Enriching {filepath.name} using agent '{agent_name}'...")
        
        # Step 1: Initial Analysis
        initial_prompt = provider.construct_prompt(AGENTS_CONFIG[agent_name]['system_prompt'], "Provide a detailed analysis of the following code:", content)
        initial_analysis = provider.execute_prompt(initial_prompt)

        # Step 2: Detailed RAG Tasks
        rag_analysis = {}
        for task in config.get("rag_tasks", []):
            print(f"    - Performing task: {task['id']}")
            task_prompt = provider.construct_prompt(AGENTS_CONFIG[agent_name]['system_prompt'], task['prompt'], initial_analysis)
            rag_analysis[task['id']] = provider.execute_prompt(task_prompt)

        parsed_data['ai_analysis'] = {
            "initial_analysis": initial_analysis,
            "rag_tasks": rag_analysis
        }
        return parsed_data

    except Exception as e:
        return {"file": str(filepath), "error": str(e)}

def walk_and_parse():
    """Walks the source directory, parses and enriches files, and uses caching."""
    cache = load_cache(CACHE_FILE)
    results = {}
    files_processed = 0
    
    all_files = [p for ext in FILE_TYPES for p in SRC_DIR.rglob(f"*.{ext}")]

    print(f"Found {len(all_files)} files to analyze in '{SRC_DIR}'.")
    for file in all_files:
        file_path_str = str(file)
        file_hash = get_file_hash(file)
        
        if cache.get(file_path_str) == file_hash:
            continue

        print(f"Processing new/modified file: {file.name}")
        enriched_data = parse_and_enrich_file(file)
        if enriched_data:
            relative_dir = file.relative_to(SRC_DIR).parent
            output_key = str(relative_dir)
            
            if output_key not in results:
                results[output_key] = []
            
            results[output_key].append(enriched_data)
            cache[file_path_str] = file_hash
            files_processed += 1

    save_cache(cache, CACHE_FILE)
    return results, files_processed

def main():
    """Main function to run the analysis, enrichment, and final review."""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    parsed_data_by_dir, files_processed = walk_and_parse()

    if files_processed > 0:
        for dir_path, data in parsed_data_by_dir.items():
            output_subdir = OUTPUT_DIR / dir_path
            output_subdir.mkdir(exist_ok=True, parents=True)
            
            for file_data in data:
                base_name = Path(file_data['file']).stem
                output_file = output_subdir / f"{base_name}.json"
                
                with open(output_file, "w") as f:
                    json.dump(file_data, f, indent=2)
        
        print(f"\nProcessed and enriched {files_processed} new or modified files.")
    else:
        print("No new or modified files to process. Analysis is up to date.")

    # --- Execute Final Project Lead Tasks ---
    if PROJECT_LEAD_TASKS:
        print("\n--- Running Project Lead Final Tasks ---")
        
        system_capabilities_context = json.dumps(ENV_CAPABILITIES, indent=2)
        agent_assignments_context = json.dumps(AGENT_ASSIGNMENTS, indent=2)
        
        for task in PROJECT_LEAD_TASKS:
            print(f"  - Performing task: {task['id']}")
            
            task_prompt = task['prompt'].format(
                system_capabilities=system_capabilities_context,
                agent_assignments=agent_assignments_context
            )
            
            run_summary_context = f"Analysis run completed for environment '{CURRENT_ENV}'. {files_processed} files were processed."
            
            project_lead_provider = provider_manager.get_provider('project_lead')
            final_prompt = project_lead_provider.construct_prompt(AGENTS_CONFIG['project_lead']['system_prompt'], task_prompt, run_summary_context)
            recommendation = project_lead_provider.execute_prompt(final_prompt)
            
            output_file = OUTPUT_DIR / "model_strategy_review.md"
            with open(output_file, "w") as f:
                f.write(recommendation)
            print(f"  - Project Lead's recommendation saved to {output_file}")

if __name__ == "__main__":
    main()
