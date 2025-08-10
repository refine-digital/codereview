# File: tests/test_parsing/test_parsing_php/test_parsing_php.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.php_handler import parse as parse_php

class TestParsingPHP(unittest.TestCase):
    """
    Tests the PHP parser.
    """

    def test_php_parsing(self):
        """
        Verifies that the PHP parser correctly extracts functions, classes, and namespaces.
        """
        print("\n--- Testing PHP Parsing ---")
        
        content = """
        <?php
        namespace MyNamespace;

        class MyClass {
            public function myMethod() {
                return true;
            }
        }

        function myFunction() {
            return false;
        }
        """
        
        result = parse_php(content)
        
        self.assertTrue(any(c['name'] == 'MyClass' for c in result['classes']))
        self.assertTrue(any(f['name'] == 'myFunction' for f in result['functions']))
        self.assertIn("MyNamespace", result["namespaces"])
        print("✅ PASSED: PHP parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

