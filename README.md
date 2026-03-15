# veri-graph

veri-graph 是一個以文本為核心的驗證系統原型，目標是建立可稽核且可回歸分析的追溯鏈路：

Spec -> Requirement -> Test Requirement -> Test Intent -> Testcase -> Test Script

## 目標

- 讓每個規格化需求都可追溯到測試需求與測試案例
- 用 ADR 與決策日誌紀錄設計迭代
- 以 Markdown-first 結構快速原型化，再銜接 NetworkX
- 與 Codebeamer / vTESTstudio 的正式追溯模型對齊
- 擴充為適用車載儀表系統的 knowledge graph

## 專案結構

- `docs/architecture/model-mapping.md`: veri-graph 與 Codebeamer / vTESTstudio 對應規則
- `docs/automotive/`: 車載語意主軸樣例節點（Feature / VehicleState / Signal / FaultReaction / DiagnosticEvent / Variant / SafetyGoal）
- `docs/results/`: 結果層樣例節點（Build / TestRun / Result / Evidence）
- `docs/specs/`: 規格文件（版本化）
- `docs/requirements/`: 需求文件（REQ-###）
- `docs/test-requirements/`: 驗證需求樣例與歷史文件
- `docs/test-intents/`: 測試設計意圖母節點樣例與歷史文件
- `docs/testcases/`: 測試案例（TC-###）
- `docs/test-scripts/`: 測試資產索引與整合說明
- `docs/traceability/trace-matrix.md`: 追溯矩陣
- `docs/decisions/adr/`: ADR 文件
- `docs/decisions/decision-log.md`: 決策時間線
- `prototype/`: NetworkX 原型規格與查詢需求
- `.github/workflows/verification-gates.yml`: CI 驗證入口

## ID 命名規範

- `SPEC-###`, `REQ-###`, `TR-###`, `TI-###`, `TC-###`, `TS-###`
- `FEAT-###`, `VSTATE-###`, `SIG-###`, `FAULT-###`, `DIAG-###`, `VAR-###`, `SG-###`
- `BUILD-###`, `RUN-###`, `RES-###`, `EVID-###`

## 稽核規則（MVP）

- 每個 normative `REQ-*` 至少連到一個 `TR-*`
- 每個 `TR-*` 至少連到一個 `TC-*`
- 每個 `TC-*` 應能對應到一個 `TS-*` 或被標示為尚未自動化
- 無對應者標記為 `non-compliant`

## 模型說明

- 正式知識圖鏈路：`SPEC -> REQ -> TR -> TI -> TC -> TS`
- 最低追溯合規鏈路：`REQ -> TR -> TC -> TS`
- 驗證主軸：描述需求怎麼被驗證
- 車載語意主軸：描述 feature、vehicle state、signal、fault reaction、diagnostic event、variant、safety goal 與需求/測試的關係
- 結果層：描述 testcase/script 在什麼 build 上、哪次 run 中執行，並留下哪些 result / evidence
- `TR` 為 Codebeamer 中的獨立 tracker，承接 requirement intent
- `TI` 為 knowledge graph 中的 scenario intent node，在 Codebeamer 由 test case hierarchy 母節點承載
- `TS` 對應 vTESTstudio 中的可執行測試資產
- 第一組車載樣例位於 `docs/automotive/`，結果層樣例位於 `docs/results/`

詳細定義見 `docs/architecture/model-mapping.md`。

## 驗證

```powershell
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts\check_traceability.py
python scripts\check_automotive_semantics.py
python scripts\check_result_evidence.py
python scripts\check_all.py
```

- `check_traceability.py`: 檢查最低追溯合規鏈路 `REQ -> TR -> TC -> TS`
- `check_automotive_semantics.py`: 檢查車載語意主軸節點是否被 `automotive-matrix.md` 正確覆蓋
- `check_result_evidence.py`: 檢查結果層 `Build / TestRun / Result / Evidence` 是否被 `result-matrix.md` 正確覆蓋
- `check_all.py`: 依序執行三層檢查並彙總結果
- GitHub Actions：push / pull request 時執行 unittest 與 `check_all.py`
