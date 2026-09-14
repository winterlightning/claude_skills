"""Donut (food), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00d20722-d108-5525-bcb7-9983d0a9df63'
SOURCE_PATH = 'icons-json/food/donut_00d20722-d108-5525-bcb7-9983d0a9df63.json'
AUTHOR = 'json_to_solo'

class Donut(Solo48):
    icon_id = 'donut'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('donut', 'food')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (15, 24), (33, 24), radius_x=9)
        self.add_arc('sym-e3', (33, 24), (15, 24), radius_x=9)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
