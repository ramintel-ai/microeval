from .base import BaseModel

class OllamaModel(BaseModel):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Initialize Ollama client here

    def generate(self, prompt: str, **kwargs) -> str:
        # Call Ollama API here
        return "[Ollama response]"

    def get_name(self) -> str:
        return f"ollama:{self.model_name}" 