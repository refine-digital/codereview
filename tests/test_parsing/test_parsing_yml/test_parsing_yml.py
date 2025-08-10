# File: tests/test_parsing/test_parsing_yml/test_parsing_yml.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.yml_handler import parse as parse_yml

class TestParsingYML(unittest.TestCase):
    """
    Tests the YML parser.
    """

    def test_yml_parsing(self):
        """
        Verifies that the YML parser correctly extracts keys.
        """
        print("\n--- Testing YML Parsing ---")
        
        content = """
        key1: value1
        key2:
          nested_key1: nested_value1
        """
        
        result = parse_yml(content)
        
        self.assertIn("key1", result["keys"])
        self.assertIn("key2", result["keys"])
        self.assertIn("nested_key1", result["keys"])
        print("✅ PASSED: YML parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

