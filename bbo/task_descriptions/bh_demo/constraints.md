# Constraints

- The raw target column is `yield`, but the benchmark objective is the regret-transformed version.
- Columns such as `cost` and `new_index` are not valid optimization parameters.
- Feature selection must use `random_forest`, `min_imp=0.01`, `max_cum_imp=0.8`, and `max_n=20`.
- The required smoke validation uses `random_search` with `--max-evaluations 3`.
- No fake selected-feature set is allowed.
