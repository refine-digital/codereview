# File: tests/test_parsing/test_parsing_sh/test_parsing_sh.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.sh_handler import parse as parse_sh

class TestParsingSH(unittest.TestCase):
    """
    Tests the Shell script parser.
    """

    def test_sh_parsing(self):
        """
        Verifies that the SH parser correctly extracts functions and variables.
        """
        print("\n--- Testing Shell Script Parsing ---")
        
        content = """
        #!/bin/bash
        
        MY_VAR="hello"

        my_function() {
            echo $MY_VAR
        }
        """
        
        result = parse_sh(content)
        
        self.assertIn("MY_VAR", result["variables"])
        self.assertIn("my_function", result["functions"])
        print("✅ PASSED: Shell script parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

