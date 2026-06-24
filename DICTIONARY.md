# Prompt 辭典

可放入 prompt 的關鍵詞，全部從軟體工程、邏輯學、認知科學、語言學、品質保證五大領域借用而來。這本辭典不發明新詞、不收錄 prompt engineering 內部黑話（few-shot、RAG 等），只挑「已經在其他領域有明確定義、可以直接搬進 prompt 當控制詞使用」的術語。每個詞條給五個欄位：來源、權威參考、本義、Prompt 用法、範例，方便 Ctrl-F 翻完直接抄進對話框。

> 本檔由 `data/entries.yml` 經 `scripts/build.py` 自動生成，請勿直接編輯。


---


## 一、結構與系統


<a id="cohesion"></a>
### 內聚 / Cohesion

- **來源**：軟體工程（Constantine, 1974）
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：模組內部元素彼此關聯的緊密程度
- **Prompt 用法**：要求 AI 輸出的每個段落/章節只談一件事、職責集中
- **範例**：請以高**內聚**原則撰寫這份文件，每個小節只處理單一主題。


<a id="invariance"></a>
### 不變性 / Invariance

- **來源**：數學、函數式程式設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：某性質在操作前後恆保持不變
- **Prompt 用法**：要求 AI 在改寫/重構時保持某些核心條件不被破壞
- **範例**：請保留原文的**不變性**：事實、數字、人名一律不得更動，只能調整語句。


<a id="interface"></a>
### 介面 / Interface

- **來源**：軟體工程、物件導向
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：兩個系統之間的契約與互動規範
- **Prompt 用法**：要求 AI 明確界定輸入/輸出格式、不要把實作細節漏出來
- **範例**：請先定義這個流程的**介面**（輸入、輸出、前後條件）再開始細節。


<a id="reproducibility"></a>
### 可重現性 / Reproducibility

- **來源**：科學研究、實驗方法學
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：在相同條件下他人能重複得到相同結果
- **Prompt 用法**：要求 AI 給出的步驟讓別人照做也能得到一樣的產出
- **範例**：請以**可重現性**為目標撰寫步驟，任何人照做都應得到相同結果。


<a id="observability"></a>
### 可觀測性 / Observability

- **來源**：控制理論、SRE
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：從外部輸出能推斷系統內部狀態的程度
- **Prompt 用法**：要求 AI 在流程中加入記錄、檢查點、可被外部驗證的訊號
- **範例**：請為這個流程加入**可觀測性**設計，每個關鍵步驟都要有可查驗的輸出。


<a id="orthogonality"></a>
### 正交性 / Orthogonality

- **來源**：線性代數、軟體工程
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：兩個元素彼此獨立、改動一者不影響另一者
- **Prompt 用法**：要求 AI 拆解時各部分互不耦合、可獨立調整
- **範例**：請以**正交性**原則拆分這份計畫，每個維度可獨立調整不互相牽動。


<a id="side-effect"></a>
### 副作用 / Side Effect

- **來源**：函數式程式設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：操作除了回傳值之外、對外部狀態造成的額外影響
- **Prompt 用法**：要求 AI 明確列出某動作的隱性影響、或避免產生副作用
- **範例**：請列出這個修改可能造成的**副作用**，特別是對其他模組的隱性影響。


<a id="abstraction-level"></a>
### 抽象層次 / Abstraction Level

- **來源**：軟體工程、系統設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：陳述細節粗細的階層位置
- **Prompt 用法**：要求 AI 在指定的抽象層級講話、不要混用不同顆粒度
- **範例**：請保持同一**抽象層次**陳述，不要時而談架構時而談變數命名。


<a id="encapsulation"></a>
### 封裝 / Encapsulation

- **來源**：物件導向程式設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：把實作細節藏在介面背後、外部只看到必要的部分
- **Prompt 用法**：要求 AI 把複雜邏輯包起來、對外只給簡潔的入口
- **範例**：請將內部細節**封裝**起來，對外只暴露最少必要的呼叫方式。


