# MicroEval

Flexible, extensible framework for benchmarking micro language models (<2B params) from Ollama, HuggingFace, and more.

**MicroEval** is a GenAI-based tool and framework designed for benchmarking and evaluating micro language models (under 2B parameters). Leveraging the latest advances in generative AI, MicroEval provides a flexible, extensible, and community-driven solution for researchers, developers, and enthusiasts working with small language models.

## Advantages & Benefits
- **GenAI-Powered Evaluation:** Utilizes generative AI techniques for robust and insightful benchmarking of language models.
- **Extensible Architecture:** Easily add new models, datasets, and metrics via a plugin-based system.
- **Cross-Platform & Flexible:** Use via CLI or Python API, and configure with YAML, JSON, or TOML.
- **Community-Oriented:** Open source and designed for collaboration, making it easy to contribute and extend.
- **Automatic Benchmarking:** Streamlines the process of creating and running benchmarks for a wide variety of models and datasets.
- **Supports Multiple Model Sources:** Works with models from Ollama, HuggingFace, and more.
- **Comprehensive Documentation:** Detailed guides and examples to help users get started and extend the framework.

## Features
- Plugin-based model, dataset, and metric support
- Automatic benchmark creation
- CLI and Python API
- Configurable via YAML, JSON, TOML
- Dynamic plugin loading
- Comprehensive documentation

## Installation
```bash
pip install -r requirements.txt
```

## Usage
### CLI
```bash
python -m microeval.main --config path/to/config.yaml
```

### Example Config (YAML)
```yaml
models:
  - type: ollama
    name: tinyllama
  - type: huggingface
    name: distilbert-base-uncased

dataset:
  type: csv
  path: data/eval.csv

metrics:
  - accuracy
  - bleu
```

### Python API
```python
from microeval.main import main
main()
```

## Extending MicroEval
- Add new models: subclass `BaseModel` in `microeval/model/`
- Add new datasets: subclass `BaseDataset` in `microeval/dataset/`
- Add new metrics: subclass `BaseMetric` in `microeval/metrics/`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
