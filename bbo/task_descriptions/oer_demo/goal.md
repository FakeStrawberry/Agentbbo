# Goal

Optimize the mixed search space to minimize predicted `overpotential_mv`.
Lower predicted overpotential is better, so the benchmark objective is directly minimized rather than converted into regret.

Each evaluation returns the primary objective `overpotential_mv` plus the sampled categorical metal choices.
