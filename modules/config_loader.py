# File: modules/config_loader.py
# Version: 1.0.0
import yaml
from pathlib import Path

def load_config():
    """Loads the main config.yaml file."""
    config_path = Path("config.yaml")
    if not config_path.exists():
        raise FileNotFoundError("config.yaml not found in the project root.")
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
