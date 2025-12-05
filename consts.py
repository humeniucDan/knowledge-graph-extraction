from pathlib import Path

def __compute_cache_paths():
    rootPath = Path.cwd()
    return (
        rootPath.joinpath("hf_cache"),
        rootPath.joinpath("data"),
        rootPath.joinpath("models")
    )

HF_PATH, DATA_PATH, MODEL_PATH = __compute_cache_paths()
