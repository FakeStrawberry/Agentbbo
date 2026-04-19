# 实验结果记录

更新时间：2026-04-19 AWST

## 0. 状态

- 总体状态：`completed`
- 当前阶段：scientific task family、数据校验、依赖安装、pytest 与五个 smoke 均已完成
- 执行 agent：OpenAI Codex (GPT-5)
- 最后更新：远程执行 agent

## 1. 远程 Benchmark 信息

| 字段 | 值 |
|---|---|
| remote host | `amax3` |
| remote repo path | `/home/trx/cm/agentic-bbo` |
| remote branch | `main` |
| remote Python version | `Python 3.11.5` |
| remote uv version | `uv 0.11.1` (from `/snap/astral-uv/current/meta/snap.yaml`) |
| agentic-bbo base commit/ref | `81431eca5a055c82eedaa738999e023a7c9ef7cc` |
| source repo ref | `9c1d7705d142259de167abedf95581d5fad5d7ce` (`/tmp/bo_tutorial_her_source`) |
| dataset cache root | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial` |
| artifact root | `/home/trx/cm/agentic-bbo/artifacts/bo_tutorial_all_smoke` |

## 2. 依赖安装记录

| 步骤 | 命令 | 状态 | 备注 |
|---|---|---|---|
| 安装 smoke 依赖 | `uv sync --extra dev --extra bo-tutorial` | completed | log: `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/uv_sync.log`；新增 `openpyxl==3.1.5`、`rdkit==2026.3.1`、`tqdm==4.67.3` |
| 导入检查 | `uv run python -c "import pandas, sklearn, scipy, openpyxl, tqdm; from rdkit import Chem; from rdkit.Chem import QED; print('bo-tutorial deps ok')"` | completed | log: `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/deps_import_check.log` |
| 完整依赖预留 | `uv sync --extra dev --extra bo-tutorial --extra bo-tutorial-full` | not_run | 本 workflow 不要求；`bo-tutorial-full` extra 已写入 `pyproject.toml` |

## 3. 数据集校验记录

### 3.1 总表

| 数据集 | Task | Source path | Local/cache path | sha256 | 行数/items | 列数 | 状态 |
|---|---|---|---|---|---:|---:|---|
| HER | `her_demo` | `examples/HER/HER_virtual_data.csv` | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/HER/HER_virtual_data.csv` | `1843a9247fb74a7df2b40088efb4e4d66f1fce5d788bfb10cf1423c31940bd5e` | 812 | 11 | completed |
| HEA | `hea_demo` | `examples/HEA/data/oracle_data.xlsx` | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/HEA/data/oracle_data.xlsx` | `68f219ea24dbe574285d79b78d064ea45f36e0d97537ab2dc8df3e36800e8a0c` | 286 | 6 | completed |
| OER | `oer_demo` | `examples/OER/OER.csv` | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/OER/OER.csv` | `46caa76f9f6a7856d417312353929dad45993167241a305aeaaf54fdde51fba5` | 1319 (cleaned) | 39 | completed |
| BH | `bh_demo` | `examples/BH/BH_dataset.csv` | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/BH/BH_dataset.csv` | `b991787d4e8ce14f51c8912b332d9f3e6271d6ba6afc7db3193822970e5ed42b` | 1728 | 21 (20 selected features + `yield`) | completed |
| Molecule/QED | `molecule_qed_demo` | `examples/Molecule/zinc.txt.gz` | `/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/Molecule/zinc.txt.gz` | `cf1f05bfed0c334a38aa26f27e4a5016dd09f5e225b86dcad490bb5f203fb099` | 249455 | N/A | completed |

### 3.2 HER 详情

- 列名：`AcidRed871_0gL`、`L-Cysteine-50gL`、`MethyleneB_250mgL`、`NaCl-3M`、`NaOH-1M`、`P10-MIX1`、`PVP-1wt`、`RhodamineB1_0gL`、`SDS-1wt`、`Sodiumsilicate-1wt`、`Target`
- 10 个 feature 列是否完整：completed
- 目标列：`Target`
- Target min/max/mean/std：`0.0 / 27.7041039 / 7.443407453194581 / 5.645122408551619`
- Regret 转换是否验证：completed；转换后 min/max/mean/std=`0.0 / 27.7041039 / 20.260696446805415 / 5.645122408551618`
- 文件大小：`83252` bytes
- 备注：默认点 `2.5 x 10` 的 oracle 预测 `regret=23.440962332260014`，`predicted_target=4.263141567739986`

### 3.3 HEA 详情

- 列名：`Co`、`Fe`、`Mn`、`V`、`Cu`、`target`
- 必需原始列 `Co`、`Fe`、`Mn`、`V`、`Cu`、`target` 是否存在：completed
- Target min/max/mean/std：`0.02343 / 297.0 / 4.762431365109905 / 25.77482935004557`
- `_phi_inv` transform 是否验证：completed；round-trip residual max=`1.6653345369377348e-16`
- 金属比例 `[0.05, 0.35]` 是否验证：completed；观察到 component bounds：`Co [0.06,0.35]`、`Fe [0.05,0.35]`、`Mn [0.05,0.35]`、`V [0.05,0.35]`、`Cu [0.05,0.35]`
- 组成比例和约等于 `1.0` 是否验证：completed
- 文件大小：`28308` bytes
- 备注：optimizer-facing default config=`x1=0.5,x2=0.3666666666666667,x3=0.5,x4=0.6035714285714286`

### 3.4 OER 详情

- 原始列名：39 列，核心列包括 `Metal_1`、`Metal_2`、`Metal_3`、`Metal_1_Proportion`、`Metal_2_Proportion`、`Metal_3_Proportion`、`Hydrothermal Temp degree`、`Hydrothermal Time min`、`Annealing Temp degree`、`Annealing Time min`、`Proton Concentration M`、`Catalyst_Loading mg cm -2`、`Overpotential mV @10 mA cm-2`
- 目标列 `Overpotential mV @10 mA cm-2` 是否存在：completed
- 清洗后 target min/max/mean/std：`197.0 / 513.0 / 304.6186504927976 / 63.671512841571484`
- categorical values 摘要：`Metal_1` 45 个 choice；`Metal_2` 50 个 choice；`Metal_3` 35 个 choice；均保留 `None`
- numeric bounds 摘要：`Metal_*_Proportion [0,100]`（其中 `Metal_3_Proportion` 实际上界 `33.33333333`）、`Hydrothermal Temp [-77,320]`、`Hydrothermal Time [0,2310]`、`Annealing Temp [25,1400]`、`Annealing Time [0,945]`、`Proton Concentration [0.1,3.7]`、`Catalyst_Loading [0,1.266]`
- 清洗摘要：完成 duplicate removal、categorical `None` 归一化、numeric coercion、IQR clipping、target 5%-95% 区间过滤
- 参考 clean 文件：`/home/trx/cm/agentic-bbo/artifacts/dataset_cache/bo_tutorial/examples/OER/OER_clean.csv`
- 文件大小：`225167` bytes
- 备注：one-hot 对齐逻辑已实现并用于预测

### 3.5 BH 详情

- 原始列名：原始文件 533 列；完整列名见 `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/dataset_validation.json`
- 目标列 `yield` 是否存在：completed
- 原始 yield min/max/mean/std：`0.0 / 100.0 / 19.374704861111113 / 24.59682883393795`
- regret yield min/max/mean/std：`0.0 / 100.0 / 80.62529513888889 / 24.59682883393795`
- feature selector 状态：completed；`feature_selector=random_forest`、`min_imp=0.01`、`max_cum_imp=0.8`、`max_n=20`
- 选中特征：`ligand_vib_1_reduced_mass_Boltz`、`temperature`、`ligand_vib_1_reduced_mass_MING`、`ligand_vib_7_reduced_mass_MAXG`、`ligand_vib_3_correlation_MING`、`concentration`、`ligand_vib_10_E-M_angle_MING`、`ligand_ES1_osc_strength_STDEV`、`ligand_vib_4_frequency_Boltz`、`solvent_molar_volume`、`ligand_atom4_NPA_Rydberg_STDEV`、`ligand_dipole_MAXG`、`ligand_vib_6_frequency_MEAN`、`ligand_c_min_NMR_anisotropy_MING`、`ligand_vib_6_IR_intensity_MEAN`、`solvent_c_max-1_NPA_Rydberg`、`ligand_vib_1_frc_const_MING`、`base_ES9_osc_strength`、`base_vib_3_correlation`、`solvent_electronegativity`
- 选中特征 bounds：已记录于 `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/dataset_validation.json`
- 文件大小：`11428004` bytes
- 备注：task-facing search space 为 20 维连续空间；`cost` 与 `new_index` 已剔除

### 3.6 Molecule/QED 详情

- archive member `zinc.txt` 是否存在：completed
- SMILES 数量：`249455`
- 首个合法 SMILES smoke check：completed；`CC(C)(C)c1ccc2occ(CC(=O)Nc3ccccc3F)c2c1`
- RDKit 导入状态：completed
- QED objective 状态：completed；default SMILES `qed=0.7319008436872338`，`qed_loss=0.26809915631276615`
- 文件大小：`3010609` bytes
- 备注：metadata 中记录 `archive_member=zinc.txt` 和原始 `qed`

## 4. 实现状态

| 组件 | 状态 | 文件/路径 | 备注 |
|---|---|---|---|
| scientific task package | completed | `bbo/tasks/scientific/` | 新增 HER/HEA/OER/BH/Molecule task family |
| data assets helper | completed | `bbo/tasks/scientific/data_assets.py` | source root 发现、cache staging、sha256/source ref 记录 |
| shared oracle helper | completed | `bbo/tasks/scientific/tabular_oracles.py` | RF 构造、one-hot 对齐、BH feature selection |
| HER task | completed | `bbo/tasks/scientific/her.py` | 10D continuous regret oracle |
| HEA task | completed | `bbo/tasks/scientific/hea.py` | `_phi_inv` / `_phi` transform + RF oracle |
| OER task | completed | `bbo/tasks/scientific/oer.py` | mixed categorical/numeric cleaning + aligned dummies |
| BH task | completed | `bbo/tasks/scientific/bh.py` | regret transform + selected-feature RF oracle |
| Molecule task | completed | `bbo/tasks/scientific/molecule.py` | real RDKit QED objective |
| scientific registry | completed | `bbo/tasks/scientific/registry.py` | 五个 task factory 注册 |
| task registry | completed | `bbo/tasks/registry.py` | 保留 synthetic 兼容并接入通用 `create_task()` |
| CLI factory | completed | `bbo/run.py` | 通用 task 创建 + numeric-only algorithm guard |
| dependency extras | completed | `pyproject.toml`, `uv.lock` | 新增 `bo-tutorial` 与 `bo-tutorial-full` |
| task descriptions | completed | `bbo/task_descriptions/<task>/` | 五个 scientific task 均补齐 `background/goal/constraints/prior_knowledge/evaluation/environment` |
| tests | completed | `tests/test_scientific_tasks.py` | 覆盖 registry、sanity、smoke；旧 `tests/test_her_task.py` 删除 |

## 5. 验证命令记录

| 命令 | 状态 | 输出/log path | 备注 |
|---|---|---|---|
| `uv sync --extra dev --extra bo-tutorial` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/uv_sync.log` | 依赖同步成功 |
| `uv run python -m compileall -q bbo tests` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/compileall.log` | 语法 smoke 通过 |
| `uv run pytest` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/pytest.log` | `18 passed in 20.05s` |
| `uv run python -m bbo.run --algorithm random_search --task her_demo --max-evaluations 3 --results-root artifacts/bo_tutorial_all_smoke` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/her_smoke.log` | 3/3 evaluations completed |
| `uv run python -m bbo.run --algorithm random_search --task hea_demo --max-evaluations 3 --results-root artifacts/bo_tutorial_all_smoke` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/hea_smoke.log` | 3/3 evaluations completed |
| `uv run python -m bbo.run --algorithm random_search --task oer_demo --max-evaluations 3 --results-root artifacts/bo_tutorial_all_smoke` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/oer_smoke.log` | 3/3 evaluations completed |
| `uv run python -m bbo.run --algorithm random_search --task bh_demo --max-evaluations 3 --results-root artifacts/bo_tutorial_all_smoke` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/bh_smoke.log` | 3/3 evaluations completed |
| `uv run python -m bbo.run --algorithm random_search --task molecule_qed_demo --max-evaluations 3 --results-root artifacts/bo_tutorial_all_smoke` | completed | `workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/molecule_qed_smoke.log` | 3/3 evaluations completed |

