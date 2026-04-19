# Evaluation

- Dataset: staged copy of `examples/HEA/data/oracle_data.xlsx`
- Raw oracle inputs: `Co`, `Fe`, `Mn`, `V`, `Cu`
- Oracle: `RandomForestRegressor(n_estimators=100, random_state=<seed>)`
- Query path: decode `x1..x4` with the tutorial `_phi_inv` logic, predict `target`, then report `regret = target.max() - predicted_target`
- Required smoke budget: 3 `random_search` evaluations
