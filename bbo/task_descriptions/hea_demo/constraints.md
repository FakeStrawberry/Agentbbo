# Constraints

- The exposed search space is four continuous variables in `[0, 1]`.
- Internal decoding must keep each metal fraction in `[0.05, 0.35]`.
- The five decoded fractions must sum to approximately `1.0`.
- The required smoke validation uses `random_search` with `--max-evaluations 3`.
- No fake simplex mapping or fake oracle is allowed.
