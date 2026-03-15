# ADR-0007 將 DiagnosticEvent 納入車載語意主軸

## Context

既有車載語意主軸已包含 `Feature`、`VehicleState`、`Signal`、`FaultReaction`、`SafetyGoal`，但對儀表系統常見的故障監測與診斷事件仍缺少明確節點。若只用 `FaultReaction` 表示，會混淆「故障被偵測到」與「系統對故障的反應」。

## Decision

將 `DiagnosticEvent (DIAG-*)` 納入車載語意主軸，作為獨立 graph node。

- `DiagnosticEvent -> FAULT` 或 `DiagnosticEvent -> TC` 使用 `covers_diagnostic_event`
- `DiagnosticEvent` 用於表達故障監測與診斷語意
- `FaultReaction` 繼續表達故障後的顯示/告警/降級反應

## Consequences

- 優點：可以區分診斷事件與故障反應，不把兩者混成同一節點。
- 優點：後續可自然擴充到 DTC、監測條件與診斷證據。
- 風險：車載語意主軸的節點種類增加，需要同步維護 matrix 與樣例。

## Supersedes

None
