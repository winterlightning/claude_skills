"""Apricot slice (food), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22a874a8-34ca-5cfe-927b-6251ffbae66d'
SOURCE_PATH = 'icons-json/food/apricot slice_22a874a8-34ca-5cfe-927b-6251ffbae66d.json'
AUTHOR = 'json_to_solo'

class ApricotSliceFood(Solo48):
    icon_id = 'apricot-slice-food'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('apricot', 'slice', 'food')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (24, 37), (24, 37))
        self.add_line('sym-e3', (24, 11), (25, 11))
        self.add_line('sym-e4', (25, 11), (30, 16))
        self.add_arc('sym-e5', (30, 16), (28, 34), radius_x=14)
        self.add_line('sym-e6', (28, 34), (24, 37))
        self.add_arc('sym-e7', (24, 37), (20, 34), radius_x=17)
        self.add_arc('sym-e8', (20, 34), (18, 16), radius_x=14)
        self.add_arc('sym-e9', (18, 16), (23, 11), radius_x=13)
        self.add_line('sym-e10', (23, 11), (24, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', closed=True)
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
