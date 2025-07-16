from .base import BaseModel

class HuggingFaceModel(BaseModel):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Initialize HuggingFace pipeline here

    def generate(self, prompt: str, **kwargs) -> str:
        # Call HuggingFace pipeline here
        return "[HuggingFace response]"

    def get_name(self) -> str:
        return f"huggingface:{self.model_name}" 