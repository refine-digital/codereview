# File: tests/test_parsing/test_parsing_tsx/test_parsing_tsx.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.tsx_handler import parse as parse_tsx

class TestParsingTSX(unittest.TestCase):
    """
    Tests the TypeScript with JSX (TSX) parser.
    """

    def test_tsx_parsing(self):
        """
        Verifies that the TSX parser correctly extracts functions, interfaces, and imports.
        """
        print("\n--- Testing TSX Parsing ---")
        
        content = """
        import React from 'react';

        interface MyComponentProps {
          name: string;
        }

        const MyComponent: React.FC<MyComponentProps> = ({ name }) => {
          return <h1>Hello, {name}</h1>;
        };

        export default MyComponent;
        """
        
        result = parse_tsx(content)
        
        self.assertIn("MyComponent", result["functions"])
        self.assertIn("MyComponentProps", result["interfaces"])
        self.assertIn("react", result["imports"])
        print("✅ PASSED: TSX parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
