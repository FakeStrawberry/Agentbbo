# Constraints

- Three parameters are categorical metal identities derived from the cleaned tutorial data.
- Three metal-proportion parameters are continuous in `[0, 100]`.
- Hydrothermal and annealing temperature/time parameters are integer-valued and bounded by cleaned-data minima and maxima.
- The required smoke validation uses `random_search` with `--max-evaluations 3`.
- One-hot alignment must follow the tutorial cleaning logic; no silent fallback encodings are allowed.
