"""Handling of configuration files"""
import json


def load_json_config(filename='./client_secrets.json'):
    config = None
    with open(filename) as f:
        config = json.load(f)
    return config
