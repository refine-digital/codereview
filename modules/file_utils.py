# File: modules/file_utils.py
# Version: 1.0.0
import hashlib
import json
from pathlib import Path

def get_file_hash(filepath):
    """Computes the SHA256 hash of a file's content."""
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def load_cache(cache_file):
    """Loads the analysis cache from a file."""
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_cache(cache, cache_file):
    """Saves the analysis cache to a file."""
    with open(cache_file, 'w') as f:
        json.dump(cache, f, indent=2)
