# ADR-0005 將 TI 納入 Knowledge Graph 正式節點

## Context

目前 `TI` 已在工具實作上被定義為 Codebeamer test case hierarchy 的母節點，但在 graph schema 中仍只是 supporting structure。這會造成語意不對稱：架構上 `TI` 已承接 scenario intent，圖上卻無法成為正式查詢節點。

## Decision

將 `TI-*` 納入 knowledge graph 的正式 node type。

- `TR` 承接 requirement intent。
- `TI` 承接 scenario intent。
- 正式知識圖鏈路改為 `SPEC -> REQ -> TR -> TI -> TC -> TS`。
- 最低追溯合規鏈路仍維持 `REQ -> TR -> TC -> TS`。
- Codebeamer 中的 `TI` 仍由 hierarchy parent node 承載，不升格為獨立 tracker。

## Alternatives

1. 維持 `TI` 為 supporting structure：工具實作簡單，但 graph 查詢無法正確表達 scenario intent。
2. 將 `TI` 升格為 Codebeamer tracker：語意一致性更高，但導入與治理成本過大。

## Consequences

- 優點：知識圖能直接查詢 scenario intent 與其覆蓋範圍。
- 優點：`Requirement Intent` 與 `Scenario Intent` 的分工更清楚，分別由 `TR` 與 `TI` 承接。
- 風險：工具實作型態與 graph node 型態不再完全同構，需要在文件中持續說明映射關係。

## Supersedes

None
