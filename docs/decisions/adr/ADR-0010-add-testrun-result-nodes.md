# ADR-0010 將 TestRun / Result 納入結果層

## Context

既有結果層只包含 `Build` 與 `Evidence`，仍不足以表達一次具體執行本身及其判定結果。若沒有 `TestRun` 與 `Result`，圖只能描述 build 與證據，無法清楚表示「哪一次執行產生哪個結果」。

## Decision

將 `TestRun (RUN-*)` 與 `Result (RES-*)` 納入結果層。

- `TS -> RUN` 使用 `executed_in_run`
- `RUN -> RES` 使用 `produced_result`
- `RES -> BUILD` 使用 `measured_on_build`
- `Build`、`TestRun`、`Result`、`Evidence` 共同構成結果層

## Consequences

- 優點：可以區分被測版本、實際執行、結果判定與證據。
- 優點：後續可擴充到 repeated runs、flaky cases、歷史趨勢。
- 風險：結果層關聯變多，matrix 與 fixture 也要同步增加。

## Supersedes

None
