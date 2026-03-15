# Result Layer Samples

這個目錄放 `Build`、`TestRun`、`Result` 與 `Evidence` 的最小樣例，用來把追溯鏈從 `TC/TS` 延伸到實際驗證結果。

v1 樣例節點：
- `BUILD-001`: 被測軟體版本
- `RUN-001`: 一次具體執行
- `RES-001`: 該次執行的結果判定
- `EVID-001`: 測試執行產出的證據

這些節點不屬於車載語意主軸，而是結果層，用來回答「在哪個 build 上、哪次 run 中執行，產生了什麼 result / evidence」。
