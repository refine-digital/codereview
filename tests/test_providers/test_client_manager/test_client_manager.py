# File: tests/test_providers/test_client_manager/test_client_manager.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from modules.providers.manager import ProviderManager
from modules.providers.ollama_provider import OllamaProvider
from modules.providers.openai_provider import OpenAIProvider
from modules.providers.gemini_provider import GeminiProvider

class TestProviderManager(unittest.TestCase):
    """
    Tests the ProviderManager.
    """

    def test_provider_selection(self):
        """
        Verifies that the ProviderManager correctly selects the provider.
        """
        print("\n--- Testing Provider Selection ---")
        
        agent_assignments = {
            "ollama_agent": {"provider": "ollama", "model": "test_model"},
            "openai_agent": {"provider": "openai", "model": "test_model"},
            "gemini_agent": {"provider": "gemini", "model": "test_model"},
        }
        
        external_apis_config = {
            "openai": {"api_key_env": "OPENAI_API_KEY"},
            "gemini": {"api_key_env": "GEMINI_API_KEY"},
        }

        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test', 'GEMINI_API_KEY': 'test'}):
            manager = ProviderManager(agent_assignments, external_apis_config)
            
            self.assertIsInstance(manager.get_provider("ollama_agent"), OllamaProvider)
            self.assertIsInstance(manager.get_provider("openai_agent"), OpenAIProvider)
            self.assertIsInstance(manager.get_provider("gemini_agent"), GeminiProvider)
        
        print("✅ PASSED: Provider selection test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
