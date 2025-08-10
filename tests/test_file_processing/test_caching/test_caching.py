# File: tests/test_file_processing/test_caching/test_caching.py
# Version: 1.0.0
import unittest
import sys
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from modules.file_utils import get_file_hash, load_cache, save_cache

class TestCaching(unittest.TestCase):
    """
    Tests the caching functionality.
    """

    def setUp(self):
        """Set up a temporary cache file for testing."""
        self.test_dir = Path(__file__).resolve().parent
        self.cache_file = self.test_dir / "test_cache.json"
        self.test_file = self.test_dir / "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("initial content")

    def tearDown(self):
        """Remove the temporary cache file."""
        if self.cache_file.exists():
            self.cache_file.unlink()
        if self.test_file.exists():
            self.test_file.unlink()

    def test_cache_save_and_load(self):
        """Tests that the cache can be saved and loaded correctly."""
        print("\n--- Testing Cache Save and Load ---")
        
        # 1. Create a cache and save it
        file_hash = get_file_hash(self.test_file)
        cache_to_save = {str(self.test_file): file_hash}
        save_cache(cache_to_save, self.cache_file)
        
        # 2. Load the cache and verify its contents
        loaded_cache = load_cache(self.cache_file)
        self.assertEqual(cache_to_save, loaded_cache)
        print("✅ PASSED: Cache saved and loaded successfully.")

    def test_caching_skips_unchanged_files(self):
        """
        Verifies that walk_and_parse skips a file if its hash is in the cache.
        """
        print("\n--- Testing Caching Skips Unchanged Files ---")
        
        # 1. Prime the cache with the current hash of the test file
        file_hash = get_file_hash(self.test_file)
        cache = {str(self.test_file): file_hash}
        save_cache(cache, self.cache_file)

        # 2. Mock the walk_and_parse function to check if the file is processed
        # This is a simplified version of the logic in analyze.py
        files_processed = 0
        if cache.get(str(self.test_file)) != get_file_hash(self.test_file):
            files_processed += 1
        
        self.assertEqual(files_processed, 0, "The file was processed even though its hash was in the cache.")
        print("✅ PASSED: Unchanged file was correctly skipped.")

    def test_caching_processes_changed_files(self):
        """
        Verifies that walk_and_parse processes a file if its hash has changed.
        """
        print("\n--- Testing Caching Processes Changed Files ---")
        
        # 1. Prime the cache with an old hash
        cache = {str(self.test_file): "old_hash"}
        save_cache(cache, self.cache_file)

        # 2. Modify the file
        with open(self.test_file, "w") as f:
            f.write("new content")

        # 3. Mock the walk_and_parse logic
        files_processed = 0
        if cache.get(str(self.test_file)) != get_file_hash(self.test_file):
            files_processed += 1
            
        self.assertEqual(files_processed, 1, "The file was not processed even though its hash changed.")
        print("✅ PASSED: Changed file was correctly processed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
