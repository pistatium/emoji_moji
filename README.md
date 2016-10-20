# EmojiMoji

日本語の文字(4文字まで)をSlackの絵文字として登録するためのツール

## 使い方
```bash
$ python emoji_moji.py なるほど

なるほど.png
https://lmnd.slack.com/admin/emoji に画像を登録してご利用下さい
```

生成された画像をSlackに登録することで絵文字として利用できます。

![なるほど.png](https://github.com/pistatium/emoji_moji/blob/master/sample/%E3%81%AA%E3%82%8B%E3%81%BB%E3%81%A9.png?raw=true)


## セットアップ(MacOSでのみ動作確認済)
```bash
git clone git@github.com:pistatium/emoji_moji.git
cd emoji_moji

# direnvでPython3の環境を作る(別の方法でも良い)
direnv edit .
## エディタが開くので `layout python3` だけ書き込んで保存、閉じる

## 必要なパッケージをインストール
pip install -r requirements.txt
```



