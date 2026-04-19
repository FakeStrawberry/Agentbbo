# Goal

Optimize ten continuous inputs to minimize `regret`, where `regret = Target.max() - predicted_Target`.
Lower regret is better, so the optimizer is indirectly seeking high predicted HER performance.

Each evaluation returns the primary objective `regret` plus metadata such as the reconstructed predicted target.
