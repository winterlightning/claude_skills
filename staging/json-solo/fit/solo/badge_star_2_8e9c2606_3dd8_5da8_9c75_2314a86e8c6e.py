"""Badge star 2 (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9c2606-3dd8-5da8-9c75-2314a86e8c6e'
SOURCE_PATH = 'icons-json/protection/badge star 2_8e9c2606-3dd8-5da8-9c75-2314a86e8c6e.json'
AUTHOR = 'json_to_solo'

class BadgeStar2Protection(Solo48):
    icon_id = 'badge-star-2-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'star', 'protection')

    def build(self):
        self.add_line('e0', (24, 4), (21, 7))
        self.add_line('e1', (8, 12), (8, 23))
        self.add_line('e2', (40, 23), (40, 11))
        self.add_line('e3', (39, 9), (34, 9))
        self.add_line('e4', (27, 20), (24, 13))
        self.add_line('e5', (24, 13), (21, 20))
        self.add_line('e6', (21, 20), (14, 20))
        self.add_line('e7', (14, 20), (20, 25))
        self.add_line('e8', (20, 25), (18, 32))
        self.add_line('e9', (18, 32), (24, 28))
        self.add_line('e10', (24, 28), (30, 32))
        self.add_line('e11', (30, 32), (28, 25))
        self.add_line('e12', (28, 25), (34, 20))
        self.add_line('e13', (34, 20), (27, 20))
        self.add_line('e14-1', (21, 7), (9, 10))
        self.add_arc('e14-2', (9, 10), (8, 11), radius_x=1, sweep=False)
        self.add_line('e14-3', (8, 11), (8, 12))
        self.add_arc('e15-1', (8, 23), (24, 44), radius_x=25, sweep=False)
        self.add_arc('e15-2', (24, 44), (40, 23), radius_x=24, sweep=False)
        self.add_line('e16', (40, 11), (39, 9))
        self.add_line('e17', (34, 9), (24, 4))
        self.add_contour('c0', 'e0', 'e14-1', 'e14-2', 'e14-3', 'e1', 'e15-1', 'e15-2', 'e2', 'e16', 'e3', 'e17', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', closed=True)
