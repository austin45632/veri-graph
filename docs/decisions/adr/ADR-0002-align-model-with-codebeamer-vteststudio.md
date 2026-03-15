# ADR-0002 對齊 Codebeamer 與 vTESTstudio 的追溯模型

## Context

`veri-graph` 原先以 `SPEC -> REQ -> TR -> TI -> TC -> TS` 作為文本原型鏈路，但在導入 `Codebeamer` 與 `vTESTstudio` 的實際使用情境後，`TR` 與 `TI` 作為獨立主實體的價值不足，且會增加跨系統同步成本。

## Decision

v1 正式追溯鏈路收斂為 `SPEC -> REQ -> TC -> TS`。

- `REQ` 與 `TC` 以 Codebeamer 為主資料源。
- `TS` 以 vTESTstudio 為主資料源。
- `TR` 降為 `REQ` 層級的 verification metadata。
- `TI` 降為 `TC` 層級的 design metadata。
- repo 中的 `trace-matrix.md` 僅作為審查視圖，不作為正式主資料源。

## Alternatives

1. 保留 `TR` 與 `TI` 為獨立 tracker：可見性高，但同步與治理成本高。
2. 全部收斂到 repo：彈性高，但與 Codebeamer / vTESTstudio 的正式流程脫節。

## Consequences

- 優點：主資料源清楚，追溯與自動化角色分工明確。
- 優點：降低雙主系統與中介實體維護成本。
- 風險：`TR` 與 `TI` 不再是獨立查詢節點，需要透過欄位或報表呈現。

## Supersedes

None

## Superseded By

ADR-0003
