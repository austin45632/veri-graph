# ADR-0009 將 Build / Evidence 納入結果層

## Context

既有模型可以表達需求、測試設計與車載語意，但仍缺少「在哪個 build 上驗證」以及「留下了哪些證據」的正式節點。若沒有結果層，圖仍停在測試設計，而無法連到實際驗證結果。

## Decision

新增結果層，納入 `Build (BUILD-*)` 與 `Evidence (EVID-*)`。

- `TC -> BUILD` 使用 `executed_on_build`
- `TS -> EVID` 使用 `produces_evidence`
- `EVID -> BUILD` 使用 `collected_from_build`
- 結果層獨立於車載語意主軸，並由獨立 matrix 與腳本檢查

## Consequences

- 優點：可把測試案例與實際被測 build、執行證據連起來。
- 優點：後續可自然擴充到 `TestRun`、`Result`、更多證據型別。
- 風險：若結果層與主鏈都維護人工資料，會增加同步成本。

## Supersedes

None
