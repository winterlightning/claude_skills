"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a36c569-3305-4077-ab3c-e8e178a28776'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_7a36c569-3305-4077-ab3c-e8e178a28776.json'
AUTHOR = 'json_to_solo'

class Megaphone7a36c569(Solo48):
    icon_id = 'megaphone-7a36c569'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 31), (8, 39))
        self.add_line('e1', (8, 39), (6, 33))
        self.add_line('e2', (6, 33), (31, 6))
        self.add_line('e3', (31, 6), (42, 31))
        self.add_arc('e4-1', (26, 35), (21, 42), radius_x=6)
        self.add_arc('e4-2', (21, 42), (15, 37), radius_x=8)
        self.add_contour('c0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
