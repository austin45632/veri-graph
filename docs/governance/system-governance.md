# System Governance

## Purpose

定義 repo、Codebeamer 與 vTESTstudio 在 `veri-graph` v1 中的責任邊界、更新時機與同步規則，避免雙主系統與追溯資訊漂移。

## System Ownership

| Artifact | System of record | Owner responsibility |
|---|---|---|
| `SPEC-*` | Repo | 維護上位規格、背景脈絡與設計假設 |
| `REQ-*` | Codebeamer | 維護正式需求內容、狀態與需求追溯 |
| `TR-*` | Codebeamer | 維護驗證需求、覆蓋狀態與 `REQ -> TR -> TI -> TC` 設計語意 |
| `TI-*` | Knowledge graph / Codebeamer hierarchy | 維護 scenario intent 與 testcase 分組 |
| `TC-*` | Codebeamer | 維護 testcase 定義、覆蓋狀態與需求對應 |
| `TS-*` | vTESTstudio | 維護可執行測試資產與自動化實作 |
| `FEAT-*` / `VSTATE-*` / `SIG-*` / `FAULT-*` / `DIAG-*` / `VAR-*` / `SG-*` | Knowledge graph | 維護車載語意主軸 |
| `BUILD-*` / `EVID-*` | Result layer | 維護被測 build 與執行證據索引 |
| `ADR-*` / `decision-log` | Repo | 維護架構、流程與模型決策 |
| `trace-matrix.md` | Repo | 維護匯出後的審查視圖，不作為主資料源 |
| `automotive-matrix.md` | Repo | 維護車載語意主軸審查視圖 |
| `result-matrix.md` | Repo | 維護結果層審查視圖 |
| `.github/workflows/verification-gates.yml` | Repo | 維護 CI 驗證入口 |

## Update Triggers

### Requirement change

當 `REQ-*` 在 Codebeamer 中新增、修改或狀態變更時，必須：

1. 更新對應 `TR-*` 的關聯或明確標記尚未覆蓋。
2. 確認相關 `TR-*` 的驗證規則與覆蓋狀態仍正確。
3. 視需要更新其 `Feature`、`Signal`、`SafetyGoal`、`Variant` 關聯。
4. 視需要更新 repo 中受影響的 `SPEC-*`、ADR 或 decision log。

### Test requirement change

當 `TR-*` 在 Codebeamer 中新增、修改或狀態變更時，必須：

1. 維持 `REQ -> TR` 關係可查詢。
2. 維持 `TR -> TI` 的 scenario intent 切分合理。
3. 維持 `TR -> TC` 關係可查詢，或明確標記尚未設計 testcase。
4. 視需要更新其 `Signal` 關聯與車載語意節點。
5. 視需要同步更新 traceability 審查視圖與 repo 樣例文件。

### Testcase change

當 `TC-*` 在 Codebeamer 中新增或修改時，必須：

1. 維持 `TR -> TC` 關係可查詢。
2. 維持所屬 `TI` 母節點與其描述、`Automation Status`、`vTESTstudio ID` 類欄位。
3. 確認 `TI` 命名符合 `TI_<Domain>_<Intent>` 規則。
4. 若 testcase 已自動化，確認對應 `TS-*` 已存在且可回指。
5. 視需要更新其 `VehicleState`、`Signal`、`FaultReaction`、`DiagnosticEvent` 或 `Variant` 關聯。
6. 若 testcase 已執行，視需要更新 `BUILD-*`、`RUN-*`、`RES-*`、`EVID-*` 關聯。

### Result change

當 build、run、result 或執行證據更新時，必須：

1. 維持 `TC -> BUILD` 關係可查詢。
2. 維持 `TS -> RUN` 關係可查詢。
3. 維持 `RUN -> RES` 關係可查詢。
4. 維持 `TS -> EVID` 與 `EVID -> BUILD` 關係可查詢。
5. 視需要同步更新 `result-matrix.md`。

