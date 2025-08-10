# File: tests/test_parsing/test_parsing_html/test_parsing_html.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.html_handler import parse as parse_html

class TestParsingHTML(unittest.TestCase):
    """
    Tests the HTML parser.
    """

    def test_html_parsing(self):
        """
        Verifies that the HTML parser correctly extracts significant tags, links, and scripts.
        """
        print("\n--- Testing HTML Parsing ---")
        
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page</title>
            <script src="header.js"></script>
        </head>
        <body>
            <h1>Hello</h1>
            <p>This is a test.</p>
            <a href="/link1">Link 1</a>
            <div>
                <a href="/link2">Link 2</a>
            </div>
            <form action="/submit" method="post">
                <input type="text" name="username">
                <button type="submit">Submit</button>
            </form>
            <img src="image.jpg">
            <script src="footer.js"></script>
        </body>
        </html>
        """
        
        result = parse_html(content)
        
        self.assertIn("a", result["tags"])
        self.assertIn("script", result["tags"])
        self.assertIn("img", result["tags"])
        self.assertIn("form", result["tags"])
        self.assertIn("input", result["tags"])
        self.assertIn("button", result["tags"])
        self.assertNotIn("p", result["tags"], "Common layout tags like <p> should be excluded.")
        self.assertNotIn("div", result["tags"], "Common layout tags like <div> should be excluded.")
        
        self.assertIn("/link1", result["links"])
        self.assertIn("/link2", result["links"])
        
        self.assertIn("header.js", result["scripts"])
        self.assertIn("footer.js", result["scripts"])
        
        print("✅ PASSED: HTML parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