附加记录：

- 依赖导入检查 log：`workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/deps_import_check.log`
- 数据集校验明细：`workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/dataset_validation.json`
- smoke 产物汇总：`workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/logs/smoke_artifacts.json`

## 6. Smoke 产物

| Task | JSONL path | Summary path | Plot paths | best_primary_objective | 状态 |
|---|---|---|---|---:|---|
| `her_demo` | `artifacts/bo_tutorial_all_smoke/her_demo/random_search/seed_7/trials.jsonl` | `artifacts/bo_tutorial_all_smoke/her_demo/random_search/seed_7/summary.json` | `artifacts/bo_tutorial_all_smoke/her_demo/random_search/seed_7/plots/trace.png`, `artifacts/bo_tutorial_all_smoke/her_demo/random_search/seed_7/plots/distribution.png` | 25.76106351365 | completed |
| `hea_demo` | `artifacts/bo_tutorial_all_smoke/hea_demo/random_search/seed_7/trials.jsonl` | `artifacts/bo_tutorial_all_smoke/hea_demo/random_search/seed_7/summary.json` | `artifacts/bo_tutorial_all_smoke/hea_demo/random_search/seed_7/plots/trace.png`, `artifacts/bo_tutorial_all_smoke/hea_demo/random_search/seed_7/plots/distribution.png` | 295.54538020194826 | completed |
| `oer_demo` | `artifacts/bo_tutorial_all_smoke/oer_demo/random_search/seed_7/trials.jsonl` | `artifacts/bo_tutorial_all_smoke/oer_demo/random_search/seed_7/summary.json` | `artifacts/bo_tutorial_all_smoke/oer_demo/random_search/seed_7/plots/trace.png`, `artifacts/bo_tutorial_all_smoke/oer_demo/random_search/seed_7/plots/distribution.png` | 278.3114727567814 | completed |
| `bh_demo` | `artifacts/bo_tutorial_all_smoke/bh_demo/random_search/seed_7/trials.jsonl` | `artifacts/bo_tutorial_all_smoke/bh_demo/random_search/seed_7/summary.json` | `artifacts/bo_tutorial_all_smoke/bh_demo/random_search/seed_7/plots/trace.png`, `artifacts/bo_tutorial_all_smoke/bh_demo/random_search/seed_7/plots/distribution.png` | 78.26860000000002 | completed |
| `molecule_qed_demo` | `artifacts/bo_tutorial_all_smoke/molecule_qed_demo/random_search/seed_7/trials.jsonl` | `artifacts/bo_tutorial_all_smoke/molecule_qed_demo/random_search/seed_7/summary.json` | `artifacts/bo_tutorial_all_smoke/molecule_qed_demo/random_search/seed_7/plots/trace.png`, `artifacts/bo_tutorial_all_smoke/molecule_qed_demo/random_search/seed_7/plots/distribution.png` | 0.2496447901451042 | completed |

