# Domain Prior Knowledge

The raw alloy representation uses five components: `Co`, `Fe`, `Mn`, `V`, and `Cu`.
The tutorial constrains every component to the same feasible interval and uses an invertible transform between the optimizer-facing design variables and the physical composition simplex.

Only these transform rules and the staged dataset are benchmark priors.
The task does not assume external metallurgy knowledge beyond the tutorial materials.
