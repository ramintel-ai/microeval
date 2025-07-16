"""
MicroEval main entry point.
"""

import argparse
from .benchmark.runner import BenchmarkRunner
from .utils import load_config

def main():
    parser = argparse.ArgumentParser(description='MicroEval: Micro Language Model Evaluation Framework')
    parser.add_argument('--config', type=str, help='Path to config file (YAML/JSON/TOML)')
    args = parser.parse_args()

    config = load_config(args.config)
    runner = BenchmarkRunner(config)
    runner.run()

if __name__ == '__main__':
    main() 