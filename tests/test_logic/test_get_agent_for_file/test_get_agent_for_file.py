# File: tests/test_logic/test_get_agent_for_file/test_get_agent_for_file.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from modules.agent_logic import get_agent_for_file

class TestGetAgentForFile(unittest.TestCase):
    """
    Tests the get_agent_for_file function.
    """

    def test_agent_mapping(self):
        """
        Verifies that file extensions are correctly mapped to their designated agent names.
        """
        print("\n--- Testing Agent Mapping ---")
        
        self.assertEqual(get_agent_for_file("php"), "php_reviewer")
        self.assertEqual(get_agent_for_file("sql"), "mysql_reviewer")
        self.assertEqual(get_agent_for_file("js"), "project_lead") # Fallback
        self.assertEqual(get_agent_for_file("xyz"), "project_lead") # Fallback
        
        print("✅ PASSED: Agent mapping test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)

