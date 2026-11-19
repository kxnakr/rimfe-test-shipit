from pathlib import Path


def _list_files(directory: str) -> list[Path]:
    return sorted(p for p in Path(directory).rglob("*") if p.is_file())


def deploy(directory: str, *, env: str, dry_run: bool, concurrency: int, token: str) -> None:
    for path in _list_files(directory):
        if dry_run:
            print(f"would upload {path}")
            continue
        print(f"uploading {path} to {env}")
