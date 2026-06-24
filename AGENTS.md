# AGENTS.md

> 給 AI agent（與人類）編輯此 repo 的編輯指引。**新增/修改詞條前請先讀完本檔**。

## 1. Repo 定位

這是一本**借詞辭典**，不是 prompt-engineering 技巧手冊。

### 收錄標準

| ✅ 收 | ❌ 不收 |
|---|---|
| 從其他領域（軟工/邏輯/認知/語言/品質）借來、可塞進 prompt 當控制詞的術語 | Prompt engineering 內部黑話（few-shot、zero-shot、RAG、ReAct、ToT 等） |
| 在原始領域有明確、可引用的權威定義 | 隨手發明的中文形容詞、無學界共識的詞 |
| 動詞化：能放進「請以 **X** ...」句型 | 純概念名詞、無 prompt 操作介面 |

**已破例的詞條**（不要當錯誤刪除）：

1. 「思考鏈 / Chain of Thought」：雖是 prompt-engineering 詞、但已跨界普及且本義來自認知科學、收錄。
2. 「Artifact / Claude Artifact」：Claude 的產品功能、非借詞、本不符收錄標準，由 owner 於 2026-06-24 核准破例收錄。新增破例請循此例註明日期與理由。

### 收錄前先問三題

1. 這詞在原本領域有明確定義嗎？沒有 → 不收
2. 能放進 prompt 後讓 AI 行為收斂嗎？不能 → 不收
3. 跟現有條目重複嗎？跑 lint 看 slug 撞名 → 撞則不收

## 2. 單一資料源

| 檔案 | 編輯？ |
|---|---|
| `data/entries.yml` | ✅ 唯一可寫資料源 |
| `schemas/entry.schema.json` | ⚠️ 改 schema 需同步調 `build.py` / `lint_entries.py` |
| `scripts/*.py` | ⚠️ 工具改進 |
| `DICTIONARY.md` | ❌ 自動生成、勿改 |
| `QUICK-REFERENCE.md` | ❌ 自動生成、勿改 |
| `README.md` 的 entries badge 與類別計數 | ❌ `build.py` 自動更新 |

## 3. 詞條欄位規則

```yaml
- term: 中文主詞                  # 繁中、不含空格
  english: English Name           # Title Case、可含空格
  slug: english-name              # ^[a-z][a-z0-9-]*$、必須唯一、§4 規則
  category: cognition             # structure / logic / cognition / language / quality
  origin: 原始領域、年份或人名
  source:                         # ← 選填、§5 規則
    name: 權威辭典名
    url: https://...
  meaning: 一句話本義              # ≤ 30 字、不重複定義詞本身
  prompt_usage: 完整版用法         # 30-50 字、動詞開頭、說「要求 AI ...」
  short_usage: 速查表用法          # 15-25 字、動詞開頭、無句號
  example: 含**粗體術語**的範例句  # 完整句、可結尾句號
  added: "2026-05-27"             # 必須加引號（YAML 否則解析成 date 物件）
  last_verified: "2026-05-27"     # 同上
```

## 4. Slug 命名規則（純中文詞特別注意）

某些詞無對應學界英文名（如「結構化」、「修辭」），用領域標準英文意譯、**不用拼音**：

| 中文 | ✅ Slug | ❌ 不要用 |
|---|---|---|
| 結構化 | `structuring` | `jiegouhua` / `structurization` |
| 精煉 | `refinement` | `jinglian` |
| 潤飾 | `polishing` | `runshi` |
| 降噪 | `denoising` | `noise-reduction` |
| 修辭 | `rhetoric` | `xiuci` |
| 對比 | `contrast` | `comparison` |

**判斷原則**：用領域學界英文用法（查 Crystal《A Dictionary of Linguistics and Phonetics》或 Google Scholar）。不確定就先停下來、開 issue 問。

## 5. 權威來源（source）規則

新詞通常**不需要寫 `source:` 欄**，自動套類別預設：

| Category | Default source | URL |
|---|---|---|
| structure | SEVOCAB (ISO/IEC/IEEE 24765) | https://www.computer.org/sevocab |
| logic | Stanford Encyclopedia of Philosophy | https://plato.stanford.edu/ |
| cognition | APA Dictionary of Psychology | https://dictionary.apa.org/ |
| language | David Crystal, *A Dictionary of Linguistics and Phonetics* | (紙本書、無 URL) |
| quality | ISTQB Glossary | https://glossary.istqb.org/ |

### 何時寫 source override

1. **詞有更具體的權威出處**（書、論文、SEP 某條目）
   - 反脆弱性 → Nassim Taleb, *Antifragile* (2012)
   - 思考鏈 → Wei et al., arXiv:2201.11903

2. **詞在類別預設來源裡有專屬頁面、可直連**
   - 錨定 → `https://dictionary.apa.org/anchoring`（比 APA 首頁精準）

3. **詞的真實來源不是類別預設**
   - 第一性原理放 logic、但來自 Aristotle Metaphysics → SEP 該條目

## 6. Workflow

```powershell
cd D:\git_project\prompt-lexicon-zh

# 一次性安裝依賴
python -m pip install pyyaml jsonschema

# 1. 編輯 data\entries.yml（append 到 entries: 陣列尾）
# 2. 驗證 schema
python scripts\lint_entries.py
# 3. 重生 markdown（也會更新 README badge 與類別計數）
python scripts\build.py
# 4. 看 diff
git diff --stat
# 5. Commit + push
git add -A
git commit -m "Add entry: 詞名（English）"
git push origin main
```

CI 會自動跑 lint + build + 同步檢查（DICTIONARY.md / QUICK-REFERENCE.md / README.md）。URL 驗證每月 1 號排程跑。

## 7. 常見 lint 錯誤

| Error | Fix |
|---|---|
| `'foo' is not unique` (slug) | 撞到既有詞、改一個 |
| `does not match pattern '^[a-z]...'` | slug 用了大寫/底線/中文、改小寫 hyphen |
| `'2026-05-27' is not of type 'string'` | 日期沒加引號 → `"2026-05-27"` |
| `'meta' is not one of [...]` | category 拼錯、五選一 |
| `Required field 'short_usage' missing` | 補上短版用法 |

## 8. Commit 前自檢

- [ ] term / english / slug 一致（slug 是 english 的 lowercase-hyphen）
- [ ] category 對（用「borrowed from where」反推）
- [ ] source override（如有）的 URL 是真實連結
- [ ] meaning ≤ 30 字
- [ ] prompt_usage 30-50 字、動詞開頭、「要求 AI ...」
- [ ] short_usage 15-25 字、動詞開頭、句尾無句號
- [ ] example 含 `**粗體詞名**`
- [ ] 日期加雙引號
- [ ] `python scripts/lint_entries.py` 通過
- [ ] `python scripts/build.py` 跑完、DICTIONARY.md / QUICK-REFERENCE.md / README.md 都更新

## 9. 越界改動（請先開 issue 討論）

- 改 schema（影響所有現有條目）
- 改類別預設來源
- 新增第六個類別
- 改 `build.py` 輸出格式（會破壞既有 anchor 連結）
- 重新洗 slug 命名（會 break 外部引用）
