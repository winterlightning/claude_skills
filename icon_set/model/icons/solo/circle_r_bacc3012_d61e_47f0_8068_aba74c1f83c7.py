"""Circle r (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bacc3012-d61e-47f0-8068-aba74c1f83c7'
SOURCE_PATH = 'icons-json/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.json'
AUTHOR = 'json_to_solo'

class CircleR(Solo48):
    icon_id = 'circle-r'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'r', 'state')

    def build(self):
        self.add_line('e0', (19, 34), (19, 24))
        self.add_line('e1', (30, 34), (26, 24))
        self.add_line('e2', (26, 24), (19, 24))
        self.add_line('e3', (26, 14), (19, 14))
        self.add_line('e4', (19, 14), (19, 24))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e6-1', (27, 24), (31, 19), radius_x=5, sweep=False)
        self.add_arc('e6-2', (31, 19), (26, 14), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e3', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
