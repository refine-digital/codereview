# File: tests/test_parsing/test_parsing_pot/test_parsing_pot.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.pot_handler import parse as parse_pot

class TestParsingPOT(unittest.TestCase):
    """
    Tests the POT file parser.
    """

    def test_pot_parsing(self):
        """
        Verifies that the POT parser correctly extracts msgid entries.
        """
        print("\n--- Testing POT Parsing ---")
        
        content = """
        #: src/some/file.php:123
        msgid "Hello"
        msgstr ""

        #: src/another/file.php:45
        msgid "World"
        msgstr ""
        """
        
        result = parse_pot(content)
        
        self.assertIn("Hello", result["msgids"])
        self.assertIn("World", result["msgids"])
        self.assertEqual(len(result["msgids"]), 2)
        print("✅ PASSED: POT parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

