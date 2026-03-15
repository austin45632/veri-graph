# ADR-0001 採用 Markdown-first + NetworkX 原型

## Context

需要快速建立可追溯驗證系統，同時保留稽核友善的文本證據。

## Decision

第一階段採用 Markdown-first 保存規格與追溯資訊；第二階段再將資料映射到 NetworkX 進行查詢與分析。

## Alternatives

1. 直接上圖資料庫：查詢強，但前期建置與治理成本高
2. 僅用試算表：上手快，但結構一致性與演進控制弱

## Consequences

- 優點：可快速啟動、便於人工審閱與版本控管
- 風險：跨文件一致性需靠規範與檢查腳本維持

## Supersedes

None