## 7. 修改文件列表

```text
bbo/run.py
bbo/tasks/__init__.py
bbo/tasks/registry.py
bbo/tasks/scientific/__init__.py
bbo/tasks/scientific/registry.py
bbo/tasks/scientific/data_assets.py
bbo/tasks/scientific/tabular_oracles.py
bbo/tasks/scientific/her.py
bbo/tasks/scientific/hea.py
bbo/tasks/scientific/oer.py
bbo/tasks/scientific/bh.py
bbo/tasks/scientific/molecule.py
bbo/task_descriptions/her_demo/background.md
bbo/task_descriptions/her_demo/goal.md
bbo/task_descriptions/her_demo/constraints.md
bbo/task_descriptions/her_demo/prior_knowledge.md
bbo/task_descriptions/her_demo/evaluation.md
bbo/task_descriptions/her_demo/environment.md
bbo/task_descriptions/hea_demo/background.md
bbo/task_descriptions/hea_demo/goal.md
bbo/task_descriptions/hea_demo/constraints.md
bbo/task_descriptions/hea_demo/prior_knowledge.md
bbo/task_descriptions/hea_demo/evaluation.md
bbo/task_descriptions/hea_demo/environment.md
bbo/task_descriptions/oer_demo/background.md
bbo/task_descriptions/oer_demo/goal.md
bbo/task_descriptions/oer_demo/constraints.md
bbo/task_descriptions/oer_demo/prior_knowledge.md
bbo/task_descriptions/oer_demo/evaluation.md
bbo/task_descriptions/oer_demo/environment.md
bbo/task_descriptions/bh_demo/background.md
bbo/task_descriptions/bh_demo/goal.md
bbo/task_descriptions/bh_demo/constraints.md
bbo/task_descriptions/bh_demo/prior_knowledge.md
bbo/task_descriptions/bh_demo/evaluation.md
bbo/task_descriptions/bh_demo/environment.md
bbo/task_descriptions/molecule_qed_demo/background.md
bbo/task_descriptions/molecule_qed_demo/goal.md
bbo/task_descriptions/molecule_qed_demo/constraints.md
bbo/task_descriptions/molecule_qed_demo/prior_knowledge.md
bbo/task_descriptions/molecule_qed_demo/evaluation.md
bbo/task_descriptions/molecule_qed_demo/environment.md
tests/test_scientific_tasks.py
tests/test_her_task.py (deleted)
pyproject.toml
uv.lock
workflow/bo_tutorial_all_datasets_agentic_bbo_remote_20260418_v1/exp_result.md
```

## 8. 当前 Blockers

- 无阻塞项。

## 9. 下一步

1. 如需复现实验 baseline，再执行 `uv sync --extra dev --extra bo-tutorial --extra bo-tutorial-full` 并在此基础上接入 HEBO / BO-LCB。
2. 若希望长期维护，建议把 `uv run pytest` 与一个 tutorial smoke 子集加入 CI。
