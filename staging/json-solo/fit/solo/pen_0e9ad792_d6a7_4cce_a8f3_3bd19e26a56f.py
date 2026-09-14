"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e9ad792-d6a7-4cce-a8f3-3bd19e26a56f'
SOURCE_PATH = 'icons-json/design/pen_0e9ad792-d6a7-4cce-a8f3-3bd19e26a56f.json'
AUTHOR = 'json_to_solo'

class Pen0e9ad792(Solo48):
    icon_id = 'pen-0e9ad792'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (32, 22), (26, 16))
        self.add_line('e1', (42, 13), (17, 38))
        self.add_line('e2', (17, 38), (11, 40))
        self.add_line('e3', (11, 40), (6, 42))
        self.add_line('e4', (6, 42), (8, 35))
        self.add_line('e5', (10, 31), (35, 6))
        self.add_line('e6', (35, 6), (42, 13))
        self.add_arc('e7', (8, 35), (10, 31), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e7', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
