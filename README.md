# EmojiMoji

文字を絵文字として登録するためのツール

## 使い方
```bash
python emoji_moji.py なるほど nrhd
```
→ slackで :nrhd:と打つと「なるほど」な絵文字が表示される
 
## セットアップ(MacOSのみ)
```bash
git clone git@github.com:pistatium/emoji_moji.git
cd emoji_moji

# direnvでPython3の環境を作る(別の方法でも良い)
direnv edit .
## エディタが開くので `layout python3` だけ書き込んで保存、閉じる

## 必要なパッケージをインストール
pip install -r requirements.txt

## Firefoxで絵文字を使いたいSlackにログインしておく
```


