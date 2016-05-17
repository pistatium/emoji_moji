# coding: utf-8

import sys
import os

from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver


class EmojiMoji():
    CANVAS_SIZE = 128
    FONT_SIZE = 64
    FONT_PATH = '/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc'

    def __init__(self):
        self.canvas = self._get_canvas()

    def draw(self, text: str) -> 'EmojiMoji':
        font = self._get_font()
        drawer = ImageDraw.Draw(self.canvas)
        drawer.text((0, 0), text[:2], font=font, fill='#020011')
        drawer.text((0, 64), text[2:4], font=font, fill='#020011')
        return self

    def get_canvas(self) -> Image:
        return self.canvas

    def save(self, path: str, file_name: str) -> str:
        write_to = os.path.join(path, file_name)
        self.canvas.save(write_to, 'PNG')
        return write_to

    def _get_canvas(self):
        return Image.new('RGBA', (self.CANVAS_SIZE, self.CANVAS_SIZE), (0, 0, 0, 0))

    def _get_font(self):
        return ImageFont.truetype(self.FONT_PATH, self.FONT_SIZE)

def get_profile_path(prof='default'):
    profile_dir = '{}/Library/Application Support/Firefox/Profiles/'.format(os.environ['HOME'])
    files = os.listdir(profile_dir)
    profile_name = [fname for fname in files if fname.endswith(prof)][0]
    return os.path.join(profile_dir, profile_name)

def main():

    params = sys.argv
    if len(params) != 3:
        print("[使い方 例]: python {} なるほど nrhd".format(params[0]))
        return
    text = params[1]
    alias = params[2]
    path = EmojiMoji().draw(text).save(os.path.dirname(os.path.abspath(__file__)), '{}.png'.format(alias))

    profile = webdriver.FirefoxProfile(get_profile_path())
    browser = webdriver.Firefox(profile)
    browser.get('https://slack.com/admin/emoji')
    browser.find_element_by_id('emojiname').send_keys(alias)
    browser.find_element_by_id('emojiimg').send_keys(path)
    form = browser.find_element_by_id('addemoji')
    submit = [tag for tag in form.find_elements_by_tag_name('input') if tag.get_attribute('type') == 'submit'][0]
    submit.submit()
    browser.close()
    print(":{}: と打てば絵文字が使えるはず!".format(alias))
     

if __name__ == '__main__':
    main()