### Model or process change

當追溯模型、欄位語意、工具邊界或治理規則變更時，必須：

1. 建立或更新 ADR。
2. 在 `docs/decisions/decision-log.md` 補一筆對應紀錄。
3. 同步修正 `model-mapping.md`、`README.md`、CI workflow 與受影響示例文件。

## Operating Rules

1. 不允許 repo、Codebeamer 與 vTESTstudio 同時作為同一類資料的主寫入來源。
2. `trace-matrix.md` 僅作為審查視圖或匯出結果，不作為正式追溯主檔。
3. `automotive-matrix.md` 僅作為車載語意主軸審查視圖。
4. `result-matrix.md` 僅作為結果層審查視圖。
5. `TR-*` 是 requirement intent 的承載者，`TI-*` 則是 scenario intent 的承載者。
6. `FEAT-*`、`VSTATE-*`、`SIG-*`、`FAULT-*`、`DIAG-*`、`VAR-*`、`SG-*` 屬於車載語意主軸，不直接取代驗證主鏈。
7. `BUILD-*`、`RUN-*`、`RES-*`、`EVID-*` 屬於結果層，不直接取代驗證主鏈或車載語意主軸。
8. `REQ-*` 的最低合規條件是至少關聯一個 `TR-*`。
9. `TR-*` 的最低合規條件是至少關聯一個 `TC-*`。
10. `TI-*` 屬於設計結構完整性，不作為最低追溯合規 gate。
11. `TC-*` 應關聯一個 `TS-*`，或被明確標示為尚未自動化。
12. CI workflow 必須至少執行 unittest 與 `check_all.py`。

## Review Checklist

- `REQ -> TR` 是否完整
- `TR -> TI` 是否符合 scenario intent 切分
- `TI -> TC` 是否完整且命名清楚
- `TC -> TS` 是否完整或已標示例外
- `Feature`、`VehicleState`、`Signal`、`FaultReaction`、`DiagnosticEvent`、`Variant`、`SafetyGoal` 關聯是否正確
- `TC -> BUILD`、`TS -> RUN`、`RUN -> RES`、`TS -> EVID`、`EVID -> BUILD` 是否正確
- `trace-matrix.md`、`automotive-matrix.md`、`result-matrix.md` 是否反映目前審查視圖
- `.github/workflows/verification-gates.yml` 是否仍執行 unittest 與 `check_all.py`
- 模型或流程變更是否同步更新 ADR 與 decision log

## Verification Entry Points

- `python scripts\check_traceability.py`
  用於最低追溯合規 gate，檢查 `REQ -> TR -> TC -> TS`
- `python scripts\check_automotive_semantics.py`
  用於車載語意完整性檢查，檢查 `automotive-matrix.md` 是否覆蓋所有 `FEAT/VSTATE/SIG/FAULT/DIAG/VAR/SG`
- `python scripts\check_result_evidence.py`
  用於結果層完整性檢查，檢查 `result-matrix.md` 是否覆蓋所有 `BUILD/RUN/RES/EVID`
- `python scripts\check_all.py`
  用於依序執行三層檢查並彙總結果
- `python -m unittest discover -s tests -p 'test_*.py' -v`
  用於文件結構、樣例、fixture 與腳本行為的回歸驗證
- GitHub Actions `verification-gates`
  用於在 push / pull request 時自動執行 unittest 與 `check_all.py`


## Issue Triage Labels

- Type labels: `bug`, `governance`, `knowledge-graph`
- Axis labels: `verification-axis`, `automotive-semantics`, `result-layer`
- Tooling labels: `ci`, `codebeamer`, `vteststudio`

Triage ???

1. ?? issue ???? 1 ? type label?
2. ???????????????? 1 ? axis label?
3. ???????? GitHub ??????? 1 ? tooling/process label?
4. `knowledge_graph_change` ? issue ????? `knowledge-graph`?
