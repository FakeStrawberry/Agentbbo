from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

import bbo.run as run_module
from bbo.algorithms import ALGORITHM_REGISTRY
from bbo.run import build_arg_parser, run_single_experiment


@pytest.mark.unit
def test_pfns4bo_is_registered_and_cli_visible() -> None:
    parser = build_arg_parser()
    algorithm_action = next(action for action in parser._actions if action.dest == "algorithm")

    assert "pfns4bo" in ALGORITHM_REGISTRY
    assert ALGORITHM_REGISTRY["pfns4bo"].family == "model_based"
    assert ALGORITHM_REGISTRY["pfns4bo"].numeric_only is False
    assert "pfns4bo" in algorithm_action.choices

    args = parser.parse_args(
        [
            "--algorithm",
            "pfns4bo",
            "--pfns-device",
            "cpu:0",
            "--pfns-pool-size",
            "128",
            "--pfns-model",
            "bnn",
        ]
    )
    assert args.algorithm == "pfns4bo"
    assert args.pfns_device == "cpu:0"
    assert args.pfns_pool_size == 128
    assert args.pfns_model == "bnn"


@pytest.mark.unit
def test_run_single_experiment_forwards_pfns_kwargs_without_runtime_dependency(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    surrogate_path = tmp_path / "surrogate.joblib"
    knobs_json_path = tmp_path / "knobs.json"
    captured: dict[str, object] = {}

    fake_task = SimpleNamespace(spec=SimpleNamespace(name="branin_demo"))

    def fake_create_task(task_name: str, **kwargs: object) -> object:
        captured["task_name"] = task_name
        captured["task_kwargs"] = kwargs
        return fake_task

    def fake_create_algorithm(name: str, **kwargs: object) -> object:
        captured["algorithm_name"] = name
        captured["algorithm_kwargs"] = kwargs
        return SimpleNamespace(name=name)

    class FakeLogger:
        def __init__(self, path: Path) -> None:
            self.path = path

        def load_records(self) -> list[dict[str, int]]:
            return [{"trial_id": 0}]

    class FakeExperimenter:
        def __init__(self, *, task: object, algorithm: object, logger_backend: object, config: object) -> None:
            captured["experiment_task"] = task
            captured["experiment_algorithm"] = algorithm
            captured["experiment_config"] = config
            self.logger_backend = logger_backend

        def run(self) -> object:
            return SimpleNamespace(
                task_name="branin_demo",
                algorithm_name="pfns4bo",
                seed=11,
                n_completed=1,
                total_eval_time=0.25,
                best_primary_objective=1.23,
                stop_reason="synthetic_stop",
                description_fingerprint="fake-fingerprint",
                incumbents=[],
                logger_summary={"records_written": 1},
            )

    monkeypatch.setattr(run_module, "create_task", fake_create_task)
    monkeypatch.setattr(run_module, "create_algorithm", fake_create_algorithm)
    monkeypatch.setattr(run_module, "JsonlMetricLogger", FakeLogger)
    monkeypatch.setattr(run_module, "Experimenter", FakeExperimenter)

    summary = run_single_experiment(
        task_name="branin_demo",
        algorithm_name="pfns4bo",
        seed=11,
        max_evaluations=5,
        results_root=tmp_path,
        noise_std=0.3,
        surrogate_path=surrogate_path,
        knobs_json_path=knobs_json_path,
        pfns_device="cpu:0",
        pfns_pool_size=64,
        pfns_model="bnn",
        generate_plots=False,
    )

    assert captured["task_name"] == "branin_demo"
    assert captured["task_kwargs"] == {
        "max_evaluations": 5,
        "seed": 11,
        "noise_std": 0.3,
        "surrogate_path": surrogate_path,
        "knobs_json_path": knobs_json_path,
    }
    assert captured["algorithm_name"] == "pfns4bo"
    assert captured["algorithm_kwargs"] == {
        "device": "cpu:0",
        "pool_size": 64,
        "model_name": "bnn",
    }
    assert summary["trial_count"] == 1
    assert "plot_paths" not in summary
    assert Path(summary["results_jsonl"]).with_name("summary.json").exists()
