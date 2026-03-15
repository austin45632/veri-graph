# Decision Log

| date | decision_id | summary | impacted_ids |
|---|---|---|---|
| 2026-03-15 | ADR-0001 | 採用 Markdown-first + NetworkX 原型策略 | SPEC-001, REQ-001, TR-001, TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0002 | 正式追溯鏈路收斂為 SPEC-REQ-TC-TS，並對齊 Codebeamer 與 vTESTstudio | SPEC-001, REQ-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0003 | 將 TR 升格為 Codebeamer tracker，正式追溯鏈路改為 SPEC-REQ-TR-TC-TS | SPEC-001, REQ-001, TR-001, TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0004 | 將 TI 調整為 Codebeamer test case hierarchy 的母節點，而非資料夾 | TI-001, TC-001 |
| 2026-03-15 | ADR-0005 | 將 TI 納入 knowledge graph 正式節點，形成 SPEC-REQ-TR-TI-TC-TS 結構 | TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0006 | 車載儀表系統採用雙主軸 knowledge graph，新增車載語意節點族群 | FEAT-001, VSTATE-001, SIG-001, FAULT-001, SG-001 |
| 2026-03-15 | ADR-0007 | 將 DiagnosticEvent 納入車載語意主軸，區分診斷事件與故障反應 | DIAG-001, FAULT-001, TC-001 |
| 2026-03-15 | ADR-0008 | 將 Variant 納入車載語意主軸，表達車型與配備適用範圍 | VAR-001, REQ-001, TC-001 |
| 2026-03-15 | ADR-0009 | 將 Build / Evidence 納入結果層，連接測試到實際驗證結果 | BUILD-001, EVID-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0010 | 將 TestRun / Result 納入結果層，區分執行批次與結果判定 | RUN-001, RES-001, BUILD-001, TS-001 |
| 2026-03-15 | ADR-0011 | ????????? PR-based GitHub ????? verify ? protected branch????? approval | .github/workflows/verification-gates.yml, .github/CODEOWNERS, .github/PULL_REQUEST_TEMPLATE.md |
