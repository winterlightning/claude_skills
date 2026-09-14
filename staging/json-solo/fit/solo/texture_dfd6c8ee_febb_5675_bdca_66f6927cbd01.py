"""Texture (nature), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfd6c8ee-febb-5675-bdca-66f6927cbd01'
SOURCE_PATH = 'icons-json/nature/texture_dfd6c8ee-febb-5675-bdca-66f6927cbd01.json'
AUTHOR = 'json_to_solo'

class TextureNature(Solo48):
    icon_id = 'texture-nature'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('texture', 'nature')

    def build(self):
        self.add_line('e0-1', (6, 8), (12, 6))
        self.add_line('e0-2', (12, 6), (17, 8))
        self.add_line('e0-3', (17, 8), (20, 9))
        self.add_arc('e0-4', (20, 9), (26, 6), radius_x=8)
        self.add_line('e0-5', (26, 6), (30, 8))
        self.add_arc('e0-6', (30, 8), (34, 8), radius_x=3, sweep=False)
        self.add_line('e0-7', (34, 8), (39, 6))
        self.add_arc('e0-8', (39, 6), (42, 7), radius_x=5)
        self.add_arc('e1-1', (6, 20), (10, 18), radius_x=7, sweep=False)
        self.add_arc('e1-2', (10, 18), (13, 17), radius_x=6)
        self.add_line('e1-3', (13, 17), (19, 20))
        self.add_arc('e1-4', (19, 20), (23, 18), radius_x=6, sweep=False)
        self.add_arc('e1-5', (23, 18), (30, 19), radius_x=6)
        self.add_line('e1-6', (30, 19), (33, 20))
        self.add_arc('e1-7', (33, 20), (39, 17), radius_x=9)
        self.add_line('e1-8', (39, 17), (42, 18))
        self.add_arc('e2-1', (6, 31), (15, 29), radius_x=8)
        self.add_arc('e2-2', (15, 29), (19, 31), radius_x=9, sweep=False)
        self.add_line('e2-3', (19, 31), (26, 28))
        self.add_line('e2-4', (26, 28), (32, 31))
        self.add_line('e2-5', (32, 31), (39, 28))
        self.add_arc('e2-6', (39, 28), (42, 29), radius_x=5)
        self.add_arc('e3-1', (6, 42), (10, 40), radius_x=7, sweep=False)
        self.add_line('e3-2', (10, 40), (13, 39))
        self.add_line('e3-3', (13, 39), (19, 42))
        self.add_arc('e3-4', (19, 42), (23, 40), radius_x=6, sweep=False)
        self.add_arc('e3-5', (23, 40), (28, 40), radius_x=5)
        self.add_line('e3-6', (28, 40), (32, 42))
        self.add_arc('e3-7', (32, 42), (37, 40), radius_x=8, sweep=False)
        self.add_arc('e3-8', (37, 40), (42, 40), radius_x=5)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8')
