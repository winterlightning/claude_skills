"""Sliced pie (business), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffd66227-1225-4049-b2a4-f8abe7a156c5'
SOURCE_PATH = 'icons-json/business/sliced pie_ffd66227-1225-4049-b2a4-f8abe7a156c5.json'
AUTHOR = 'json_to_solo'

class SlicedPieBusiness(Solo48):
    icon_id = 'sliced-pie-business'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('sliced', 'pie', 'business')

    def build(self):
        self.add_line('e0', (31, 24), (44, 24))
        self.add_line('e1', (10, 38), (19, 29))
        self.add_line('e2', (24, 17), (24, 4))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e4-top', (17, 24), (31, 24), radius_x=7)
        self.add_arc('e4-bottom', (31, 24), (17, 24), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e3')
