# File: tests/test_parsing/test_parsing_yaml/test_parsing_yaml.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.yaml_handler import parse as parse_yaml

class TestParsingYAML(unittest.TestCase):
    """
    Tests the YAML parser.
    """

    def test_yaml_parsing(self):
        """
        Verifies that the YAML parser correctly extracts keys.
        """
        print("\n--- Testing YAML Parsing ---")
        
        content = """
        key1: value1
        key2:
          nested_key1: nested_value1
        """
        
        result = parse_yaml(content)
        
        self.assertIn("key1", result["keys"])
        self.assertIn("key2", result["keys"])
        self.assertIn("nested_key1", result["keys"])
        print("✅ PASSED: YAML parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

