# File: tests/test_parsing/test_parsing_md/test_parsing_md.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.md_handler import parse as parse_md

class TestParsingMD(unittest.TestCase):
    """
    Tests the Markdown parser.
    """

    def test_md_parsing(self):
        """
        Verifies that the MD parser correctly extracts headings and links.
        """
        print("\n--- Testing Markdown Parsing ---")
        
        content = """
        # Heading 1
        
        Some text.
        
        ## Heading 2
        
        [A link](https://example.com)
        """
        
        result = parse_md(content)
        
        self.assertIn("Heading 1", result["headings"])
        self.assertIn("Heading 2", result["headings"])
        self.assertIn("https://example.com", result["links"])
        print("✅ PASSED: Markdown parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

