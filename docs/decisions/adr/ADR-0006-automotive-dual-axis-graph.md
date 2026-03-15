# ADR-0006 車載儀表系統採用雙主軸 Knowledge Graph

## Context

既有圖主要描述驗證追溯鏈路，但對車載儀表系統而言，還需要描述 feature、vehicle state、signal、fault reaction 與 safety goal 等車載語意。如果把這些語意全部塞進 `REQ -> TR -> TI -> TC -> TS` 單一路徑，圖會變得難以維護且查詢語意混亂。

## Decision

採用雙主軸 knowledge graph：

- 驗證主軸：`SPEC -> REQ -> TR -> TI -> TC -> TS`
- 車載語意主軸：`Feature / VehicleState / Signal / FaultReaction / SafetyGoal -> REQ / TR / TI / TC`

其中：
- 驗證主軸回答「需求怎麼被驗證」
- 車載語意主軸回答「驗什麼車載語意」
- 最低追溯合規 gate 仍維持在 `REQ -> TR -> TC -> TS`

## Alternatives

1. 將所有車載語意硬塞進驗證主鏈：查詢困難且節點責任混亂。
2. 完全不加入車載語意節點：無法支援儀表系統的 signal / vehicle state / safety query。

## Consequences

- 優點：保留驗證主鏈的穩定性，同時能支援車載語意查詢。
- 優點：可逐步增加車載節點，不必一次重構整個追溯模型。
- 風險：圖的層次變多，需要更清楚的節點與邊定義。

## Supersedes

None
