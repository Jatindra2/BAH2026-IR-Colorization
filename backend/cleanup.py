from pathlib import Path


def remove_file(path: Path):

    try:

        if path.exists():
            path.unlink()

    except Exception:
        pass