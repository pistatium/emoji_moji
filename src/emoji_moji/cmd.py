# coding: utf-8

import sys
import os

from PIL import Image, ImageDraw, ImageFont
from .emoji_moji import EmojiMoji


def main():
    params = sys.argv
    if len(params) != 2:
        print("[使い方 例]: python {} なるほど".format(params[0]))
        return
    text = params[1]
    EmojiMoji().draw(text).save(os.getcwd(), '{}.png'.format(text))
    print("{}.png".format(text))
    print("https://slack.com/admin/emoji に画像を登録してご利用下さい")
     

if __name__ == '__main__':
    main()
