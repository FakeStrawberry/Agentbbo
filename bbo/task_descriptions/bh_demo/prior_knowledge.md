# Domain Prior Knowledge

The tutorial BH workflow first converts yield into regret and then filters the design space with a random-forest feature-importance heuristic.
The benchmark should preserve that ordering because the selected continuous coordinates define the optimizer-facing task.

Only the staged dataset and tutorial feature-selection recipe are benchmark priors.
