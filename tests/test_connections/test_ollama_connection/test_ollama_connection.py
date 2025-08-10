# File: tests/test_connections/test_ollama_connection/test_ollama_connection.py
# Version: 1.2.1
import unittest
import ollama
import yaml
from pathlib import Path
from dotenv import dotenv_values

class TestOllamaConnection(unittest.TestCase):
    """
    Tests the connection to the local Ollama server.
    """

    @classmethod
    def setUpClass(cls):
        """Load base and override configurations."""
        print("\n--- Loading Configuration for Ollama Connection Test ---")
        cls.test_dir = Path(__file__).resolve().parent
        
        base_config_path = cls.test_dir / "config.yaml"
        with open(base_config_path, 'r') as f:
            cls.config = yaml.safe_load(f)

        base_env_path = cls.test_dir / ".env"
        cls.env_vars = dotenv_values(base_env_path)

        override_config_path = cls.test_dir / "config.override.yaml"
        if override_config_path.exists():
            with open(override_config_path, 'r') as f:
                override_config = yaml.safe_load(f)
                cls.config.update(override_config)
        
        override_env_path = cls.test_dir / ".env.override"
        if override_env_path.exists():
            cls.env_vars.update(dotenv_values(override_env_path))

    def test_ollama_list_models(self):
        """
        Verifies that the client can connect to Ollama and list models.
        This requires the Ollama server to be running locally.
        """
        print("\n[1] Testing Connection to Ollama Server...")
        try:
            client = ollama.Client(host=self.env_vars.get("OLLAMA_BASE_URL", "http://localhost:11434"))
            response = client.list()
            
            self.assertTrue(response, "The response from ollama.list() should not be empty.")
            
            print(f"✅ PASSED: Successfully connected to Ollama.")

        except Exception as e:
            self.fail(f"Failed to connect to the Ollama server. Please ensure it is running and OLLAMA_BASE_URL is correct. Error: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)

