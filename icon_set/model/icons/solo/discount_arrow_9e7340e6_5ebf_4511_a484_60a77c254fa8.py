"""Discount arrow (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e7340e6-5ebf-4511-a484-60a77c254fa8'
SOURCE_PATH = 'icons-json/shopping/discount arrow_9e7340e6-5ebf-4511-a484-60a77c254fa8.json'
AUTHOR = 'json_to_solo'

class DiscountArrow(Solo48):
    icon_id = 'discount-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('discount', 'arrow', 'shopping')

    def build(self):
        self.add_line('e0', (33, 6), (42, 6))
        self.add_line('e1', (6, 42), (42, 6))
        self.add_line('e2', (42, 15), (42, 6))
        self.add_arc('e3-top', (6, 13), (18, 13), radius_x=6)
        self.add_arc('e3-bottom', (18, 13), (6, 13), radius_x=6)
        self.add_arc('e4-top', (29, 33), (41, 33), radius_x=6)
        self.add_arc('e4-bottom', (41, 33), (29, 33), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
