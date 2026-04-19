# Constraints

- All 10 decision variables are continuous and bounded in `[0, 5]`.
- The task must use the staged tutorial dataset; no synthetic fallback data are allowed.
- The evaluator is a learned oracle, not a real experiment.
- The required smoke validation uses `random_search` with `--max-evaluations 3`.
- This task is for benchmark integration and interface checks, not for full paper reproduction.
