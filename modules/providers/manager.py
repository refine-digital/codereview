# File: modules/providers/manager.py
# Version: 1.0.0
from .ollama_provider import OllamaProvider
from .openai_provider import OpenAIProvider
from .gemini_provider import GeminiProvider

class ProviderManager:
    """
    Manages the creation and retrieval of provider instances.
    """
    def __init__(self, agent_assignments, external_apis_config):
        self.agent_assignments = agent_assignments
        self.external_apis_config = external_apis_config
        self._providers = {}

    def get_provider(self, agent_name):
        if agent_name in self._providers:
            return self._providers[agent_name]

        assignment = self.agent_assignments.get(agent_name)
        if not assignment:
            raise ValueError(f"No assignment found for agent '{agent_name}'.")

        provider_name = assignment['provider']
        model_name = assignment['model']

        if provider_name == "ollama":
            provider = OllamaProvider({"model": model_name})
        elif provider_name == "openai":
            config = self.external_apis_config['openai']
            config['model'] = model_name
            provider = OpenAIProvider(config)
        elif provider_name == "gemini":
            config = self.external_apis_config['gemini']
            config['model'] = model_name
            provider = GeminiProvider(config)
        else:
            raise ValueError(f"Unsupported provider: {provider_name}")

        self._providers[agent_name] = provider
        return provider
