"""Refresh (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fd1c079-cf3a-416d-9512-f7ec606bfef0'
SOURCE_PATH = 'icons-json/interface-essential/refresh_2fd1c079-cf3a-416d-9512-f7ec606bfef0.json'
AUTHOR = 'json_to_solo'

class Refresh(Solo48):
    icon_id = 'refresh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('refresh', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 13), (40, 16))
        self.add_line('e1', (40, 6), (40, 16))
        self.add_line('e2', (40, 16), (31, 16))
        self.add_arc('e3-1', (42, 26), (25, 42), radius_x=18)
        self.add_line('e3-2', (25, 42), (18, 41))
        self.add_arc('e3-3', (18, 41), (9, 34), radius_x=19)
        self.add_arc('e3-4', (9, 34), (7, 30), radius_x=18)
        self.add_line('e3-5', (7, 30), (6, 24))
        self.add_arc('e3-6', (6, 24), (24, 6), radius_x=18)
        self.add_arc('e3-7', (24, 6), (37, 13), radius_x=18)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
