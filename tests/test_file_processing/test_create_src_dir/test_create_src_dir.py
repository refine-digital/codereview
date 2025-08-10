# File: tests/test_file_processing/test_create_src_dir/test_create_src_dir.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from analyze import walk_and_parse

class TestCreateSrcDir(unittest.TestCase):
    """
    Tests that the walk_and_parse function correctly finds all relevant files.
    """

    def test_file_discovery(self):
        """
        Verifies that walk_and_parse discovers all expected files in the src directory.
        """
        print("\n--- Testing File Discovery ---")
        
        # We don't need to parse the files for this test, just discover them.
        # We can mock the parse_file function to speed up the test.
        from unittest.mock import patch
        with patch('analyze.parse_and_enrich_file') as mock_parse_and_enrich_file:
            mock_parse_and_enrich_file.return_value = {"file": "mocked"}
            
            results, files_processed = walk_and_parse()
            
            # We expect to find a certain number of files.
            # This number will need to be updated if the src directory changes.
            expected_file_count = 1179 # Based on the previous run
            self.assertEqual(files_processed, expected_file_count, f"Expected to find {expected_file_count} files, but found {files_processed}.")
            
            print(f"✅ PASSED: Successfully discovered {files_processed} files.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

