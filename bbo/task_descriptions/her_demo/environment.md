# Environment

Recommended setup:

```bash
uv sync --extra dev --extra bo-tutorial
```

The task looks for the tutorial source checkout through `BBO_BO_TUTORIAL_SOURCE_ROOT` and stages cached files under `BBO_BO_TUTORIAL_CACHE_ROOT` or the default artifact cache.
Runtime dependencies include `pandas` and `scikit-learn`; no task-local Docker workflow is required for this smoke benchmark.