<a id="coupling"></a>
### 耦合 / Coupling

- **來源**：軟體工程（Constantine, 1974）
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：模組之間相互依賴的程度
- **Prompt 用法**：要求 AI 降低各部分的相互依賴、或指出哪些地方耦合過高
- **範例**：請檢查這份設計的**耦合**度，找出修改 A 就會牽動 B 的環節。


<a id="atomicity"></a>
### 原子性 / Atomicity

- **來源**：資料庫交易、軟體設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：不可再分割、要麼全做、要麼全不做
- **Prompt 用法**：要求把任務拆到不能再分的最小單位、或要求每個輸出獨立可驗證
- **範例**：請以**原子性**原則拆解這個需求，每一步驟必須獨立可執行。


<a id="determinism"></a>
### 確定性 / Determinism

- **來源**：計算理論、形式驗證
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：給定相同輸入必定產生相同輸出、無隨機性
- **Prompt 用法**：要求 AI 給出明確答案、不要含糊、不要「視情況而定」
- **範例**：請以**確定性**回答這個問題，給出明確結論而非條件式回應。


<a id="decoupling"></a>
### 解耦 / Decoupling

- **來源**：軟體工程
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：主動降低或切斷模組之間的依賴
- **Prompt 用法**：要求 AI 把目前糾纏在一起的概念/流程拆開
- **範例**：請把流程裡的資料處理與通知邏輯**解耦**，分成兩個獨立段落。


<a id="modularization"></a>
### 模組化 / Modularization

- **來源**：軟體工程
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：將整體拆成可獨立使用、替換的模組
- **Prompt 用法**：要求 AI 輸出可被切片使用的段落、不要黏成一坨
- **範例**：請**模組化**地撰寫這份指南，讀者可只取其中一節單獨使用。


<a id="idempotency"></a>
### 冪等性 / Idempotency

- **來源**：數學、API 設計
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：同一操作執行多次與執行一次效果相同
- **Prompt 用法**：要求 AI 產出的 SOP、指令、流程「重複跑也不出錯」
- **範例**：請以**冪等性**原則撰寫這份還原流程，確保腳本重跑不會造成資料不一致。


<a id="single-responsibility"></a>
### 單一職責 / Single Responsibility

- **來源**：物件導向設計（SOLID 之首）
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：每個單元只承擔一項職責、只有一個改變的理由
- **Prompt 用法**：要求 AI 拆分時每個段落/函數/章節只負責一件事
- **範例**：請依**單一職責**原則重組這份提案，每段只回答一個問題。


<a id="granularity"></a>
### 顆粒度 / Granularity

- **來源**：軟體工程、資料倉儲
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：劃分的精細程度
- **Prompt 用法**：要求 AI 用指定的粗細程度展開、避免過粗或過細
- **範例**：請以中等**顆粒度**展開計畫，不要細到動作層、也不要粗到只剩目標。


<a id="e2e"></a>
### E2E / End-to-end

