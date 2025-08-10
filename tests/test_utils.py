# File: tests/test_utils.py
# Version: 1.1.0
import os
import yaml
from pathlib import Path
from dotenv import dotenv_values, load_dotenv

def load_test_config(test_dir: Path):
    """
    Loads test configuration, handling symlinks and overrides, and prints a report.
    """
    print(f"\n--- Loading Configuration for Test: {test_dir.name} ---")

    # 1. Define paths
    base_config_path = test_dir / "config.yaml"
    base_env_path = test_dir / ".env"
    override_config_path = test_dir / "config.override.yaml"
    override_env_path = test_dir / ".env.override"

    # 2. Load base config and .env file values for inspection
    with open(base_config_path, 'r') as f:
        config = yaml.safe_load(f)
    env_base_vars = dotenv_values(base_env_path)
    
    # 3. Load and apply overrides
    if override_config_path.exists():
        print(f"  - Found config.override.yaml, applying overrides...")
        with open(override_config_path, 'r') as f:
            config.update(yaml.safe_load(f))

    env_override_vars = {}
    if override_env_path.exists():
        print(f"  - Found .env.override, applying overrides...")
        env_override_vars = dotenv_values(override_env_path)

    # 4. Load .env files into the actual environment for the test
    # Base .env does NOT override existing system variables
    load_dotenv(dotenv_path=base_env_path, override=False)
    # Override .env DOES override existing system variables
    if override_env_path.exists():
        load_dotenv(dotenv_path=override_env_path, override=True)

    # 5. Report on the final state of critical variables
    print("Final environment variables being used for this test:")
    
    # Gather all relevant keys from all potential sources
    keys_to_check = set(env_base_vars.keys()) | set(env_override_vars.keys())
    for key in os.environ:
        if "API_KEY" in key or "OLLAMA" in key:
            keys_to_check.add(key)

    for key in sorted(list(keys_to_check)):
        # Skip irrelevant keys
        if "API_KEY" not in key and "OLLAMA" not in key:
            continue

        # Determine the final value and its source based on precedence
        final_value = os.getenv(key)
        source = "Not Found"

        if env_override_vars.get(key) is not None:
            source = ".env.override"
        elif os.environ.get(key) is not None and env_base_vars.get(key) != os.environ.get(key):
             # If the os.environ value is different from the base .env value, it must be a system variable
            source = "System Environment"
        elif env_base_vars.get(key) is not None:
            source = ".env file"
        
        masked_value = f"{final_value[:4]}{'*' * (len(final_value) - 4)}" if final_value else "Not Set"
        print(f"  - {key}: {masked_value} (Source: {source})")

    # Return the final config dictionary for the test to use
    return config, {**env_base_vars, **env_override_vars}
