# 概要
![[./README_img/image1.png](https://raw.githubusercontent.com/Sasakura-ayato/nidule/main/README_img/image1.png)]
これを自動生成したい

# Usage
Python 環境で、

```
python3 main.py
```

すると、`output.txt` が生成される。

# Issue

Issue の順番は、**簡単に今後対応できそうな順**（下に行くほど対応が難しい）。

- "06時----" といった表現にはまだ対応していない
- YouTube 以外だと使えない
- いつから.link に記載されている情報しか引っ張ってこない
    - つまり、ライバーが早めに枠を立てていない時は反映されない
    - そのため該当するスケジュールのツイート URL を引っ張ってくることはできない
    - 現在は Youtube の枠の配信ページへ遷移するように書いている。

