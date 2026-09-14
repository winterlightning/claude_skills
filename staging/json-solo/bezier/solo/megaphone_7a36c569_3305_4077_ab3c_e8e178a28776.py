"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a36c569-3305-4077-ab3c-e8e178a28776'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_7a36c569-3305-4077-ab3c-e8e178a28776.json'
AUTHOR = 'json_to_solo'

class Megaphone(Solo48):
    icon_id = 'megaphone'
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
        self.add_bezier('e4', (26, 35), ((26.016, 36.145), (25.8, 37.083), (25.448, 38.204)), ((24.9, 39.979), (23.026, 41.984), (21.038, 41.984)), ((20.981, 41.992), (20.924, 41.992), (20.875, 42)), ((20.874, 42), (20.873, 42), (20.872, 42)), ((20.824, 42), (20.784, 41.992), (20.735, 41.992)), ((18.207, 41.992), (16.309, 38.735), (15, 37)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
