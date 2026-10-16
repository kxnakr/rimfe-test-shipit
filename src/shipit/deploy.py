from pathlib import Path


def deploy(directory: str, *, env: str, dry_run: bool, concurrency: int, token: str, region: str = "us") -> None:
    files = [p for p in Path(directory).rglob("*") if p.is_file()]
    for path in files:
        if dry_run:
            print(f"would upload {path}")
            continue
        print(f"uploading {path} to {env} in {region}")
