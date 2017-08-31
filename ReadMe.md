# このソフトウェアについて

小説を書くためのローカルWebツール。

* 400字まで
* 1件読み切り
* ファイル書き出し

# 実行環境の用意

* [実行環境の用意](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md)
* [ライセンス](#ライセンス)にあるPythonパッケージを`pip install flask`のようにしてインストールする

# 実行

```sh
$ bash run.sh
```

![first_step](firststep.gif)

[TAB], [Shift+Tab]キーでフォーカス遷移する。

![startup](startup.png)

指定字数内のみ登録できる

![write_100](write_100.png)

ボタンを押下して登録する。

![write_100_regist.png](write_100_regist.png)

登録後、少しだけ表示されてフェードアウトする。

![write_100_regist_fadeout](write_100_regist_fadeout.png)

`./contents/list.html`ファイルをブラウザで開くと一覧できる。新しい順。

![list_html](list_html.png)

すでにlist.htmlファイルを開いており新たに登録したなら、F5キーでリロードすれば表示が更新される。

# 細かい書式

* タイトルは任意。必須ではない。最大40字まで。

本文は必須。字数は以下の通り。それ以外の字数では登録不可。

規格|最小字数|最大字数|
----|--------|--------|
100字小説|90|100|
200字小説|180|200|
300字小説|270|300|
400字小説|360|400|

最大字数の10%前までOK。ぴったりだと書きにくいので制限を緩くした。規模としての一定の目安。

# 設定

`setting/path.txt`に出力したいディレクトリパスを書く。複数あるなら1行ずつ書く。

# 隠し機能

* 一括ファイル出力
    * `src/export/SingleDirectoryExporter.py`
        * もしファイルを削除してしまった場合、DBにあるデータからファイル出力する

`app.py`にあるとおり以下のように使う。`path.txt`で指定したパスへ出力する。
```python
import src.export.SingleDirectoryExporter
#    exp = src.export.SingleDirectoryExporter.SingleDirectoryExporter(base_path=__base_path)
#    exp.Export()
```

ふつうに使っていたら`path.txt`の指定先へ毎回ファイル作成されるため必要ないと思う。

# 用法

## 解決できる問題

* ファイル作成やファイル名を決めるのが面倒
* 字数をカウントするのが面倒

## 心得

* とにかく文章をアウトプットしてみる
    * 自分の中にあるもの、思いついたものを吐き出す
        * 頭を整理させる
        * 気持ちをスッキリさせる
        * 自分の世界に浸らせる
        * 自己満足に浸らせる
    * とにかく新規に吐き出すことだけをする
        * 編集、修正は一切しない（できない。させない。黒歴史をそのまま残す）
        * 続き物は書かない（1件読み切り）
        * 内容や質は不問（意味不明でも辻褄が合わなくても何でもいい）

文章をアウトプットする練習台。

## 方針

* 規模を小さくすることで量産しやすくする
* ある程度の縛りを設けることで想像力を高める
* ある程度の緩さを持たせて書きづらさを取り除く

想像力を促しつつ、書きやすさの邪魔をしない程度の制約を設けたつもり。

# 課題

* ほかの制約も儲けたい
    * 時間制限
        * 5分以内に400字書け等
    * 目標
        * 起承転結をつけろ等
    * お題
        * もし○○なら等
* 一覧を見やすくしたい
    * 一覧から検索(絞込)できるようにしたい
* 編集できるようにしたい
    * 編集履歴を追えるようにしたい
        * 編集理由を確認できるようにしたい
* 一括ファイル出力できるようにしたい
* GitHub, Mastodonに出力できるようにしたい
* GitHub Pagesでまとめサイトを自動作成したい
* ライセンスについて明記したい
* もっと実行しやすくしたい（Pythonの準備等を排除したい）

# 開発環境

* Linux Mint 17.3 MATE 32bit
* SQLite 3.8.2
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * ローカルサーバ
            * Flask
        * BeautifulSoup
* Firefox 52.0
    * JavaScript
        * JQuery 3.2.1

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[Flask 0.12.2](http://flask.pocoo.org/)|[three clause BSD](http://flask.pocoo.org/docs/0.12/license/#flask-license)|[Copyright (c) 2015 by Armin Ronacher and contributors.](http://flask.pocoo.org/docs/0.12/license/)
[bs4(BeautifulSoup)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)

