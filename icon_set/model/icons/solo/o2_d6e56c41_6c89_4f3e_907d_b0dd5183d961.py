"""O2 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e56c41-6c89-4f3e-907d-b0dd5183d961'
SOURCE_PATH = 'icons-json/symbol/O2_d6e56c41-6c89-4f3e-907d-b0dd5183d961.json'
AUTHOR = 'json_to_solo'

class O2(Solo48):
    icon_id = 'o2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('o2', 'symbol')

    def build(self):
        self.add_line('e0', (41, 24), (29, 40))
        self.add_line('e1', (29, 40), (44, 40))
        self.add_line('e2', (19, 31), (19, 16))
        self.add_line('e3', (4, 17), (4, 31))
        self.add_arc('e4-1', (30, 14), (37, 8), radius_x=9)
        self.add_arc('e4-2', (37, 8), (42, 11), radius_x=6)
        self.add_line('e4-3', (42, 11), (44, 16))
        self.add_arc('e4-4', (44, 16), (41, 24), radius_x=13)
        self.add_arc('e5-1', (4, 31), (6, 37), radius_x=11, sweep=False)
        self.add_arc('e5-2', (6, 37), (11, 40), radius_x=6, sweep=False)
        self.add_arc('e5-3', (11, 40), (19, 31), radius_x=9, sweep=False)
        self.add_arc('e6-1', (19, 16), (11, 8), radius_x=8, sweep=False)
        self.add_arc('e6-2', (11, 8), (6, 11), radius_x=6, sweep=False)
        self.add_arc('e6-3', (6, 11), (4, 17), radius_x=10, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e1')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', closed=True)
