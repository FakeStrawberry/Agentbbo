# Goal

Optimize four continuous design variables `x1..x4` to minimize `regret`, where `regret = target.max() - predicted_target`.
The optimizer never proposes the five metal fractions directly; the task maps `x1..x4` into feasible `Co/Fe/Mn/V/Cu` compositions internally.

Each evaluation returns `regret` and the decoded alloy composition.
