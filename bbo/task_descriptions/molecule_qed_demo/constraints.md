# Constraints

- The exposed search space contains one categorical parameter: `SMILES`.
- Candidate molecules must come from the staged `zinc.txt` archive member.
- Invalid SMILES receive raw `qed = 0.0`, which maps to `qed_loss = 1.0`.
- The required smoke validation uses `random_search` with `--max-evaluations 3`.
- RDKit is mandatory; no fake objective may replace QED.
