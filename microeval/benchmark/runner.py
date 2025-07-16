import importlib
from ..model.base import BaseModel
from ..dataset.loader import BaseDataset
from ..metrics.core import BaseMetric

class BenchmarkRunner:
    def __init__(self, config):
        self.config = config
        self.models = []
        self.datasets = []
        self.metrics = []
        self._discover_plugins()
        self._prompt_for_features_and_metrics()

    def _discover_plugins(self):
        # Discover and register model, dataset, and metric plugins
        # For now, statically import built-in plugins
        from ..model.ollama import OllamaModel
        from ..model.huggingface import HuggingFaceModel
        self.model_plugins = {
            'ollama': OllamaModel,
            'huggingface': HuggingFaceModel
        }
        # Extend for datasets and metrics as needed

    def _prompt_for_features_and_metrics(self):
        print("\n=== MicroEval: Dataset Features & Metrics Selection ===")
        # Prompt for dataset features
        features = input("Enter required dataset features (comma-separated, e.g., 'input,output'): ")
        self.selected_features = [f.strip() for f in features.split(',') if f.strip()]
        # Prompt for metrics
        metrics = input("Enter evaluation metrics (comma-separated, e.g., 'accuracy,bleu'): ")
        self.selected_metrics = [m.strip() for m in metrics.split(',') if m.strip()]
        print(f"Selected features: {self.selected_features}")
        print(f"Selected metrics: {self.selected_metrics}\n")

    def run(self):
        print("Running benchmarks...")
        # Main benchmark logic here
        # For each model, dataset, and metric, run evaluation
        for model_name, model_cls in self.model_plugins.items():
            print(f"Benchmarking model: {model_name}")
            # Example: instantiate and run dummy benchmark
            model = model_cls(model_name)
            # ... load dataset, run metrics, etc.
        print("Benchmarking complete.") 