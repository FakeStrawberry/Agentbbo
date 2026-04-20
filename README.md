# Agentic BBO Benchmark Core

Language versions:
- English: `README.md`
- 中文：`README.zh.md`

## Overview

This repository provides a compact benchmark framework for agentic black-box optimization.
It is organized as a standard Python package under `bbo/`, with clear separation between reusable core abstractions, algorithm families, task families, documentation assets, and runnable examples.

The current repository serves three purposes:

- provide a small but well-structured benchmark core for future agent-based optimization methods
- provide executable traditional baselines for validation and comparison
- provide a standardized task-description format that collaborators can extend for new benchmark problems

## Repository layout

```text
.
├── AGENTS.md
├── README.md
├── README.zh.md
├── bbo/
│   ├── __init__.py
│   ├── algorithms/
│   │   ├── registry.py
│   │   └── traditional/
│   ├── core/
│   ├── run.py
│   ├── task_descriptions/
│   └── tasks/
├── docs/
├── examples/
├── tests/
└── pyproject.toml
```

### `bbo/core/`

Reusable benchmark abstractions:

- search-space definitions
- task specification and sanity checks
- trial records
- logging and replay
- experiment orchestration
- task-description loading
- plotting utilities
- external optimizer adapters

### `bbo/algorithms/`

Algorithm implementations are grouped by family.
Current family:

- `bbo/algorithms/traditional/`
  - `random_search.py`
  - `pycma.py`

### `bbo/tasks/`

Task implementations are also grouped by family.
Current families:

- `bbo/tasks/synthetic/`
  - `branin.py`
  - `sphere.py`
  - `base.py`
- `bbo/tasks/bboplace/`
  - `task.py`

### `bbo/task_descriptions/`

Standardized task packaging for benchmark context.
The current repository includes:

- runnable benchmark descriptions for `branin_demo`, `sphere_demo`, and `bboplace_bench`
- a collaborator-facing packaging example
- a reusable template
- bilingual documentation companions

## Installation

Create the managed environment with `uv`:

```bash
uv sync --extra dev
```

Optional interoperability helpers for ConfigSpace can be installed with:

```bash
uv sync --extra dev --extra interop
```

## Running the demos

### Full comparison suite

```bash
uv run python -m bbo.run --algorithm suite --task branin_demo
```

Equivalent example script:

```bash
uv run python examples/run_branin_suite.py
```

### Random-search baseline

```bash
uv run python examples/run_random_search_demo.py
```

### CMA-ES baseline

```bash
uv run python examples/run_pycma_demo.py
```

### Direct CLI example

```bash
uv run python -m bbo.run \
  --algorithm pycma \
  --task branin_demo \
  --max-evaluations 36 \
  --sigma-fraction 0.18 \
  --popsize 6
```

### BBOPlace HTTP task

Start the published evaluator service first:

```bash
docker pull gaozhixuan/bboplace-bench
docker run --rm -p 8080:8080 gaozhixuan/bboplace-bench
```

Then run a quick smoke test from this repo:

```bash
uv run python -m bbo.run --algorithm random_search --task bboplace_bench --max-evaluations 1
```

## Outputs

Runs write JSONL histories, summaries, and plots under `artifacts/`.
A validated reference run is available under `artifacts/final_demo_v3/`.

Generated visualization artifacts currently include:

- optimization trace plots
- objective distribution plots
- 2D landscape overlays for visualizable tasks
- optimizer comparison plots

## Task-description standard

Each benchmark task should live under `bbo/task_descriptions/<task_name>/`.
Required files:

```text
background.md
goal.md
constraints.md
prior_knowledge.md
```

Recommended optional files:

```text
evaluation.md
submission.md
environment.md
notes.md
history.md
```

Localized companion files such as `background.zh.md` are supported for documentation purposes.
They are ignored by the loader during runtime so benchmark context remains deterministic.

Each task must also provide at least one environment provisioning path:

- a task-local Docker workflow
- or explicit setup instructions in `environment.md`

Related documentation:

- `bbo/task_descriptions/README.md`
- `bbo/task_descriptions/README.zh.md`
- `docs/collaborator_demo.md`
- `docs/collaborator_demo.zh.md`
- `bbo/core/DEVELOPER_GUIDE_zh.md`
- `bbo/core/IMPLEMENTATION_PLAN.md`
- `bbo/core/IMPLEMENTATION_PLAN.zh.md`

## Adding a new task

1. Copy `bbo/task_descriptions/_template/` into `bbo/task_descriptions/<task_name>/`.
2. Add or extend a task family under `bbo/tasks/`.
3. Define the search space explicitly with `SearchSpace` and typed parameters.
4. Return normalized `EvaluationResult` objects from the evaluator.
5. Add tests and run the validation commands below.

## Validation commands

```bash
uv run python -m compileall -q bbo examples tests
uv run pytest
uv run python -m bbo.run --algorithm suite --task branin_demo --results-root artifacts/final_demo
```

## Current reference benchmarks

- `branin_demo`: two-dimensional synthetic benchmark for visualization and optimizer comparisons
- `sphere_demo`: convex synthetic benchmark for smoke tests and replay/resume validation
- `bboplace_bench`: HTTP-backed macro-placement benchmark adapter for BBOPlace-Bench MGO evaluation
- `collaborator_problem_demo`: documentation-focused example showing how to package a realistic benchmark problem
