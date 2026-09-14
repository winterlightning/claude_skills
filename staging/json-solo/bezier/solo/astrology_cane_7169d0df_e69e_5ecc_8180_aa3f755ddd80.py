"""Batch-06/astrology cane (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7169d0df-e69e-5ecc-8180-aa3f755ddd80'
SOURCE_PATH = 'icons-json/culture/batch-06/astrology cane_7169d0df-e69e-5ecc-8180-aa3f755ddd80.json'
AUTHOR = 'json_to_solo'

class Batch06AstrologyCane(Solo48):
    icon_id = 'batch-06-astrology-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'cane', 'culture')

    def build(self):
        self.add_line('e0', (23, 9), (8, 44))
        self.add_bezier('e1', (38, 17), ((38.66, 15.6), (39.99, 13.182), (39.99, 11.5)), ((40, 11.428), (40, 11.357), (40, 11.277)), ((40, 11.275), (40, 11.274), (40, 11.273)), ((40, 11.118), (39.98, 10.973), (39.98, 10.818)), ((39.98, 10.082), (39.65, 9.391), (39.33, 8.736)), ((38.01, 6.018), (35.06, 4), (31.68, 4)), ((31.676, 4), (31.673, 4), (31.669, 4)), ((31.443, 4), (31.206, 4.009), (30.98, 4.009)), ((27.02, 4.009), (24.39, 5.791), (23, 9)))
        self.add_contour('c0', 'e1', 'e0')
