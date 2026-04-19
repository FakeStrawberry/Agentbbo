# Goal

Optimize the selected continuous features to minimize `regret`, where `regret = yield.max() - predicted_yield`.
Lower regret is better, so the optimizer is indirectly seeking higher predicted reaction yield.

Each evaluation returns `regret` and the reconstructed predicted yield.
