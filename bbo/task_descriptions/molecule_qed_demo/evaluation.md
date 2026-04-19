# Evaluation

- Dataset: staged copy of `examples/Molecule/zinc.txt.gz`
- Archive member: `zinc.txt`
- Objective: parse each SMILES with `rdkit.Chem.MolFromSmiles`, compute `rdkit.Chem.QED.qed`, then report `qed_loss = 1.0 - qed`
- Invalid molecules receive `qed = 0.0`
- Primary objective: `qed_loss` with direction `minimize`
