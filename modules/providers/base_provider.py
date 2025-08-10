# File: modules/providers/base_provider.py
# Version: 1.0.0
from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for all provider implementations.
    """

    @abstractmethod
    def get_connection(self):
        """
        Returns a connection object for the provider.
        """
        pass

    @abstractmethod
    def construct_prompt(self, agent_persona, task, context):
        """
        Constructs a provider-specific prompt.
        """
        pass

    @abstractmethod
    def execute_prompt(self, prompt):
        """
        Executes a prompt and returns the result.
        """
        pass

    @abstractmethod
    def get_cache(self, prompt):
        """
        Retrieves a cached response for a prompt, if available.
        """
        pass

    @abstractmethod
    def set_cache(self, prompt, response):
        """
        Caches a response for a prompt.
        """
        pass
