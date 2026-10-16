import argparse
import os

from shipit.deploy import deploy


def main() -> None:
    parser = argparse.ArgumentParser(prog="shipit", description="Deploy a static site.")
    parser.add_argument("directory", help="Folder to upload.")
    parser.add_argument("--env", choices=["staging", "production"], default="staging")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be uploaded.")
    parser.add_argument("--concurrency", type=int, default=4, help="Parallel uploads.")
    args = parser.parse_args()
    token = os.environ.get("SHIPIT_TOKEN")
    if not token:
        raise SystemExit("SHIPIT_TOKEN is not set")
    deploy(args.directory, env=args.env, dry_run=args.dry_run, concurrency=args.concurrency, token=token)
