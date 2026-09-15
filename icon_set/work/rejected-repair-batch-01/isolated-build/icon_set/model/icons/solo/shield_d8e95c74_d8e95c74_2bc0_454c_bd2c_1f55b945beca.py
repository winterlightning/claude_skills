"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd8e95c74-2bc0-454c-bd2c-1f55b945beca'
SOURCE_PATH = 'pictographic-primitives/protection/shield_d8e95c74-2bc0-454c-bd2c-1f55b945beca.svg'
AUTHOR = 'gpt-6'

class ShieldD8e95c74(Solo48):
    icon_id = 'shield-d8e95c74'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (15, 9), (24, 4))
        self.add_line('e1', (24, 4), (33, 9))
        self.add_line('e2', (37, 9), (40, 8))
        self.add_line('e3', (8, 24), (8, 8))
        self.add_line('e4', (40, 21), (8, 21))
        self.add_arc('e5', (8, 8), (15, 9), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e6', (33, 9), (37, 9), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('e7-1', (40, 8), (40, 25))
        self.add_arc('e7-2', (40, 25), (35, 35), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_arc('e7-3', (35, 35), (24, 44), radius_x=36, radius_y=36, large_arc=False, sweep=True)
        self.add_arc('e7-4', (24, 44), (8, 24), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e3', closed=True)
        self.add_contour('c1', 'e4', closed=False)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
