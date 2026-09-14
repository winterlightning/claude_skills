"""Trash (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65adbc02-2e53-460d-8ac2-44fa49dbce5f'
SOURCE_PATH = 'icons-json/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.json'
AUTHOR = 'json_to_solo'

class Trash65adbc02(Solo48):
    icon_id = 'trash-65adbc02'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')

    def build(self):
        self.add_line('e0', (8, 13), (11, 13))
        self.add_line('e1', (40, 13), (37, 13))
        self.add_line('e2', (37, 13), (34, 44))
        self.add_line('e3', (34, 44), (15, 44))
        self.add_line('e4', (15, 44), (11, 13))
        self.add_line('e5', (37, 13), (30, 13))
        self.add_line('e6', (11, 13), (18, 13))
        self.add_line('e7', (18, 13), (18, 8))
        self.add_line('e8', (30, 11), (30, 13))
        self.add_line('e9', (18, 13), (30, 13))
        self.add_line('e10-1', (18, 8), (19, 5))
        self.add_line('e10-2', (19, 5), (23, 4))
        self.add_arc('e10-3', (23, 4), (26, 4), radius_x=22, sweep=False)
        self.add_arc('e10-4', (26, 4), (29, 6), radius_x=4)
        self.add_arc('e10-5', (29, 6), (30, 11), radius_x=12)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e8')
        self.add_contour('c6', 'e9')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
