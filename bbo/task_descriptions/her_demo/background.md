# Background

`her_demo` models catalyst-composition optimization for photocatalytic hydrogen evolution reaction (HER).
It uses the tutorial repository file `examples/HER/HER_virtual_data.csv` from *Efficient and Principled Scientific Discovery through Bayesian Optimization: A Tutorial*.

This benchmark is a smoke-level proxy, not a wet-lab workflow.
The evaluator fits a reproducible random-forest oracle on the staged tutorial dataset and exposes it through the standard benchmark interface.
