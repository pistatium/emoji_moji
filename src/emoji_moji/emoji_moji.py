# coding: utf-8

import sys
import os

from PIL import Image, ImageDraw, ImageFont


FONT_PATH = os.environ.get("FONT_PATH", "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc")


class EmojiMoji():

    def __init__(self, canvas_size=128, text_color='#020011'):
        self.canvas_size = canvas_size
        self.text_color = text_color
        self.canvas = self._get_canvas()

    def draw(self, text: str) -> 'EmojiMoji':
        str_size = len(text)
        font = self._get_font()
        drawer = ImageDraw.Draw(self.canvas)
        drawer.text((0, 0), text[:str_size//2], font=font, fill=self.text_color)
        drawer.text((0, self.canvas_size/2), text[str_size//2:], font=font, fill=self.text_color)
        return self

    def get_canvas(self) -> Image:
        return self.canvas

    def save(self, path: str, file_name: str) -> str:
        write_to = os.path.join(path, file_name)
        self.canvas.save(write_to, 'PNG')
        return write_to

    def _get_canvas(self) -> Image:
        return Image.new('RGBA', (self.canvas_size, self.canvas_size), (0, 0, 0, 0))

    def _get_font(self) -> ImageFont:
        # FIXME: 4文字以外に対応
        return ImageFont.truetype(FONT_PATH, self.canvas_size//2)

