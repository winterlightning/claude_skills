"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e1100ca-39fe-4e71-b978-93997ec5e7d8'
SOURCE_PATH = 'icons-json/protection/shield_8e1100ca-39fe-4e71-b978-93997ec5e7d8.json'
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
        self.add_line('e0', (40, 10), (34, 9))
        self.add_line('e1', (34, 9), (28, 6))
        self.add_line('e2', (28, 6), (24, 4))
        self.add_line('e3', (24, 4), (13, 9))
        self.add_line('e4', (13, 9), (8, 10))
        self.add_line('e5-1', (8, 10), (9, 24))
        self.add_arc('e5-2', (9, 24), (11, 31), radius_x=32, sweep=False)
        self.add_arc('e5-3', (11, 31), (24, 44), radius_x=25, sweep=False)
        self.add_arc('e5-4', (24, 44), (36, 33), radius_x=24, sweep=False)
        self.add_arc('e5-5', (36, 33), (40, 17), radius_x=39, sweep=False)
        self.add_arc('e5-6', (40, 17), (40, 10), radius_x=22)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', closed=True)
