# Evaluation

- Dataset: staged copy of `examples/OER/OER.csv` with `examples/OER/OER_clean.csv` kept as a clean reference
- Cleaning: tutorial-style duplicate removal, categorical normalization, numeric coercion, and outlier clipping
- Encoding: `pandas.get_dummies` with train/test column alignment
- Oracle: `RandomForestRegressor(n_estimators=200, max_depth=15, min_samples_split=5, min_samples_leaf=2, random_state=42, n_jobs=-1)`
- Primary objective: `overpotential_mv` with direction `minimize`
