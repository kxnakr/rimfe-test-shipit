# Configuration

shipit reads these environment variables:

- `SHIPIT_TOKEN` (required): deploy token from the dashboard. shipit exits with `SHIPIT_TOKEN is not set` when it is missing.
- `SHIPIT_REGION` (optional): region to deploy to. Defaults to `us`.
