# Codebeamer Configuration

## Purpose

定義 `veri-graph` 在 Codebeamer 中的最小可落地配置，涵蓋 `REQ`、`TR`、`TC` 三種 tracker 與 `TI` 母節點規則，讓 repo 內模型能對應到實際工具設定。

## Tracker Layout

| Concept | Codebeamer object | Key fields | Required links |
|---|---|---|---|
| `REQ-*` | Requirement tracker item | ID, Title, Status, Owner, Priority | At least one `TR-*` via `validated_by` |
| `TR-*` | Test requirement tracker item | ID, Title, Status, Owner, Verification Rule, Coverage Status, Source Requirement | One source `REQ-*`, optional one or more `TI-*`, at least one `TC-*` via `verified_by` |
| `TI-*` | Scenario intent node carried by the test case hierarchy | Name, Description | Groups related `TC-*` items under one `TR-*` |
| `TC-*` | Test case tracker item | ID, Title, Status, Owner, Automation Status, vTESTstudio ID | One source `TR-*`, one source `TI-*`, optional one or more `TS-*` |

## Field Guidance

### Requirement tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Priority`

Required relation:
- `validated_by` to at least one `TR-*`

### Test requirement tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Verification Rule`
- `Coverage Status`
- `Source Requirement`

Recommended status values:
- `draft`
- `active`
- `reviewed`
- `obsolete`

Required relations:
- exactly one source `REQ-*`
- at least one `TC-*` via `verified_by`

### Test intent node

Minimum fields:
- `Name`
- `Description`

Semantics:
- graph 中的 `TI-*` 是正式 scenario intent node
- Codebeamer 中由 test case hierarchy 的母節點承載
- 不需要獨立 workflow

### Test case tracker

Required fields:
- `ID`
- `Title`
- `Status`
- `Owner`
- `Automation Status`
- `vTESTstudio ID`

Recommended `Automation Status` values:
- `not_automated`
- `planned`
- `automated`
- `retired`

Required relations:
- exactly one source `TR-*`
- exactly one source `TI-*` in the graph model
- zero or more linked `TS-*` in vTESTstudio

## TI Parent Node Rules

- `TI` 不建立獨立 tracker。
- 每個 `TI` 以 test case hierarchy 內母節點表達，例如 `TI_Speed_Normal`。
- 每個 `TI` 母節點至少需要 `Name` 與 `Description`。
- `TC-*` 必須掛在一個 `TI` 母節點下，除非明確標示為暫時未分類。
- `TI` 母節點名稱應能表達測試設計意圖，而不是只用模糊分類名稱。

## TI Naming Convention

- 格式：`TI_<Domain>_<Intent>`
- `Domain` 使用功能或訊號域，例如 `Speed`、`Brake`、`CAN`
- `Intent` 使用測試意圖，例如 `Normal`、`Boundary`、`Timeout`
- 不在 `TI` 名稱中放數值、步驟細節或 testcase 編號
- 同一個 `TR-*` 底下的 `TI` 名稱必須唯一

## Traceability Rules

1. 每個 `REQ-*` 至少一個 `TR-*`。
2. 每個 `TR-*` 至少一個 `TC-*`。
3. 若採用 scenario 分群，`TR-*` 應至少有一個 `TI-*`。
4. 每個 `TC-*` 應有 `Automation Status`。
5. `Automation Status=automated` 的 `TC-*` 必須有 `vTESTstudio ID`。
6. repo 中的 `trace-matrix.md` 只反映 `REQ -> TR -> TC -> TS` 審查視圖，不作為主資料源。
