# File: tests/test_connections/test_gemini_connection/test_gemini_connection.py
# Version: 1.2.0
import unittest
import os
import sys
import google.generativeai as genai
from pathlib import Path

# Add project root to path to allow importing test_utils
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from tests.test_utils import load_test_config

class TestGeminiConnection(unittest.TestCase):
    """
    Tests the connection to the Google Gemini API.
    """

    @classmethod
    def setUpClass(cls):
        """Load configurations using the centralized utility."""
        cls.config, cls.env_vars = load_test_config(Path(__file__).resolve().parent)

    def test_gemini_list_models(self):
        """
        Verifies that the client can connect to Gemini and list models.
        This requires a valid GEMINI_API_KEY to be set.
        """
        print("\n[1] Testing Connection to Google Gemini API...")
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or "DUMMY" in api_key:
            self.skipTest("GEMINI_API_KEY is not set or is a dummy key. Skipping live connection test.")

        try:
            genai.configure(api_key=api_key)
            models = genai.list_models()
            model_list = list(models)
            self.assertIsNotNone(model_list)
            self.assertGreater(len(model_list), 0, "The response from Gemini did not contain any models.")
            print(f"✅ PASSED: Successfully connected to Gemini and found models.")
        except Exception as e:
            self.fail(f"Failed to connect to the Gemini API. Please check your API key and network connection. Error: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
