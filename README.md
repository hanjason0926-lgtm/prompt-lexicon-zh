# Prompt 辭典 / Prompt Lexicon

![License](https://img.shields.io/badge/license-MIT-blue) ![Language](https://img.shields.io/badge/lang-繁體中文-brightgreen) ![Entries](https://img.shields.io/badge/entries-77-orange)

一句話定位：**把工程、邏輯、認知科學的精準術語、拿來當 prompt 的控制詞彙。**

## 為什麼需要這本辭典

- 中文模糊 → 精準術語讓 AI 收斂到單一語義
- 借用既有概念 → 不需發明新詞、業界已有共識
- 可組合 → 每個詞都是獨立「樂高積木」、可疊加使用

## 怎麼用

1. 寫 prompt 時想表達某個控制意圖
2. 在 [DICTIONARY.md](DICTIONARY.md) Ctrl-F 找最貼近的術語
3. 把術語放進 prompt，例：「請以**冪等性**原則撰寫這段 SOP」

## 索引

兩種使用方式：

- 📋 **[QUICK-REFERENCE.md](QUICK-REFERENCE.md)** — 五張速查表，點詞名跳到詳細條目（最快）
- 📖 **[DICTIONARY.md](DICTIONARY.md)** — 完整詞條（含來源、權威參考、本義、用法、範例）

> 上面兩個檔案是**從 `data/entries.yml` 自動生成**、請勿直接編輯。

各類別詞條數：
- 一、結構與系統（18）
- 二、邏輯與推理（16）
- 三、思考與認知（18）
- 四、語言與表達（12）
- 五、品質與檢查（13）

## 貢獻流程（新增/修改詞條）

唯一資料源是 `data/entries.yml`。請**勿直接編輯** `DICTIONARY.md` 或 `QUICK-REFERENCE.md` —— 它們會被 build 腳本覆蓋。

新增一條詞：

1. 在 `data/entries.yml` 的 `entries:` 陣列加一條（參考既有格式）
2. 跑 `python scripts/lint_entries.py` 確認 schema 通過
3. 跑 `python scripts/build.py` 產生新 markdown
4. `git add -A && git commit -m "Add entry: 詞名"`
5. 開 PR；CI 會自動驗證 schema、build 是否同步

排程任務：每月 1 號自動跑 `verify_sources.py` 檢查所有來源 URL，壞掉會自動開 issue。

### 本地環境

```powershell
python -m pip install pyyaml jsonschema
python scripts/lint_entries.py
python scripts/build.py
```

## 授權

MIT License — 自由使用、修改、分發。
