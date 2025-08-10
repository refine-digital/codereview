# File: tests/test_connections/test_openai_connection/test_openai_connection.py
# Version: 1.2.1
import unittest
import os
import sys
import openai
from pathlib import Path

# Add project root to path to allow importing test_utils
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from tests.test_utils import load_test_config

class TestOpenAIConnection(unittest.TestCase):
    """
    Tests the connection to the OpenAI API.
    """

    @classmethod
    def setUpClass(cls):
        """Load configurations using the centralized utility."""
        cls.config, cls.env_vars = load_test_config(Path(__file__).resolve().parent)

    def test_openai_list_models(self):
        """
        Verifies that the client can connect to OpenAI and list models.
        This requires a valid OPENAI_API_KEY to be set.
        """
        print("\n[1] Testing Connection to OpenAI API...")
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key or "DUMMY" in api_key:
            self.fail("OPENAI_API_KEY is not set or is a dummy key. This is a live connection test and requires a valid API key.")

        try:
            client = openai.OpenAI(api_key=api_key)
            models = client.models.list()
            self.assertIsNotNone(models)
            self.assertGreater(len(models.data), 0, "The response from OpenAI did not contain any models.")
            print(f"✅ PASSED: Successfully connected to OpenAI and found models.")
        except openai.AuthenticationError:
            self.fail("Failed to connect to the OpenAI API due to an authentication error. Please check your API key.")
        except Exception as e:
            self.fail(f"Failed to connect to the OpenAI API. Please check your network connection. Error: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
