# File: prompt.py
# Version: 4.0.0
import os
import json
import yaml
import argparse
import ollama
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

MODEL = config.get("model", "gpt-oss:20b")
OUTPUT_DIR = Path(config.get("output_dir", "./output"))
CACHE_FILE = OUTPUT_DIR / "analysis_cache.json"

def summarize_context(file_path):
    """Summarizes the content of a single JSON file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    prompt = f"You are a senior software engineer analyzing a codebase. Summarize the following file analysis, focusing on its primary purpose, classes, functions, and any public methods or APIs. Be concise but informative.:\n\n{content}"
    
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes code analysis."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"Warning: Could not summarize {file_path}. Error: {e}")
        return ""

def main(prompt):
    # Stage 1: Summarize each JSON file
    summaries = []
    for json_file in sorted(OUTPUT_DIR.rglob("*.json")):
        if json_file.resolve() != CACHE_FILE.resolve():
            print(f"Summarizing {json_file}...")
            summary = summarize_context(json_file)
            summaries.append(summary)

    # Stage 2: Combine summaries and ask the original question
    combined_summary = "\n\n".join(summaries)
    
    full_prompt = f"Context:\n{combined_summary}\n\nPrompt: {prompt}"

    print("Generating final answer...")
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about a codebase based on provided context."},
            {"role": "user", "content": full_prompt}
        ]
    )

    # Save the response
    output_file = OUTPUT_DIR / "answer.md"
    with open(output_file, "w") as f:
        f.write(response['message']['content'])

    print(f"Answer saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="The prompt for the AI model")
    args = parser.parse_args()
    main(args.prompt)
