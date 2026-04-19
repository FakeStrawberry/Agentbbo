# Goal

Optimize the categorical `SMILES` parameter to minimize `qed_loss`, where `qed_loss = 1.0 - qed`.
Higher QED therefore corresponds to lower loss and better performance.

Each evaluation also records the raw `qed` value in the trial metrics and metadata.
