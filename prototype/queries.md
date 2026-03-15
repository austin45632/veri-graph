# Query Requirements (Prototype)

1. 找出所有沒有 `TR-*` 的 `REQ-*`（non-compliant）
2. 找出所有沒有 `TC-*` 的 `TR-*`（non-compliant）
3. 找出採用 scenario 分群但沒有 `TI-*` 的 `TR-*`
4. 找出所有沒有 `TC-*` 的 `TI-*`
5. 找出沒有對應 `TS-*` 的 `TC-*`，或標示為未自動化的案例
6. 找出 orphan testcase（無 test requirement 或 test intent 關聯）
7. 找出 stale links（`last_reviewed_at` 超過門檻）
8. 依 scenario intent 查詢其覆蓋到的 `TC-*` 與 `TS-*`
9. 查詢某個 `Feature-*` 關聯到的 `REQ/TR/TC`
10. 查詢某個 `VehicleState-*` 下有哪些 `TI/TC`
11. 查詢某個 `Signal-*` 影響哪些 `REQ/TR`
12. 查詢某個 `FaultReaction-*` 對應哪些 `TI/TC`
13. 查詢某個 `DiagnosticEvent-*` 對應哪些 `FAULT/TC`
14. 查詢某個 `Variant-*` 對應哪些 `REQ/TC`
15. 查詢某個 `SafetyGoal-*` 下哪些 `REQ-*` 尚未覆蓋
16. 查詢某個 `Build-*` 上執行了哪些 `TC-*`
17. 查詢某個 `Run-*` 產生了哪些 `Result-*`
18. 查詢某個 `Evidence-*` 由哪些 `TS-*` 產生
19. 依變更影響列出最小回歸測試集（planned）
