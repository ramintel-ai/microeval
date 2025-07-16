import os
import yaml
import json
import toml

def load_config(path):
    if path.endswith('.yaml') or path.endswith('.yml'):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    elif path.endswith('.json'):
        with open(path, 'r') as f:
            return json.load(f)
    elif path.endswith('.toml'):
        with open(path, 'r') as f:
            return toml.load(f)
    else:
        raise ValueError('Unsupported config format')

# Plugin discovery utilities can be added here 