from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Abstract base class for all model plugins."""
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass 