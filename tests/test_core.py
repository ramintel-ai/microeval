import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from microeval.model.base import BaseModel
from microeval.dataset.loader import BaseDataset
from microeval.metrics.core import BaseMetric
from microeval.benchmark.runner import BenchmarkRunner

class DummyModel(BaseModel):
    def generate(self, prompt: str, **kwargs) -> str:
        return "dummy"
    def get_name(self) -> str:
        return "dummy"

class DummyDataset(BaseDataset):
    def load(self):
        return ["sample"]
    def get_features(self):
        return ["input", "output"]

class DummyMetric(BaseMetric):
    def compute(self, prediction, reference) -> float:
        return 1.0
    def get_name(self) -> str:
        return "dummy_metric"

class TestMicroEval(unittest.TestCase):
    def test_model(self):
        m = DummyModel()
        self.assertEqual(m.generate("test"), "dummy")
        self.assertEqual(m.get_name(), "dummy")
    def test_dataset(self):
        d = DummyDataset()
        self.assertEqual(d.load(), ["sample"])
        self.assertEqual(d.get_features(), ["input", "output"])
    def test_metric(self):
        metric = DummyMetric()
        self.assertEqual(metric.compute("a", "b"), 1.0)
        self.assertEqual(metric.get_name(), "dummy_metric")
    def test_benchmark_runner_init(self):
        config = {}
        runner = BenchmarkRunner(config)
        self.assertIsInstance(runner, BenchmarkRunner)

if __name__ == "__main__":
    unittest.main() 