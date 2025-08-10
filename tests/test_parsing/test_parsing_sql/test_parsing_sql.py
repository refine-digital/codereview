# File: tests/test_parsing/test_parsing_sql/test_parsing_sql.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from parsers.sql_handler import parse as parse_sql

class TestParsingSQL(unittest.TestCase):
    """
    Tests the SQL parser.
    """

    def test_sql_parsing(self):
        """
        Verifies that the SQL parser correctly extracts tables and columns.
        """
        print("\n--- Testing SQL Parsing ---")
        
        content = """
        CREATE TABLE users (
            id INT PRIMARY KEY,
            username VARCHAR(255)
        );
        """
        
        result = parse_sql(content)
        
        self.assertIn("users", result["tables"])
        self.assertIn("id", result["columns"])
        self.assertIn("username", result["columns"])
        print("✅ PASSED: SQL parsing test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

