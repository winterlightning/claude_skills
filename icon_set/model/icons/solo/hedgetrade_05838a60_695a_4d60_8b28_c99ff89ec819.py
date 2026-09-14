"""Hedgetrade (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05838a60-695a-4d60-8b28-c99ff89ec819'
SOURCE_PATH = 'icons-json/symbol/hedgetrade_05838a60-695a-4d60-8b28-c99ff89ec819.json'
AUTHOR = 'json_to_solo'

class Hedgetrade(Solo48):
    icon_id = 'hedgetrade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hedgetrade', 'symbol')

    def build(self):
        self.add_line('e0', (15, 6), (6, 42))
        self.add_line('e1', (37, 24), (11, 24))
        self.add_line('e2', (42, 6), (33, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
