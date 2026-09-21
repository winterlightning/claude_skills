"""Fm (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a51617-1848-4fd3-a632-11bc61dcc756'
SOURCE_PATH = 'icons-json/symbol/fm (text u)_82a51617-1848-4fd3-a632-11bc61dcc756.json'
AUTHOR = 'json_to_solo'

class FmTextU(Solo48):
    icon_id = 'fm-text-u'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fm', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (6, 14), (14, 14))
        self.add_line('e1', (6, 26), (6, 7))
        self.add_line('e2', (7, 6), (17, 6))
        self.add_line('e3', (24, 13), (24, 26))
        self.add_line('e4', (33, 17), (33, 26))
        self.add_line('e5', (42, 17), (42, 26))
        self.add_line('e6', (6, 42), (42, 42))
        self.add_arc('e7', (6, 7), (7, 6), radius_x=1)
        self.add_arc('e8-1', (24, 17), (31, 14), radius_x=5)
        self.add_arc('e8-2', (31, 14), (33, 17), radius_x=3)
        self.add_arc('e9', (33, 17), (42, 17), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e8-1', 'e8-2', 'e4')
        self.add_contour('c4', 'e9', 'e5')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c3')
