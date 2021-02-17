Python パッケージを発行してみる。

# chapter1
status: GitHub レポジトリーをinitしてクローンしただけの状態
goal: パッケージの大枠を作る

- 作りたいパッケージの名前を検索する
    - `poetry search wordcloudja`
        - [パッケージ命名規則](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
        - ヒットしないので wordcloudja にする
- poetry project を開始
    - `poetry new wordcloudja`
    - README.rst は削除
    - 他のファイルを移動する
- chapter1 タグの状態になっていることを確認する

# chapter2
goal: 仮想環境の作成とパッケージの install
- poetry 仮想環境を作成
    - `poetry shell`
    - プロジェクトルートに .venv が作成されるので確かめる
- `poetry install`
  - デフォルトで dependencies に入っているパッケージを install
      - pytest や パッケージングに必要なものが install される
  - lock が作成される
- `pytest`
  - ここらで1回テストしてみる
- `poetry add wordcloud mecab-python3 unidic-lite click`
  - 開発に必要なパッケージを全て足す
- 以下のような状態(chapter2 タグの状態)になっていることを確認する

```
.
├── .venv
├── LICENSE
├── README.md
├── poetry.lock
├── pyproject.toml
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   └── test_wordcloudja.py
└── wordcloudja
    ├── __init__.py
    └── __pycache__
```

# chapter3
- `core.py(cli関数のみ)作成して呼び出してみる`
  - `poetry run python wordcloudja/core.py`
  - "this is wordcloudja" と返ってくるはず
- pyproject.toml の `[tool.poetry.scripts]` にコマンドを登録
  - `wordcloudja` が cli になった際のコマンド名称になる
  - `poetry run wordcloudja` を実行する
- `poetry publish --build` でパッケージ化してみる
  - dist ディレクトリが作成され wheel と tar.gz が作成される
- wheel を pip install できることを試す

```
$ cd ../
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install wordcloud-cli/dist/wordcloudja-0.1.0-py3-none-any.whl
$ wordcloudja
```

- chapter3 タグの状態になっていることを確認する

# chapter4
- chapter4の状態を参考に core.py, stopwords.py, wordcloud_app.py を実装する
- data ディレクトリを用意する
    - IPAからフォントとライセンスを入手
    - 青空文庫からサンプルを入手して sample.txt に書き込む
- pyproject.toml に `include = ["data/*"]` を追加
- poetry run python wordcloudja/core.py --target wordcloudja/data/sample.txt --out sample.png
    - sample.png がアウトプットされるので確認する

# chapter5

- git レポジトリーからinstallできるかを確認する
  - `pip install git+https://github.com/nnashiki/wordcloud-cli`
  - `wordcloudja --target sample.txt --out sample.png`

以上です。