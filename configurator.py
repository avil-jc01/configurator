#!/usr/bin/env python
import os
from pathlib import Path


def get_env_vars():
    env_vars = {}

    for k, v in os.environ.items():
        env_vars[k] = v

    return env_vars


def get_config(config_path):
    config = {}

    with open(config_path) as f:
        for line in f:
            line = line.strip()

            # skip blank lines
            if not line:
                continue

            # don't pick up commented lines
            if line[0] == "#" or line[0] == ";":
                continue

            _values = line.split("=")

            config[_values[0].strip()] = _values[1].strip()

    return config


# print(get_env_vars())
print(get_config(Path("config.ini")))
