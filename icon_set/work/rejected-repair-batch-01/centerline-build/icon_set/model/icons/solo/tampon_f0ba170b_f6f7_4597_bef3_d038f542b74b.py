"""Tampon (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0ba170b-f6f7-4597-bef3-d038f542b74b'
SOURCE_PATH = 'pictographic-primitives/health/tampon_f0ba170b-f6f7-4597-bef3-d038f542b74b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Tampon(Solo48):
    icon_id = 'tampon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tampon', 'health')

    def build(self):
        self.add_line('e0', (12, 38), (13, 33))
        self.add_line('e1', (15, 30), (18, 27))
        self.add_line('e2', (16, 19), (29, 6))
        self.add_line('e3', (38, 16), (26, 29))
        self.add_line('e4', (20, 28), (18, 26))
        self.add_arc('e5', (8, 44), (12, 38), radius_x=10, sweep=False)
        self.add_line('e6', (13, 33), (15, 30))
        self.add_arc('e7', (18, 27), (18, 26), radius_x=28)
        self.add_arc('e8', (18, 26), (16, 19), radius_x=5)
        self.add_arc('e9-1', (29, 6), (34, 4), radius_x=8)
        self.add_arc('e9-2', (34, 4), (38, 6), radius_x=5)
        self.add_line('e9-3', (38, 6), (40, 11))
        self.add_arc('e9-4', (40, 11), (38, 16), radius_x=8)
        self.add_arc('e10', (26, 29), (20, 28), radius_x=4)
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7')
        self.add_contour('c1', 'e8', 'e2', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e3', 'e10', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
