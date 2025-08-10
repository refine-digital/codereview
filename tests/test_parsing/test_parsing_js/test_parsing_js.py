# File: tests/test_parsing/test_parsing_js/test_parsing_js.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.js_handler import parse as parse_js

class TestParsingJS(unittest.TestCase):
    """
    Tests the JavaScript parser.
    """

    def test_js_parsing(self):
        """
        Verifies that the JS parser correctly extracts functions, classes, and imports.
        """
        print("\n--- Testing JavaScript Parsing ---")
        
        content = """
        import { something } from 'some-module';
        
        function myFunction(a, b) {
            return a + b;
        }

        class MyClass {
            constructor() {
                this.value = 1;
            }

            myMethod() {
                return this.value;
            }
        }

        const myArrowFunction = () => {
            console.log("hello");
        };
        """
        
        result = parse_js(content)
        
        self.assertIn("myFunction", result["functions"])
        self.assertIn("myArrowFunction", result["functions"])
        self.assertIn("MyClass", result["classes"])
        self.assertIn("some-module", result["imports"])
        print("✅ PASSED: JavaScript parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
