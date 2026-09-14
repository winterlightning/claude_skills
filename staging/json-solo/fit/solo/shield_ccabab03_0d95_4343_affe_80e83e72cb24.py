"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccabab03-0d95-4343-affe-80e83e72cb24'
SOURCE_PATH = 'icons-json/protection/shield_ccabab03-0d95-4343-affe-80e83e72cb24.json'
AUTHOR = 'json_to_solo'

class Shield(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (8, 9), (12, 4))
        self.add_line('e1', (12, 4), (18, 8))
        self.add_line('e2', (18, 8), (24, 4))
        self.add_line('e3', (24, 4), (30, 8))
        self.add_line('e4', (30, 8), (36, 4))
        self.add_line('e5', (36, 4), (39, 9))
        self.add_line('e6', (37, 19), (39, 23))
        self.add_line('e7', (10, 23), (11, 19))
        self.add_arc('e8', (39, 9), (37, 19), radius_x=10, sweep=False)
        self.add_line('e9-1', (39, 23), (40, 27))
        self.add_arc('e9-2', (40, 27), (24, 44), radius_x=21)
        self.add_arc('e9-3', (24, 44), (8, 29), radius_x=22)
        self.add_arc('e9-4', (8, 29), (10, 23), radius_x=13)
        self.add_arc('e10', (11, 19), (8, 9), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e8', 'e6', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e7', 'e10', closed=True)
