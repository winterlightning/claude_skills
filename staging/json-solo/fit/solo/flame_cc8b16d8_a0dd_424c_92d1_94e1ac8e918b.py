"""Flame (fire), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc8b16d8-a0dd-424c-92d1-94e1ac8e918b'
SOURCE_PATH = 'icons-json/fire/flame_cc8b16d8-a0dd-424c-92d1-94e1ac8e918b.json'
AUTHOR = 'json_to_solo'

class FlameCc8b16d8(Solo48):
    icon_id = 'flame-cc8b16d8'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('flame', 'fire')

    def build(self):
        self.add_line('e0', (25, 8), (19, 4))
        self.add_line('e1', (18, 16), (12, 20))
        self.add_line('e2', (28, 35), (25, 32))
        self.add_arc('e3-1', (26, 44), (40, 29), radius_x=16, sweep=False)
        self.add_arc('e3-2', (40, 29), (36, 18), radius_x=19, sweep=False)
        self.add_arc('e3-3', (36, 18), (30, 24), radius_x=8)
        self.add_arc('e3-4', (30, 24), (25, 8), radius_x=14, sweep=False)
        self.add_arc('e4', (19, 4), (18, 16), radius_x=10)
        self.add_arc('e5-1', (12, 20), (8, 30), radius_x=15, sweep=False)
        self.add_arc('e5-2', (8, 30), (21, 44), radius_x=15, sweep=False)
        self.add_arc('e5-3', (21, 44), (24, 28), radius_x=9)
        self.add_arc('e6', (26, 44), (28, 35), radius_x=7, sweep=False)
        self.add_arc('e7-1', (25, 32), (24, 27), radius_x=6)
        self.add_arc('e7-2', (24, 27), (24, 28), radius_x=1)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4', 'e1', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c1', 'e6', 'e2', 'e7-1', 'e7-2')
