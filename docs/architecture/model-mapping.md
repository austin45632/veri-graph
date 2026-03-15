# veri-graph Model Mapping

## Purpose

定義 `veri-graph` 概念模型在 `Codebeamer`、`vTESTstudio` 與 repo 中的落地方式，避免 `TR`、`TI`、`TS` 在不同文件中被解讀成不同層級的主實體。

## Canonical Traceability Chain

正式知識圖鏈路為：

`SPEC -> REQ -> TR -> TI -> TC -> TS`

最低追溯合規鏈路為：

`REQ -> TR -> TC -> TS`

## Layers

- 驗證主軸：回答「需求怎麼被驗證」
- 車載語意主軸：回答「驗什麼車載語意」
- 結果層：回答「在哪個 build 上、哪次 run 中執行，留下了什麼 result / evidence」

其中：

- `TR` 為 Codebeamer 中的獨立 tracker，承接 requirement intent
- `TI` 為 knowledge graph 中的 scenario intent node，在 Codebeamer 中由 test case hierarchy 內的母節點承載
- 車載語意節點透過關聯接到 `REQ/TR/TI/TC`
- 結果層節點透過關聯接到 `TC/TS`

## Mapping Table

| Concept | Keep | Independent ID | System of Record | Form | Purpose |
|---|---|---|---|---|---|
| `SPEC` | Yes | Yes | Repo | Markdown document | 上位規格與背景脈絡 |
| `REQ` | Yes | Yes | Codebeamer | Requirement tracker item | 正式需求與追溯核心 |
| `TR` | Yes | Yes | Codebeamer | Test requirement tracker item | 驗證需求、覆蓋要求、acceptance logic；承接 requirement intent |
| `TI` | Yes | Yes in graph | Knowledge graph / Codebeamer hierarchy | Scenario intent node, carried by a parent node inside the test case hierarchy | 測試設計意圖與案例分組 |
| `TC` | Yes | Yes | Codebeamer | Test case tracker item | 測試管理與需求覆蓋單位 |
| `TS` | Yes | Yes | vTESTstudio | Executable test asset | 自動化與執行層實體 |
| `Feature` | Yes | Yes in graph | Knowledge graph | Domain node | 儀表功能語意 |
| `VehicleState` | Yes | Yes in graph | Knowledge graph | Domain node | 車輛操作狀態 |
| `Signal` | Yes | Yes in graph | Knowledge graph | Domain node | 車內通訊或輸入訊號 |
| `FaultReaction` | Yes | Yes in graph | Knowledge graph | Domain node | 故障後的顯示/警示/降級反應 |
| `DiagnosticEvent` | Yes | Yes in graph | Knowledge graph | Domain node | 診斷事件與故障監測語意 |
| `Variant` | Yes | Yes in graph | Knowledge graph | Domain node | 車型、配備或市場適用範圍 |
| `SafetyGoal` | Yes | Yes in graph | Knowledge graph | Domain node | 功能安全目標 |
| `Build` | Yes | Yes | Result layer | Result node | 被測軟體建置版本 |
| `TestRun` | Yes | Yes | Result layer | Result node | 一次具體執行批次 |
| `Result` | Yes | Yes | Result layer | Result node | 該次執行的結果判定 |
| `Evidence` | Yes | Yes | Result layer | Result node | 測試執行後留下的證據 |

## Design Rules

1. `TR` 承接 requirement intent，不再額外拆出獨立的 Requirement Intent 節點。
2. `TI` 承接 scenario intent，作為 `TR` 與 `TC` 之間的設計層節點。
3. 車載語意節點不取代驗證主鏈，而是以關聯方式補足背景語意。
4. 結果層不取代驗證主鏈，而是把 `TC/TS` 連到實際被測版本、執行批次、結果判定與證據。
5. `Codebeamer` 承載需求、驗證需求與測試管理語意。
6. `vTESTstudio` 承載可執行測試資產，不在 repo 中維護平行主腳本。

## Field Guidance

- `REQ` 必須能追溯到至少一個 `TR-*`。
- `TR` 至少需要來源需求、驗證規則與覆蓋狀態等欄位。
- `TI` 至少需要名稱與描述，用來表達 scenario intent。
- `TC` 至少需要 `Automation Status` 與 `vTESTstudio ID` 類欄位。
- `TS` 必須有穩定外部識別碼，能回指對應的 `TC`。
- `Feature`、`VehicleState`、`Signal`、`FaultReaction`、`DiagnosticEvent`、`Variant`、`SafetyGoal` 在 v1 先作為 graph 節點，不要求先映射到獨立工具主實體。
- `Build`、`TestRun`、`Result`、`Evidence` 在 v1 先作為 repo 中的結果層節點與審查視圖，不要求接實際 CI 或測試管理平台。

## Non-Goals For V1

- 不建立獨立的 Requirement Intent 節點。
- 不要求 `TI` 在 Codebeamer 中升格為獨立 tracker。
- 不把所有車載語意節點都映射到 Codebeamer tracker。
- 不把 repo 內 `TS-*` Markdown 文件當成正式腳本來源。
- 不在 v1 處理 Codebeamer 與 vTESTstudio 的雙向主寫入。
- 不在 v1 接入真實 test run database 或 artifact store。
