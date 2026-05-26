# Prompt 辭典速查表

關鍵詞的快速查詢表。點擊任一詞名跳轉到 [DICTIONARY.md](DICTIONARY.md) 對應的詳細詞條。

> 沒看到合用的詞？打開 [DICTIONARY.md](DICTIONARY.md) Ctrl-F 全文搜尋。
>
> 本檔由 `data/entries.yml` 經 `scripts/build.py` 自動生成，請勿直接編輯。


---


## 一、結構與系統

| 詞 | Prompt 用法 |
|---|---|
| [**內聚**](DICTIONARY.md#cohesion) | 要求每個段落只談一件事 |
| [**不變性**](DICTIONARY.md#invariance) | 要求改寫時保留事實與數字 |
| [**介面**](DICTIONARY.md#interface) | 要求先界定輸入輸出格式 |
| [**可重現性**](DICTIONARY.md#reproducibility) | 要求步驟讓他人照做也能複現 |
| [**可觀測性**](DICTIONARY.md#observability) | 要求流程加入可驗證的檢查點 |
| [**正交性**](DICTIONARY.md#orthogonality) | 要求各部分互不耦合可獨立調整 |
| [**副作用**](DICTIONARY.md#side-effect) | 要求列出隱性影響或避免之 |
| [**抽象層次**](DICTIONARY.md#abstraction-level) | 要求陳述顆粒度保持一致 |
| [**封裝**](DICTIONARY.md#encapsulation) | 要求把細節藏起來只露入口 |
| [**耦合**](DICTIONARY.md#coupling) | 要求降低或檢查相互依賴 |
| [**原子性**](DICTIONARY.md#atomicity) | 要求把任務拆到最小單位 |
| [**確定性**](DICTIONARY.md#determinism) | 要求給出明確答案不要含糊 |
| [**解耦**](DICTIONARY.md#decoupling) | 要求把糾纏概念拆開 |
| [**模組化**](DICTIONARY.md#modularization) | 要求輸出可被切片獨立使用 |
| [**冪等性**](DICTIONARY.md#idempotency) | 要求流程重複跑也不出錯 |
| [**單一職責**](DICTIONARY.md#single-responsibility) | 要求每個段落只負責一件事 |
| [**顆粒度**](DICTIONARY.md#granularity) | 要求用指定粗細程度展開 |
| [**E2E**](DICTIONARY.md#e2e) | 要求從頭到尾講完整條鏈路 |

---


## 二、邏輯與推理

| 詞 | Prompt 用法 |
|---|---|
| [**三段論**](DICTIONARY.md#syllogism) | 要求用前提前提結論的格式呈現 |
| [**反例**](DICTIONARY.md#counterexample) | 要求主動找能打破論點的案例 |
| [**反證**](DICTIONARY.md#reductio-ad-absurdum) | 要求假設反面成立並導出矛盾 |
| [**充要條件**](DICTIONARY.md#necessary-and-sufficient) | 要求區分必要與充分不要混談 |
| [**第一性原理**](DICTIONARY.md#first-principles) | 要求拋開既有方案從根本重思 |
| [**命題**](DICTIONARY.md#proposition) | 要求把模糊主張轉為可判真假句 |
| [**奧坎剃刀**](DICTIONARY.md#occams-razor) | 要求在多解釋中挑最簡的 |
| [**悖論**](DICTIONARY.md#paradox) | 要求指出方案中的自相矛盾 |
| [**演繹**](DICTIONARY.md#deduction) | 要求從已給原則嚴格推出結論 |
| [**蘊含**](DICTIONARY.md#implication) | 要求標明每步的因此或則 |
| [**假設**](DICTIONARY.md#hypothesis) | 要求把判斷講成可驗證的假設 |
| [**前提**](DICTIONARY.md#premise) | 要求先列出論證依賴的起始陳述 |
| [**等價**](DICTIONARY.md#equivalence) | 要求判斷兩說法是否真同義 |
| [**歸納**](DICTIONARY.md#induction) | 要求從多案例抽出通則 |
| [**邊界條件**](DICTIONARY.md#boundary-condition) | 要求界定方案的適用臨界值 |

---


## 三、思考與認知

| 詞 | Prompt 用法 |
|---|---|
| [**元認知**](DICTIONARY.md#metacognition) | 要求邊回答邊反思推理品質 |
| [**反向推理**](DICTIONARY.md#backward-reasoning) | 要求從目標倒推所需步驟 |
| [**心智模型**](DICTIONARY.md#mental-model) | 要求先講清楚如何理解整件事 |
| [**收斂思考**](DICTIONARY.md#convergent-thinking) | 要求從候選中挑唯一推薦 |
| [**框架**](DICTIONARY.md#framework) | 要求先建立分析結構再展開 |
| [**模式識別**](DICTIONARY.md#pattern-recognition) | 要求從案例中找共通模式 |
| [**範疇化**](DICTIONARY.md#categorization) | 要求先把雜亂項目分類再處理 |
| [**思考鏈**](DICTIONARY.md#chain-of-thought) | 要求展示完整推理步驟 |
| [**系統思考**](DICTIONARY.md#systems-thinking) | 要求考慮回饋環與長期動態 |
| [**抽象化**](DICTIONARY.md#abstraction) | 要求把案例提升為通則 |
| [**具象化**](DICTIONARY.md#concretization) | 要求把空泛敘述換成具體場景 |
| [**發散思考**](DICTIONARY.md#divergent-thinking) | 要求先大量產出選項暫不評價 |
| [**層次化**](DICTIONARY.md#hierarchization) | 要求把扁平清單轉為樹狀結構 |
| [**類比**](DICTIONARY.md#analogy) | 要求用熟悉事物說明陌生概念 |
| [**隱喻**](DICTIONARY.md#metaphor) | 要求找一個強力隱喻貫穿說明 |

---


## 四、語言與表達

| 詞 | Prompt 用法 |
|---|---|
| [**口語化**](DICTIONARY.md#colloquial) | 要求改成自然對話的語氣 |
| [**排比**](DICTIONARY.md#parallelism) | 要求用一致句式呈現並列項 |
| [**修辭**](DICTIONARY.md#rhetoric) | 要求調整說服力強度 |
| [**重組**](DICTIONARY.md#restructuring) | 要求不增刪只調整段落順序 |
| [**結構化**](DICTIONARY.md#structuring) | 要求加標題條列表格組織 |
| [**對比**](DICTIONARY.md#contrast) | 要求用 A vs B 並列呈現差異 |
| [**精煉**](DICTIONARY.md#refinement) | 要求砍掉冗餘只留本質 |
| [**語域**](DICTIONARY.md#register) | 要求切換到指定的正式層次 |
| [**語境**](DICTIONARY.md#context) | 要求先確認情境再回答 |
| [**潤飾**](DICTIONARY.md#polishing) | 要求只改通順度不動結構 |
| [**擴寫**](DICTIONARY.md#expansion) | 要求把要點展開為完整段落 |
| [**降噪**](DICTIONARY.md#denoising) | 要求濾出真正關鍵的部分 |

---


## 五、品質與檢查

| 詞 | Prompt 用法 |
|---|---|
| [**一致性**](DICTIONARY.md#consistency) | 要求檢查前後是否矛盾用詞是否統一 |
| [**反例測試**](DICTIONARY.md#counterexample-testing) | 要求主動構造能戳破結論的場景 |
| [**反脆弱性**](DICTIONARY.md#antifragility) | 要求方案遇例外能變更穩健 |
| [**可重複性**](DICTIONARY.md#repeatability) | 要求自己跑兩次也要結果一致 |
| [**可驗證性**](DICTIONARY.md#verifiability) | 要求每個結論附可查證的依據 |
| [**完備性**](DICTIONARY.md#completeness) | 要求檢查是否所有案例都已涵蓋 |
| [**盲點檢查**](DICTIONARY.md#blind-spot-check) | 要求設想自己漏掉了什麼 |
| [**穩健性**](DICTIONARY.md#robustness) | 要求輸入不理想時也能撐住 |
| [**健全性**](DICTIONARY.md#soundness) | 要求核對前提真實且推理有效 |
| [**雙重檢查**](DICTIONARY.md#double-check) | 要求用另一種方法重新推導一次 |
| [**漏洞檢查**](DICTIONARY.md#vulnerability-check) | 要求從濫用者視角找弱點 |
| [**邊界測試**](DICTIONARY.md#boundary-testing) | 要求特別說明極端值與空值行為 |
