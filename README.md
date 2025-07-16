# MicroEval

Flexible, extensible framework for benchmarking micro language models (<2B params) from Ollama, HuggingFace, and more.

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