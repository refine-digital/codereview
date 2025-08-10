# File: tests/test_parsing/test_parsing_css/test_parsing_css.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.css_handler import parse as parse_css

class TestParsingCSS(unittest.TestCase):
    """
    Tests the CSS parser.
    """

    def test_css_parsing(self):
        """
        Verifies that the CSS parser correctly extracts selectors and rules.
        """
        print("\n--- Testing CSS Parsing ---")
        
        content = """
        /* A CSS comment */
        body {
            font-family: sans-serif;
            color: #333;
        }

        #main-container {
            width: 100%;
        }
        """
        
        result = parse_css(content)
        
        self.assertIn("body", result["selectors"])
        self.assertIn("#main-container", result["selectors"])
        self.assertEqual(len(result["rules"]), 2)
        print("✅ PASSED: CSS parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

