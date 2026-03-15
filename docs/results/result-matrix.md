# Result Matrix

此矩陣是結果層的審查視圖，用來表達 `Build`、`TestRun`、`Result`、`Evidence` 與驗證主軸節點的關聯。

| source_id | target_id | relation | status | last_reviewed_at |
|---|---|---|---|---|
| TC-001 | BUILD-001 | executed_on_build | active | 2026-03-15 |
| TS-001 | RUN-001 | executed_in_run | active | 2026-03-15 |
| RUN-001 | RES-001 | produced_result | active | 2026-03-15 |
| RES-001 | BUILD-001 | measured_on_build | active | 2026-03-15 |
| TS-001 | EVID-001 | produces_evidence | active | 2026-03-15 |
| EVID-001 | BUILD-001 | collected_from_build | active | 2026-03-15 |
