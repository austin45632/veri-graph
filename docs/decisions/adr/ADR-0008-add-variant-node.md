# ADR-0008 將 Variant 納入車載語意主軸

## Context

儀表系統通常存在不同車型、配備、地區或功能組合的差異。若沒有獨立的 Variant 節點，需求與測試的適用範圍會分散在敘述文字中，難以查詢與維護。

## Decision

將 `Variant (VAR-*)` 納入車載語意主軸，作為獨立 graph node。

- `Variant -> REQ` 或 `Variant -> TC` 使用 `applies_to_variant`
- `Variant` 用於表達車型、配備或市場適用範圍
- 不在 v1 細分成 market、trim、coding 等更細類型

## Consequences

- 優點：可明確回答需求與測試的適用變體範圍。
- 優點：後續可自然擴充到市場別或功能開關。
- 風險：若變體建模過細，矩陣維護成本會上升。

## Supersedes

None
