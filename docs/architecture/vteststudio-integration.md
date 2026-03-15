# vTESTstudio Integration

## Purpose

定義 `veri-graph` 與 `vTESTstudio` 之間對 `TS-*` 的最小整合規則，確保 `TC -> TS` 追溯可穩定維持。

## TS Identity Rules

- repo 中的 `TS-*` 代表 vTESTstudio 測試資產索引，不是腳本主體。
- 每個 `TS-*` 必須對應一個穩定的 `vTESTstudio ID`。
- `vTESTstudio ID` 應記錄在 Codebeamer 的 `TC-*` 上，並與 repo 中的 `TS-*` 文件一致。
- `TS-*` 命名建議採用 `TS-### <short-title>`，vTESTstudio 中至少保留同一個 `TS-###` 前綴。

## Minimum Mapping

| Repo concept | vTESTstudio field | Rule |
|---|---|---|
| `TS-*` | Test asset ID | 必須唯一且穩定 |
| `TC-*` | Linked testcase reference | 必須可回指到 Codebeamer testcase |
| `TR-*` | Optional trace tag | 建議保留，用於回推驗證需求 |
| `Automation Status` | Execution readiness | 與 Codebeamer 中 `TC-*` 的狀態一致 |

## Required Conventions

1. `Automation Status=automated` 的 `TC-*` 必須有 `vTESTstudio ID`。
2. 每個 `TS-*` 必須能回指一個 `TC-*`。
3. 若 `TS-*` 對應多個 testcase，必須在 repo 索引與 Codebeamer 中明確列出所有 `TC-*`。
4. 若 vTESTstudio 資產被重命名，`TS-*` 前綴與 `vTESTstudio ID` 不得失效。
5. 若自動化被退役，`Automation Status` 必須同步改為 `retired` 或等價狀態。

## TS File Content Rules

每個 repo 內 `TS-*` 文件至少應包含：
- Linked testcase
- Linked test requirement
- Execution system
- Asset identifier

## Non-Goals

- 不在 repo 中保存 vTESTstudio 腳本正文。
- 不在 v1 自動同步 Codebeamer 與 vTESTstudio 欄位。
- 不定義 vTESTstudio 專案層級流程，只定義追溯所需最小規則。
