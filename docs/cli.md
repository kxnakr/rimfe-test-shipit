# CLI reference

```
shipit DIRECTORY [--env staging|production] [--dry-run] [--concurrency N]
```

| Flag | Default | Description |
| --- | --- | --- |
| `--env` | `staging` | Target environment. |
| `--dry-run` | off | Print what would be uploaded without uploading. |
| `--concurrency` | `4` | Number of parallel uploads. |
