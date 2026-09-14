"""Nested sliced pie (business), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fb0aac2-8039-5f1f-ac53-9e78b33bb7d4'
SOURCE_PATH = 'icons-json/business/nested sliced pie_0fb0aac2-8039-5f1f-ac53-9e78b33bb7d4.json'
AUTHOR = 'json_to_solo'

class NestedSlicedPieBusiness(Solo48):
    icon_id = 'nested-sliced-pie-business'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('nested', 'sliced', 'pie', 'business')

    def build(self):
        self.add_line('e0', (24, 32), (24, 44))
        self.add_line('e1', (19, 30), (10, 38))
        self.add_line('e2', (16, 24), (4, 24))
        self.add_line('e3', (18, 19), (10, 10))
        self.add_line('e4', (38, 10), (30, 19))
        self.add_line('e5', (24, 4), (24, 16))
        self.add_arc('e6-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e6-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_arc('e7-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e7-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c2', 'e7')
        self.relate('connect', 'c3', 'e6')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c4', 'e7')
        self.relate('connect', 'c4', 'e6')
        self.relate('connect', 'c5', 'e7')
        self.relate('connect', 'c5', 'e6')
