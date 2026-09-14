"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3034182-8272-438e-bd25-32ee58c63442'
SOURCE_PATH = 'icons-json/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.json'
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
        self.add_line('e0', (8, 24), (8, 9))
        self.add_line('e1', (15, 9), (24, 4))
        self.add_line('e2', (24, 4), (33, 9))
        self.add_line('e3', (37, 9), (40, 8))
        self.add_line('e4-1', (40, 8), (39, 28))
        self.add_arc('e4-2', (39, 28), (24, 44), radius_x=35)
        self.add_arc('e4-3', (24, 44), (8, 24), radius_x=29)
        self.add_line('e5-1', (8, 9), (9, 8))
        self.add_arc('e5-2', (9, 8), (15, 9), radius_x=6, sweep=False)
        self.add_arc('e6', (33, 9), (37, 9), radius_x=3, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5-1', 'e5-2', 'e1', 'e2', 'e6', 'e3', closed=True)
