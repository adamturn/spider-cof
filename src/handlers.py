import pathlib


def get_src_dir(file: str) -> pathlib.Path:
    """Returns the Path to this project's /src directory.

    Args:
        file: __file__
    """
    src_dir = str(pathlib.Path(file).parent.absolute())

    if src_dir.lower().endswith("src"):
        return pathlib.Path(src_dir)
    else:
        raise ValueError(f"This file is not in the `src/` directory: `{src_dir}`")
