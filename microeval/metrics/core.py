from abc import ABC, abstractmethod

class BaseMetric(ABC):
    @abstractmethod
    def compute(self, prediction, reference) -> float:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass 