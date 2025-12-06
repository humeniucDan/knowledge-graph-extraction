import os
from pathlib import Path

__rootPath = Path.cwd()

def __compute_cache_paths():
    paths = ["hf_cache", "data", "models"]

    for path in paths:
        os.makedirs(__rootPath.joinpath(path), exist_ok=True)

    return (
        __rootPath.joinpath("hf_cache"),
        __rootPath.joinpath("data"),
        __rootPath.joinpath("models")
    )

HF_PATH, DATA_PATH, MODEL_PATH = __compute_cache_paths()
