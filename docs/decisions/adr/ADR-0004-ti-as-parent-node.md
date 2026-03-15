# ADR-0004 將 TI 調整為 Codebeamer Test Case 母節點

## Context

先前將 `TI` 定義為 Codebeamer test case tracker 內的資料夾，但實際使用情境更接近一個能承載多個 testcase 的結構化母節點，例如 `TI_NormalSpeed -> TC_Speed_30kmh`。這種表達方式比資料夾更貼近測試設計樹，也更清楚表達一組 testcase 共享的設計意圖。

## Decision

`TI` 在 v1 改定義為 Codebeamer test case hierarchy 內的母節點。

- `TI` 不是獨立 tracker，也不進正式追溯鏈路。
- `TI` 至少需要 `Name` 與 `Description`。
- `TC-*` 應掛在某個 `TI` 母節點下，除非被明確標示為未分類。
- 正式追溯鏈路維持 `SPEC -> REQ -> TR -> TC -> TS`。

## Alternatives

1. 維持 `TI` 為資料夾：較簡單，但較難表達具有名稱與描述的設計母節點。
2. 將 `TI` 升格為 tracker：可追蹤性更高，但會增加正式鏈路與治理複雜度。

## Consequences

- 優點：更符合實際的 test design hierarchy。
- 優點：保留設計意圖聚合能力，但不增加正式追溯層級。
- 風險：若未明確約束，團隊可能把 `TI` 誤用為正式追溯節點。

## Supersedes

None
