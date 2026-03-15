# ADR-0003 將 TR 升格為 Codebeamer Tracker

## Context

`ADR-0002` 將 `TR` 降為 metadata，以降低模型複雜度，但這會削弱驗證需求的獨立追蹤能力。若 `TR` 需要獨立負責驗證範圍、覆蓋狀態與審查節點，則僅靠 `REQ` 欄位已不足。

## Decision

v1 正式追溯鏈路改為 `SPEC -> REQ -> TR -> TC -> TS`。

- `TR` 升格為 Codebeamer 中的獨立 tracker。
- `REQ` 以 `validated_by` 關係連到 `TR`。
- `TR` 以 `verified_by` 關係連到 `TC`。
- `TI` 不升格為 tracker，而是改作 Codebeamer test case tracker 內的資料夾。
- `TS` 仍以 vTESTstudio 為主資料源。
- repo 中的 `trace-matrix.md` 仍僅作為審查視圖。

## Alternatives

1. 維持 `TR` 為 metadata：模型較輕，但無法獨立管理驗證需求。
2. 讓 `REQ` 直接連 `TC` 並同時保留 `TR`：彈性較高，但規則與責任邊界更複雜。

## Consequences

- 優點：`TR` 可獨立追蹤狀態、覆蓋與責任。
- 優點：需求、驗證需求與 testcase 的治理分工更清楚。
- 風險：模型層級增加，需要維護 `REQ -> TR -> TC` 的完整性。

## Supersedes

ADR-0002
