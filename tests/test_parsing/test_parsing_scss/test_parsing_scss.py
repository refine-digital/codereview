# File: tests/test_parsing/test_scss/test_parsing_scss.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.scss_handler import parse as parse_scss

class TestParsingSCSS(unittest.TestCase):
    """
    Tests the SCSS parser.
    """

    def test_scss_parsing(self):
        """
        Verifies that the SCSS parser correctly extracts variables and mixins.
        """
        print("\n--- Testing SCSS Parsing ---")
        
        content = """
        $primary-color: #333;

        @mixin border-radius($radius) {
            -webkit-border-radius: $radius;
            border-radius: $radius;
        }

        .box {
            @include border-radius(10px);
            color: $primary-color;
        }
        """
        
        result = parse_scss(content)
        
        self.assertIn("$primary-color", result["variables"])
        self.assertIn("border-radius", result["mixins"])
        print("✅ PASSED: SCSS parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

