# File: tests/test_parsing/test_parsing_ts/test_parsing_ts.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.ts_handler import parse as parse_ts

class TestParsingTS(unittest.TestCase):
    """
    Tests the TypeScript parser.
    """

    def test_ts_parsing(self):
        """
        Verifies that the TS parser correctly extracts functions, classes, and imports.
        """
        print("\n--- Testing TypeScript Parsing ---")
        
        content = """
        import { something } from 'some-module';
        
        function myFunction(a: number, b: number): number {
            return a + b;
        }

        class MyClass {
            private value: number;

            constructor() {
                this.value = 1;
            }

            myMethod(): number {
                return this.value;
            }
        }
        """
        
        result = parse_ts(content)
        
        self.assertIn("myFunction", result["functions"])
        self.assertIn("MyClass", result["classes"])
        self.assertIn("some-module", result["imports"])
        print("✅ PASSED: TypeScript parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