- **來源**：軟體測試、網路通訊
- **權威參考**：[SEVOCAB (ISO/IEC/IEEE 24765)](https://www.computer.org/sevocab)
- **本義**：從起點到終點、涵蓋整條鏈路的完整視角
- **Prompt 用法**：要求 AI 從使用者第一個動作講到最後一個結果、不要只看片段
- **範例**：請以 **E2E** 視角描述這個流程，從使用者按下按鈕到收到結果為止。


<a id="artifact"></a>
### Artifact / Claude Artifact

- **來源**：Anthropic Claude 產品功能（2024）
- **權威參考**：[Claude Help Center - What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- **本義**：把 AI 產出渲染成獨立、可即時瀏覽與分享的 claude.ai 頁面
- **Prompt 用法**：要求 AI 把成果做成自包含、可即時預覽與分享的獨立頁面、而非只給對話內純文字
- **範例**：請把這份報表做成 **Artifact**，獨立成可即時瀏覽、可分享的頁面。

---


## 二、邏輯與推理


<a id="syllogism"></a>
### 三段論 / Syllogism

- **來源**：亞里斯多德邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：由大前提、小前提、推出結論的演繹結構
- **Prompt 用法**：要求 AI 用「前提 → 前提 → 結論」的標準格式呈現推理
- **範例**：請用**三段論**結構展示這個論證，清楚標出兩個前提與結論。


<a id="counterexample"></a>
### 反例 / Counterexample

- **來源**：數學、邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：能推翻一個普遍命題的單一具體案例
- **Prompt 用法**：要求 AI 主動找出能打破自己論點的案例
- **範例**：請為你剛才的結論提出**反例**，若找不到反例再說明為何普遍成立。


<a id="reductio-ad-absurdum"></a>
### 反證 / Reductio ad Absurdum

- **來源**：古希臘邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：假設反面為真、推出矛盾、從而證明原命題為真
- **Prompt 用法**：要求 AI 用「假設不成立 → 推出荒謬」的方式論證
- **範例**：請用**反證**法證明這個結論，先假設它為假再導出矛盾。


<a id="necessary-and-sufficient"></a>
### 充要條件 / Necessary and Sufficient

- **來源**：邏輯學、數學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：必要條件（缺它不成立）加上充分條件（有它即成立）
- **Prompt 用法**：要求 AI 區分「沒有它不行」和「有它就夠」、不要混為一談
- **範例**：請列出達成這個目標的**充要條件**，分別說明必要與充分的部分。


<a id="first-principles"></a>
### 第一性原理 / First Principles

- **來源**：哲學（亞里斯多德）、物理學
- **權威參考**：[SEP - Aristotle's Metaphysics](https://plato.stanford.edu/entries/aristotle-metaphysics/)
- **本義**：從不可再分割的基本事實出發推理、不依賴類比
- **Prompt 用法**：要求 AI 拋開既有方案、從根本需求重新思考
- **範例**：請用**第一性原理**重新分析這個架構，不要參考既有的業界做法。


<a id="proposition"></a>
### 命題 / Proposition

- **來源**：邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：可以判定為真或假的陳述句
- **Prompt 用法**：要求 AI 把模糊主張轉成可判真假的明確命題
- **範例**：請把這段論述拆成數個獨立**命題**，每一個都可以單獨判定真假。


<a id="occams-razor"></a>
### 奧坎剃刀 / Occam's Razor

- **來源**：中世紀邏輯學（William of Ockham）
- **權威參考**：[SEP - Simplicity](https://plato.stanford.edu/entries/simplicity/)
- **本義**：若無必要、勿增實體；同等解釋力下選最簡假設
- **Prompt 用法**：要求 AI 在多個解釋中選最簡單的、不要過度推測
- **範例**：請用**奧坎剃刀**原則篩選這幾個假設，留下最簡單而仍能解釋現象的那個。


<a id="paradox"></a>
### 悖論 / Paradox

- **來源**：邏輯學、哲學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：表面合理推理卻導出矛盾或不可接受結論的陳述
- **Prompt 用法**：要求 AI 主動指出方案中的自相矛盾之處
- **範例**：請檢查這份設計是否存在**悖論**，有沒有條件互相打架的地方。


<a id="deduction"></a>
### 演繹 / Deduction

- **來源**：邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：從一般原則推出特定結論、結論必然為真
- **Prompt 用法**：要求 AI 從已給原則嚴格推出、不要靠經驗或舉例
- **範例**：請用**演繹**方式從前述三條原則推出結論，不要引用其他案例。


<a id="implication"></a>
### 蘊含 / Implication

- **來源**：邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：若 A 則 B 的條件關係
- **Prompt 用法**：要求 AI 明確標示「因此」「則」的邏輯連結、不要含糊
- **範例**：請把這段推理的**蘊含**關係標示清楚，每一步都標出「因此」。


<a id="hypothesis"></a>
### 假設 / Hypothesis

- **來源**：科學方法
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：可被驗證或推翻的暫時性主張
- **Prompt 用法**：要求 AI 把判斷講成可驗證的假設、而非斷言
- **範例**：請把你的判斷改寫成可驗證的**假設**，並指出如何驗證它。


<a id="premise"></a>
### 前提 / Premise

- **來源**：邏輯學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：推理所依據的起始陳述
- **Prompt 用法**：要求 AI 明確列出論證所依賴的所有前提
- **範例**：請先列出這個結論所依賴的**前提**，再開始推理。


<a id="equivalence"></a>
### 等價 / Equivalence

- **來源**：邏輯學、數學
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：兩個陳述彼此互相蘊含、真假同步
- **Prompt 用法**：要求 AI 判斷兩個說法是否真的同義、或找出兩者的等價形式
- **範例**：請判斷這兩個敘述是否**等價**，若不等價請指出差異。


<a id="induction"></a>
### 歸納 / Induction

- **來源**：邏輯學、科學方法
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：從多個個案歸結出一般規律
- **Prompt 用法**：要求 AI 從具體案例中抽出通則、而非直接給結論
- **範例**：請從這五個案例**歸納**出共通模式，再給出一般性結論。


<a id="boundary-condition"></a>
### 邊界條件 / Boundary Condition

- **來源**：數學、物理、軟體測試
- **權威參考**：[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)
- **本義**：適用範圍的臨界值或限制條件
- **Prompt 用法**：要求 AI 明確界定方案在什麼情況下成立、超出何時失效
- **範例**：請列出這個建議的**邊界條件**，超過哪些情況就不再適用。


<a id="dialectic"></a>
### 辯證法 / Dialectic

- **來源**：古希臘哲學、Hegel《邏輯學》
- **權威參考**：[Stanford Encyclopedia of Philosophy - Hegel's Dialectics](https://plato.stanford.edu/entries/hegel-dialectics/)
- **本義**：透過正論、反論、合論的對立統一推進思考
- **Prompt 用法**：要求 AI 用「正論 → 反論 → 合論」三段式結構分析議題
- **範例**：請用**辯證法**結構分析這個議題：先列支持論點、再列反對論點、最後綜合出折衷方案。

---


## 三、思考與認知


<a id="metacognition"></a>
### 元認知 / Metacognition

- **來源**：認知心理學（Flavell, 1979）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：對自己思考過程的覺察與監控
- **Prompt 用法**：要求 AI 邊回答邊反思自己的推理品質與限制
- **範例**：請啟動**元認知**：每段回答後簡述你做了什麼推理、哪裡可能出錯。


<a id="backward-reasoning"></a>
### 反向推理 / Backward Reasoning

- **來源**：認知科學、解題理論
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：從目標往回推、找出達成所需的前置條件
- **Prompt 用法**：要求 AI 從結果出發倒推所需步驟、而非從現狀出發
- **範例**：請用**反向推理**從目標倒推步驟，列出每一步的必要前置條件。


<a id="mental-model"></a>
### 心智模型 / Mental Model

- **來源**：認知科學（Craik, 1943）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：人對事物運作機制的內在表徵
- **Prompt 用法**：要求 AI 先講清楚它如何理解整件事、再開始細節
- **範例**：請先描述你對這個系統的**心智模型**，再回答具體問題。


<a id="convergent-thinking"></a>
### 收斂思考 / Convergent Thinking

- **來源**：認知心理學（Guilford, 1956）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：從多個選項中聚焦到單一最佳答案的思考方式
- **Prompt 用法**：要求 AI 從候選方案中挑出唯一推薦、不要繼續發散
- **範例**：請進入**收斂思考**模式，從前面列出的五個方案中挑出唯一推薦。


<a id="framework"></a>
### 框架 / Framework

- **來源**：認知科學、管理學
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：用來組織思考的結構化視角
- **Prompt 用法**：要求 AI 套用某個既有框架分析、或先建立分析框架再展開
- **範例**：請先建立分析**框架**，再用此框架逐項檢視這個提案。


<a id="pattern-recognition"></a>
### 模式識別 / Pattern Recognition

- **來源**：認知科學、機器學習
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：從雜訊中辨識出重複出現的結構
- **Prompt 用法**：要求 AI 從一堆案例中找出共通模式、而非逐案分析
- **範例**：請在這 20 筆事件中做**模式識別**，找出反覆出現的根因類型。


<a id="categorization"></a>
### 範疇化 / Categorization

- **來源**：認知語言學（Rosch, 1973）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：將個體歸入類別以便處理
- **Prompt 用法**：要求 AI 先把雜亂項目分類、再針對類別處理
- **範例**：請先對這份清單做**範疇化**，分成 3-5 組再各組給建議。


<a id="chain-of-thought"></a>
### 思考鏈 / Chain of Thought

- **來源**：認知科學（已跨界普及為 LLM 術語）
- **權威參考**：[Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (arXiv:2201.11903, 2022)](https://arxiv.org/abs/2201.11903)
- **本義**：把推理過程逐步外顯、而非只給結論
- **Prompt 用法**：要求 AI 展示完整推理步驟、不要跳到結論
- **範例**：請用**思考鏈**方式回答，每一步推理都明寫出來。


<a id="systems-thinking"></a>
### 系統思考 / Systems Thinking

- **來源**：管理學（Senge）、控制論
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：從整體關係與回饋環路看問題、而非孤立元素
- **Prompt 用法**：要求 AI 考慮元素間的回饋與長期動態、不要只看單點
- **範例**：請以**系統思考**檢視這個方案，找出可能的回饋環與長期副作用。


<a id="abstraction"></a>
### 抽象化 / Abstraction

- **來源**：哲學、計算機科學
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：去除具體細節、保留共通本質
- **Prompt 用法**：要求 AI 把具體案例提升為通則
- **範例**：請對這三個案例做**抽象化**，提煉出可應用於其他情境的通則。


<a id="concretization"></a>
### 具象化 / Concretization

- **來源**：認知科學、教學設計
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：把抽象概念落實為具體案例或畫面
- **Prompt 用法**：要求 AI 把空泛敘述換成可想像的具體場景
- **範例**：請把這段抽象描述**具象化**，給出一個讀者可想像的具體場景。


<a id="divergent-thinking"></a>
### 發散思考 / Divergent Thinking

- **來源**：認知心理學（Guilford, 1956）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：從單一起點生成多個可能方向的思考方式
- **Prompt 用法**：要求 AI 先大量產出選項、暫不評價
- **範例**：請先做**發散思考**列出至少十種可能做法，暫不評估優劣。


<a id="hierarchization"></a>
### 層次化 / Hierarchization

- **來源**：認知科學、系統設計
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：將事物依抽象/重要程度分層組織
- **Prompt 用法**：要求 AI 把扁平清單轉成有層級結構的樹狀組織
- **範例**：請把這 30 條重點**層次化**，分成主類、次類、細項三層。


<a id="analogy"></a>
### 類比 / Analogy

- **來源**：認知科學、修辭學
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：藉由結構相似性把已知概念對應到未知領域
- **Prompt 用法**：要求 AI 用熟悉的事物來說明陌生概念
- **範例**：請用一個日常生活的**類比**說明這個技術概念。


<a id="metaphor"></a>
### 隱喻 / Metaphor

- **來源**：認知語言學（Lakoff & Johnson）
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/)
- **本義**：用 A 概念來理解 B 概念、不是修辭裝飾而是認知工具
- **Prompt 用法**：要求 AI 找一個強而有力的隱喻來貫穿整段說明
- **範例**：請為這個複雜系統找一個一以貫之的**隱喻**，讓讀者一句話就懂。


<a id="anchoring"></a>
### 錨定 / Anchoring

- **來源**：行為經濟學、Tversky & Kahneman (1974)
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/anchoring)
- **本義**：對第一個收到的資訊賦予過高權重、後續判斷以此為基準
- **Prompt 用法**：主動給 AI 一個參照點作為起算基準、或要求 AI 警覺自己是否被前文錨定
- **範例**：請以**錨定**到本季 KPI 為起點，後續所有提案都對齊這個基準評估。


<a id="confirmation-bias"></a>
### 確認偏誤 / Confirmation Bias

- **來源**：認知心理學、Wason (1960)
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/confirmation-bias)
- **本義**：偏好支持既有信念的資訊、忽略反證
- **Prompt 用法**：要求 AI 主動找反證、或檢查論述是否只挑符合假設的資料
- **範例**：請檢查這份報告是否存在**確認偏誤**，列出三個與結論相反的證據。


<a id="cognitive-load"></a>
### 認知負荷 / Cognitive Load

- **來源**：Sweller (1988) 認知負荷理論
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/cognitive-load)
- **本義**：工作記憶在處理資訊時承受的心智壓力
- **Prompt 用法**：要求 AI 降低輸出的閱讀難度、控制每段資訊密度
- **範例**：請以低**認知負荷**為設計目標，每段落只解釋一個概念、術語首次出現必附簡釋。


<a id="calibration"></a>
### 校準 / Calibration

- **來源**：心理計量、決策科學
- **權威參考**：[APA Dictionary of Psychology](https://dictionary.apa.org/calibration)
- **本義**：讓主觀判斷與實際結果對齊的調整過程
- **Prompt 用法**：要求 AI 依證據強度調整結論信心，並明示不確定範圍
- **範例**：請對你的結論做**校準**，高不確定段落要降語氣並標示依據不足處。

---


## 四、語言與表達


<a id="colloquial"></a>
### 口語化 / Colloquialization

- **來源**：語言學、修辭學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：把書面/專業文體轉為日常對話風格
- **Prompt 用法**：要求 AI 把生硬文字改成自然口吻、像在對人說話
- **範例**：請把這段技術文件**口語化**，改成像對同事口頭說明的語氣。


<a id="parallelism"></a>
### 排比 / Parallelism

- **來源**：修辭學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：用相同句式串接多項、強化節奏與比較
- **Prompt 用法**：要求 AI 用結構一致的句式呈現並列項目
- **範例**：請用**排比**句式重寫這三個重點，讓讀者一眼看出對應關係。


<a id="rhetoric"></a>
### 修辭 / Rhetoric

- **來源**：古典修辭學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：為達成說服或感染效果而調整的語言策略
- **Prompt 用法**：要求 AI 強化或弱化修辭、調整說服力強度
- **範例**：請降低這段文案的**修辭**強度，改成中性客觀的描述。


<a id="restructuring"></a>
### 重組 / Reorganization

- **來源**：寫作學、編輯學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：保留資訊但重新安排呈現順序與結構
- **Prompt 用法**：要求 AI 不增刪內容、只調整段落順序與切分
- **範例**：請**重組**這篇草稿，不要增刪任何資訊、只調整段落順序讓邏輯更清楚。


<a id="structuring"></a>
### 結構化 / Structurization

- **來源**：寫作學、資訊架構
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：把散亂內容轉為有層次、可導覽的形式
- **Prompt 用法**：要求 AI 用標題、條列、表格組織輸出
- **範例**：請把這段散文**結構化**，加上標題、條列與必要的表格。


<a id="contrast"></a>
### 對比 / Contrast

- **來源**：修辭學、寫作學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：將兩個事物並列以突顯差異
- **Prompt 用法**：要求 AI 用「A vs B」的格式呈現比較、而非分述
- **範例**：請用**對比**手法呈現新舊方案差異，並列陳述每個維度。


<a id="refinement"></a>
### 精煉 / Refinement

- **來源**：寫作學、編輯學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：刪去冗餘、保留核心、提升密度
- **Prompt 用法**：要求 AI 砍掉廢話、把長文壓縮到剩本質
- **範例**：請**精煉**這份報告到三分之一長度，只保留決策必要的資訊。


<a id="register"></a>
### 語域 / Register

- **來源**：社會語言學（Halliday）
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：依場合調整的語言層次（正式/非正式/技術/通俗）
- **Prompt 用法**：要求 AI 切換到指定語域、不要混用
- **範例**：請用適合對高階主管的正式**語域**改寫這封信。


<a id="context"></a>
### 語境 / Context

- **來源**：語言學、語用學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：話語發生的情境、上下文與背景知識
- **Prompt 用法**：要求 AI 先確認語境再回答、不要脫離情境給通用建議
- **範例**：請先釐清這個問題的**語境**（誰問、為何問、給誰看），再給建議。


<a id="polishing"></a>
### 潤飾 / Polishing

- **來源**：寫作學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：修整語句通順度與用詞但不動結構與內容
- **Prompt 用法**：要求 AI 只改文字流暢度、不要改原意或結構
- **範例**：請**潤飾**這段文字，只修語句通順度，保留原意與段落結構。


<a id="expansion"></a>
### 擴寫 / Expansion

- **來源**：寫作學
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：從綱要或短句延展為完整段落
- **Prompt 用法**：要求 AI 把要點展開為敘述、補上脈絡與例證
- **範例**：請把這份大綱**擴寫**為完整段落，每個要點補上脈絡與一個例證。


<a id="denoising"></a>
### 降噪 / Denoising

- **來源**：訊號處理、機器學習
- **權威參考**：David Crystal, A Dictionary of Linguistics and Phonetics
- **本義**：去除無關訊息、突顯核心訊號
- **Prompt 用法**：要求 AI 從一大堆雜訊資料中濾出真正關鍵的部分
- **範例**：請對這份會議逐字稿做**降噪**，只留下與決策相關的發言。

---


## 五、品質與檢查


<a id="consistency"></a>
### 一致性 / Consistency

- **來源**：資料庫理論（ACID）、品質保證
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：前後不矛盾、命名/格式/語氣統一
- **Prompt 用法**：要求 AI 檢查文件內前後是否打架、用詞是否統一
- **範例**：請檢查這份文件的**一致性**，找出前後矛盾或用詞不統一之處。


<a id="counterexample-testing"></a>
### 反例測試 / Counterexample Testing

- **來源**：形式驗證、軟體測試
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：主動構造能推翻主張的案例來驗證強度
- **Prompt 用法**：要求 AI 不只驗證正例、要主動構造能戳破的反例
- **範例**：請對這個結論做**反例測試**，主動構造能戳破它的場景。


<a id="antifragility"></a>
### 反脆弱性 / Antifragility

- **來源**：Nassim Taleb《反脆弱》
- **權威參考**：[Nassim Taleb, Antifragile (Random House, 2012)](https://en.wikipedia.org/wiki/Antifragility)
- **本義**：在壓力與不確定下變得更強的特質（不只是抗壓、是受益）
- **Prompt 用法**：要求 AI 設計的方案能因例外/失敗變得更好、而不只是不崩
- **範例**：請以**反脆弱性**為設計目標，這個流程遇到例外時應該變得更穩健而不是退化。


<a id="repeatability"></a>
### 可重複性 / Repeatability

- **來源**：計量學、實驗科學
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：同一人同一條件多次執行得到一致結果
- **Prompt 用法**：要求 AI 的步驟自己跑兩次也要結果一致、不要看心情
- **範例**：請確保這份流程的**可重複性**，同一人照做兩次結果必須一致。


<a id="verifiability"></a>
### 可驗證性 / Verifiability

- **來源**：哲學（Popper）、品質保證
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：主張可被獨立檢查為真或為假
- **Prompt 用法**：要求 AI 給出的每個結論都附上可查證的依據
- **範例**：請確保每個結論的**可驗證性**，附上能讓第三方查證的來源或測試方法。


<a id="completeness"></a>
### 完備性 / Completeness

- **來源**：邏輯學、形式系統
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：涵蓋所有應處理的情況、無遺漏
- **Prompt 用法**：要求 AI 檢查是否所有案例都已處理、不要漏邊角
- **範例**：請檢查這份規格的**完備性**，列出尚未涵蓋的邊角情況。


<a id="blind-spot-check"></a>
### 盲點檢查 / Blind Spot Check

- **來源**：認知偏誤研究、稽核實務
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：主動尋找自己沒看到、不會想到的角度
- **Prompt 用法**：要求 AI 跳出當前框架、設想自己漏掉了什麼
- **範例**：請對這份計畫做**盲點檢查**，提出三個我可能完全沒想到的風險。


<a id="robustness"></a>
### 穩健性 / Robustness

- **來源**：統計學、控制理論
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：在輸入有雜訊或偏離預期時仍維持表現
- **Prompt 用法**：要求 AI 的方案在輸入不理想時也要能撐住
- **範例**：請評估這個流程的**穩健性**，若輸入有缺漏或格式錯誤會發生什麼。


<a id="soundness"></a>
### 健全性 / Soundness

- **來源**：邏輯學、形式驗證
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：前提為真且推理有效、結論必然為真
- **Prompt 用法**：要求 AI 檢查論證是否「前提真且推理對」、而非只看結論順眼
- **範例**：請檢查這段推論的**健全性**，逐一核對前提是否真實、推理是否有效。


<a id="double-check"></a>
### 雙重檢查 / Double Check

- **來源**：航空、醫療、品質保證
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：用獨立第二種方法重做一次以發現第一次的錯
- **Prompt 用法**：要求 AI 給完答案再用另一種方式重算/重推一次
- **範例**：請對這個答案做**雙重檢查**，用另一種獨立方法重新推導一次。


<a id="vulnerability-check"></a>
### 漏洞檢查 / Vulnerability Check

- **來源**：資訊安全、稽核
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：主動尋找可被濫用或失效的脆弱點
- **Prompt 用法**：要求 AI 從攻擊者/濫用者視角找出弱點
- **範例**：請對這份規則做**漏洞檢查**，從會鑽漏洞的人的角度找出可被繞過之處。


<a id="boundary-testing"></a>
### 邊界測試 / Boundary Testing

- **來源**：軟體測試
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：在輸入範圍的臨界值上特別驗證
- **Prompt 用法**：要求 AI 特別處理極端值、零值、上限、空值等情境
- **範例**：請對這個方案做**邊界測試**，特別說明在零、極大、空輸入時的行為。


<a id="acceptance-criteria"></a>
### 驗收標準 / Acceptance Criteria

- **來源**：敏捷開發、需求工程
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：一個交付物被視為「完成」所必須符合的具體可驗證條件
- **Prompt 用法**：要求 AI 在開始任務前先明確產出的判定條件、避免做完才發現不對
- **範例**：請先列出這份報告的**驗收標準**（至少 5 條可驗證），確認後再開始撰寫。


<a id="traceability"></a>
### 可追溯性 / Traceability

- **來源**：需求工程、品質管理
- **權威參考**：[ISTQB Glossary](https://glossary.istqb.org/)
- **本義**：結果能回溯到來源與決策依據的能力
- **Prompt 用法**：要求 AI 讓每項結論對應來源、需求或步驟，保留稽核路徑
- **範例**：請以**可追溯性**整理此提案，每個結論後都標註對應依據與決策步驟。
