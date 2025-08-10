# File: tests/test_config_integrity/test_config_integrity.py
# Version: 2.1.2
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
import unittest

class TestConfigIntegrity(unittest.TestCase):
    """
    This test suite validates the structure of a copy of the project's 
    config.yaml and .env files. It is fully isolated.
    """

    @classmethod
    def setUpClass(cls):
        """Load the configuration from this test's directory."""
        print("\n--- Loading Configuration for Validation ---")
        
        cls.test_dir = Path(__file__).resolve().parent
        config_path = cls.test_dir / "config.yaml"
        env_path = cls.test_dir / ".env"

        if not config_path.exists():
            raise FileNotFoundError(f"Copy of 'config.yaml' not found at {config_path}")
        if not env_path.exists():
            raise FileNotFoundError(f"Copy of '.env' not found at {env_path}")
        
        # This loads variables from the .env file. It will NOT override
        # any variables that are already set in the system environment.
        load_dotenv(dotenv_path=env_path)

        with open(config_path) as f:
            cls.config = yaml.safe_load(f)

    def test_top_level_keys_exist(self):
        """Checks for the presence of all required top-level sections."""
        print("\n[1] Checking for required top-level keys...")
        required_keys = [
            "current_environment",
            "system_capabilities",
            "agents",
            "external_apis",
            "rag_tasks",
            "project_lead_tasks"
        ]
        for key in required_keys:
            self.assertIn(key, self.config, f"Top-level key '{key}' is missing from config.yaml")
        print("✅ PASSED: All required top-level keys are present.")

    def test_current_environment_is_valid(self):
        """Ensures the current_environment points to a valid system_capability."""
        print("\n[2] Validating the 'current_environment' setting...")
        current_env = self.config["current_environment"]
        self.assertIn(current_env, self.config["system_capabilities"], 
                      f"'current_environment' is set to '{current_env}', which is not defined in 'system_capabilities'.")
        print(f"✅ PASSED: Current environment '{current_env}' is valid.")

    def test_agent_model_assignments_are_complete(self):
        """Verifies that every agent has a model assignment in the current environment."""
        print("\n[3] Validating agent model assignments for the current environment...")
        current_env = self.config["current_environment"]
        assignments = self.config["system_capabilities"][current_env].get("agent_model_assignments", {})
        
        all_agents = self.config["agents"].keys()
        for agent_name in all_agents:
            self.assertIn(agent_name, assignments,
                          f"Agent '{agent_name}' is missing a model assignment in the '{current_env}' environment.")
            self.assertIn("provider", assignments[agent_name], f"Provider is missing for '{agent_name}'.")
            self.assertIn("model", assignments[agent_name], f"Model is missing for '{agent_name}'.")
        print("✅ PASSED: All agents have a valid model assignment.")

    def test_environment_variables_for_external_apis(self):
        """Checks if API keys specified in config.yaml are documented in the .env file."""
        print("\n[4] Checking for required environment variables...")
        external_apis = self.config.get("external_apis", {})
        
        with open(self.test_dir / ".env", 'r') as f:
            env_content = f.read()

        for provider, details in external_apis.items():
            api_key_env_var = details.get("api_key_env")
            self.assertIsNotNone(api_key_env_var, f"'api_key_env' not set for provider '{provider}'.")

            # Check if the variable name exists in the .env file, even if commented out.
            # This ensures the variable is at least documented for the user.
            self.assertIn(
                api_key_env_var, 
                env_content,
                f"Environment variable '{api_key_env_var}' for provider '{provider}' is not documented in the test's .env file."
            )
            print(f"  - Found documented variable '{api_key_env_var}' for provider '{provider}'.")

        print("✅ PASSED: All required API keys are documented in the .env file.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
