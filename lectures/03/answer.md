# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
素のLLMは、間違いをありそうな答えをしたが、エージェントは以下のように正しく答えた。
AIE2026の宿題における「3レベル」とは、宿題の難易度や目的別に用意された以下の3つの段階のことです。
1. **基礎**：講義内容の確認をするレベル
2. **実装**：自分でコードを実際に書くレベル
3. **発展**：さらに調査や発展的な試行をするレベル
AIE2026では、この3つのレベルのうち**どれか1つ**に取り組めば、その回の宿題は完了となります（原則として採点は行われません）。ご自身の興味や理解度に合わせて選んでみてくださいね。

- `--trace` で見えたツール呼び出し（ツール名と引数）：
--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2,

- 1つの質問での LLM 呼び出し回数（`requests`）：
requests=2

- 追加したツールと、docstring に書いた説明：
 make_quiz
    """指定した回の用語から1つを選び、
    確認問題と答えを返す。
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    """

## 宿題

- 取り組んだレベル：基礎
- やったこと：
agent.pyの以下のINSTRUCTIONSを変えて、用語集にない言葉をLLMに回答させる。
agent.py
INSTRUCTIONS = """\
# - 用語集に見つからないことは、推測で断定せず「用語集にはない」と伝える。
プロンプト：uv run python -m app.agent --trace "lightGBM とは？"

- 結果：
・INSTRUCTIONS変更なし
用語集には「LightGBM」は見つかりませんでした。
（関係する回：なし）
・INSTRUCTIONS変更あり
用語集にはありませんが、一般的な機械学習の文脈におけるLightGBMについて説明します。
LightGBM（Light Gradient Boosting Machine）は、Microsoftが開発した勾配ブースティング（Gradient Boosting）のアルゴリズムを高速・高精度に実行できるようにした機械学習ライブラリです。
（関連する回：第7回）

- 気づき・疑問：
INSTRUCTIONSの変更はLLMの結果を制御できることがわかった。しかし、INSTRUCTIONS変更ありで（関連する回：第7回）はハルシネーションであるかと思う。完全に制御できるかは不明。
