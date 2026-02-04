import os
from pathlib import Path


def get_default_config_path(target: str = "config.toml") -> Path:
    return (
        Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config")) / "roboapp" / target
    )
