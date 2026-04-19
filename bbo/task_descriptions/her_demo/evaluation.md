# Evaluation

- Dataset: staged copy of `examples/HER/HER_virtual_data.csv`
- Preprocessing: convert `Target` into `Target.max() - Target`
- Oracle: `RandomForestRegressor(n_estimators=100, random_state=<seed>)`
- Primary objective: `regret` with direction `minimize`
- Required smoke budget: 3 `random_search` evaluations
- Standard outputs: append-only `trials.jsonl`, `summary.json`, trace plot, and distribution plot
