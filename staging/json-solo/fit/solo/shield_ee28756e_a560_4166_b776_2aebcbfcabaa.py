"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee28756e-a560-4166-b776-2aebcbfcabaa'
SOURCE_PATH = 'icons-json/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.json'
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
        self.add_line('e0', (38, 7), (32, 5))
        self.add_line('e1', (16, 6), (10, 8))
        self.add_line('e2', (8, 9), (8, 25))
        self.add_line('e3', (40, 26), (40, 8))
        self.add_line('e4', (40, 8), (38, 7))
        self.add_line('e5-1', (32, 5), (25, 4))
        self.add_line('e5-2', (25, 4), (16, 6))
        self.add_arc('e6', (10, 8), (8, 9), radius_x=2, sweep=False)
        self.add_arc('e7-1', (8, 25), (24, 44), radius_x=22, sweep=False)
        self.add_arc('e7-2', (24, 44), (40, 26), radius_x=22, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6', 'e2', 'e7-1', 'e7-2', 'e3', 'e4', closed=True)
