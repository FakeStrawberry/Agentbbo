# Evaluation

- Dataset: staged copy of `examples/BH/BH_dataset.csv`
- Preprocessing: convert `yield` to `yield.max() - yield`
- Feature selection: random-forest importance with `max_n=20`, `max_cum_imp=0.8`, `min_imp=0.01`
- Oracle: `RandomForestRegressor(n_estimators=100, random_state=<seed>)`
- Primary objective: `regret` with direction `minimize`
