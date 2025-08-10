# File: modules/providers/ollama_provider.py
# Version: 1.0.0
from .base_provider import BaseProvider
from openai import OpenAI

class OllamaProvider(BaseProvider):
    """
    Provider implementation for Ollama.
    """

    def __init__(self, config):
        self.config = config
        self.connection = None

    def get_connection(self):
        if not self.connection:
            self.connection = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        return self.connection

    def construct_prompt(self, agent_persona, task, context):
        # For now, a simple prompt construction. This will be expanded.
        return f"{agent_persona}\n\n{task}\n\n--- CONTEXT ---\n{context}"

    def execute_prompt(self, prompt):
        connection = self.get_connection()
        response = connection.chat.completions.create(
            model=self.config['model'],
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def get_cache(self, prompt):
        # Caching to be implemented
        return None

    def set_cache(self, prompt, response):
        # Caching to be implemented
        pass
