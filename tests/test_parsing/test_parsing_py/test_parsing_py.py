# File: tests/test_parsing/test_parsing_py/test_parsing_py.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.py_handler import parse as parse_py

class TestParsingPY(unittest.TestCase):
    """
    Tests the Python parser.
    """

    def test_py_parsing(self):
        """
        Verifies that the Python parser correctly extracts functions, classes, and imports.
        """
        print("\n--- Testing Python Parsing ---")
        
        content = """
import os
from pathlib import Path

class MyClass:
    def __init__(self):
        self.value = 1

def my_function(a, b):
    return a + b
        """
        
        result = parse_py(content)
        
        self.assertIn("my_function", result["functions"])
        self.assertIn("MyClass", result["classes"])
        self.assertIn("os", result["imports"])
        self.assertIn("pathlib", result["from_imports"])
        print("✅ PASSED: Python parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

