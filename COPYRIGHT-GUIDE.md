# 著作権ガイドライン

IEEE論文をベースにZenn記事を執筆する際のルール。

## OK（許可される行為）

- 論文内容を**自分の言葉で要約・解説**する
- DOIリンクで**出典を明記**する
- **自作の図**を使う（matplotlib / schemdraw / Mermaid）
- 論文の測定データに基づき**独自のグラフを作成**する（事実のデータに著作権は及ばない）
- 複数論文のデータを**比較表にまとめる**

## NG（禁止される行為）

- 論文の図表を**そのまま転載**する
- 論文の文章を**コピペ**する
- Abstractを**丸写し**する
- 論文PDFのスクリーンショットを貼る

## 引用ルール

- 引用は `>` blockquoteで明示し、出典を記載する
- 引用は**最小限**にとどめる（1-2文程度）
- 自分の解説が**主体**であること（引用が記事の大部分を占めてはならない）

### 引用例

> "The load modulated balanced amplifier (LMBA) achieves high efficiency over a wide bandwidth by modulating the load impedance presented to the balanced pair." [1]

この手法のポイントは、バランスド構成の負荷インピーダンスを動的に制御することで...

## 数値データの扱い

- 論文中の測定値（PAE, Pout, Gain等）を表やグラフで再構成するのはOK
- グラフは必ず**自作**する（論文のグラフ画像をトレースしない）
- データの出典を明記する（例：「[1]のTable IIより」）

## 参考文献の形式

IEEE引用形式を使用。DOIリンク付き。

```
[1] A. Author et al., "Paper Title," IEEE Trans. Microw. Theory Techn., vol. 70, no. 5, pp. 2345-2356, May 2022. DOI: [10.1109/TMTT.2022.xxxxxxx](https://doi.org/10.1109/TMTT.2022.xxxxxxx)
```
