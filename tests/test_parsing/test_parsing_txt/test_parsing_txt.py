# File: tests/test_parsing/test_parsing_txt/test_parsing_txt.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.txt_handler import parse as parse_txt

class TestParsingTXT(unittest.TestCase):
    """
    Tests the TXT file parser.
    """

    def test_txt_parsing(self):
        """
        Verifies that the TXT parser correctly extracts paragraphs.
        """
        print("\n--- Testing TXT Parsing ---")
        
        content = """
        This is the first paragraph.

        This is the second paragraph.
        """
        
        result = parse_txt(content)
        
        self.assertEqual(len(result["paragraphs"]), 2)
        self.assertEqual(result["paragraphs"], ["This is the first paragraph.", "This is the second paragraph."])
        print("✅ PASSED: TXT parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
