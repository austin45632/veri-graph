# Automotive Semantics Matrix

此矩陣是車載語意主軸的審查視圖，用來表達 `Feature`、`VehicleState`、`Signal`、`FaultReaction`、`DiagnosticEvent`、`Variant`、`SafetyGoal` 與驗證主軸節點的關聯。

正式欄位：

| source_id | target_id | relation | status | last_reviewed_at |
|---|---|---|---|---|
| FEAT-001 | REQ-001 | belongs_to_feature | active | 2026-03-15 |
| FEAT-001 | TR-001 | belongs_to_feature | active | 2026-03-15 |
| FEAT-001 | TC-001 | belongs_to_feature | active | 2026-03-15 |
| VSTATE-001 | TI-001 | applies_in_state | active | 2026-03-15 |
| VSTATE-001 | TC-001 | applies_in_state | active | 2026-03-15 |
| SIG-001 | REQ-001 | depends_on_signal | active | 2026-03-15 |
| SIG-001 | TR-001 | depends_on_signal | active | 2026-03-15 |
| FAULT-001 | TI-001 | covers_fault_reaction | active | 2026-03-15 |
| FAULT-001 | TC-001 | covers_fault_reaction | active | 2026-03-15 |
| DIAG-001 | FAULT-001 | covers_diagnostic_event | active | 2026-03-15 |
| DIAG-001 | TC-001 | covers_diagnostic_event | active | 2026-03-15 |
| VAR-001 | REQ-001 | applies_to_variant | active | 2026-03-15 |
| VAR-001 | TC-001 | applies_to_variant | active | 2026-03-15 |
| SG-001 | REQ-001 | satisfies_safety_goal | active | 2026-03-15 |
