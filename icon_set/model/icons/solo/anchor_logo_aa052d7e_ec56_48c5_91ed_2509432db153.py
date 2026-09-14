"""Anchor logo (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa052d7e-ec56-48c5-91ed-2509432db153'
SOURCE_PATH = 'icons-json/_uncategorized_03/anchor logo_aa052d7e-ec56-48c5-91ed-2509432db153.json'
AUTHOR = 'json_to_solo'

class AnchorLogo(Solo48):
    icon_id = 'anchor-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('anchor', 'logo', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (18, 19), (24, 19))
        self.add_line('e1', (13, 31), (8, 26))
        self.add_line('e2', (6, 31), (8, 26))
        self.add_line('e3', (42, 31), (40, 26))
        self.add_line('e4', (35, 31), (40, 26))
        self.add_line('e5', (30, 19), (24, 19))
        self.add_line('e6', (24, 15), (24, 19))
        self.add_line('e7', (24, 42), (24, 19))
        self.add_arc('e8-top', (20, 10), (28, 10), radius_x=4)
        self.add_arc('e8-bottom', (28, 10), (20, 10), radius_x=4)
        self.add_line('e9', (24, 14), (24, 15))
        self.add_arc('e10', (24, 42), (8, 26), radius_x=16)
        self.add_arc('e11', (24, 42), (40, 26), radius_x=16, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e9', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c6', 'e8')
