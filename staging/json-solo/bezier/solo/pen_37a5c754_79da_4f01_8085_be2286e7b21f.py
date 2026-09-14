"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37a5c754-79da-4f01-8085-be2286e7b21f'
SOURCE_PATH = 'icons-json/design/pen_37a5c754-79da-4f01-8085-be2286e7b21f.json'
AUTHOR = 'json_to_solo'

class Pen37a5c754(Solo48):
    icon_id = 'pen-37a5c754'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (14, 21), (8, 36))
        self.add_line('e1', (8, 36), (6, 42))
        self.add_line('e2', (26, 35), (12, 41))
        self.add_line('e3', (12, 41), (6, 42))
        self.add_line('e4', (6, 42), (24, 24))
        self.add_line('e5', (31, 17), (42, 6))
        self.add_bezier('e6', (31, 17), ((29.83, 16.403), (28.173, 15.36), (26.88, 15.041)), ((21.955, 13.83), (16.045, 16.14), (14, 21)))
        self.add_bezier('e7', (31, 17), ((32.465, 18.972), (33.344, 20.596), (33.794, 23.067)), ((34.505, 27.011), (32.337, 31.012), (29.13, 33.245)), ((28.287, 33.835), (26.933, 34.583), (26, 35)))
        self.add_contour('c0', 'e6', 'e0', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
