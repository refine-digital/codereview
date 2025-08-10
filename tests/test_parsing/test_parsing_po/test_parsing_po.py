# File: tests/test_parsing/test_parsing_po/test_parsing_po.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.po_handler import parse as parse_po

class TestParsingPO(unittest.TestCase):
    """
    Tests the PO file parser.
    """

    def test_po_parsing(self):
        """
        Verifies that the PO parser correctly extracts msgid and msgstr entries.
        """
        print("\n--- Testing PO Parsing ---")
        
        content = """
        msgid "Hello"
        msgstr "Hola"

        msgid "World"
        msgstr "Mundo"
        """
        
        result = parse_po(content)
        
        self.assertIn("Hello", result["entries"])
        self.assertEqual(result["entries"]["Hello"], "Hola")
        self.assertIn("World", result["entries"])
        self.assertEqual(result["entries"]["World"], "Mundo")
        print("✅ PASSED: PO parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

