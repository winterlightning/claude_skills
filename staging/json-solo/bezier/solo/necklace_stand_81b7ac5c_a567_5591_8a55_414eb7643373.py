"""Batch-02/necklace stand (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81b7ac5c-a567-5591-8a55-414eb7643373'
SOURCE_PATH = 'icons-json/accessories/batch-02/necklace stand_81b7ac5c-a567-5591-8a55-414eb7643373.json'
AUTHOR = 'json_to_solo'

class Batch02NecklaceStand(Solo48):
    icon_id = 'batch-02-necklace-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'stand', 'accessories')

    def build(self):
        self.add_line('e0', (35, 35), (40, 28))
        self.add_line('e1', (42, 26), (42, 17))
        self.add_line('e2', (30, 6), (18, 6))
        self.add_line('e3', (6, 17), (6, 24))
        self.add_line('e4', (8, 29), (15, 35))
        self.add_line('e5', (38, 42), (10, 42))
        self.add_bezier('e6', (30, 42), ((30.327, 39.905), (30.832, 38.138), (32.427, 36.706)), ((33.18, 36.019), (34.321, 35.777), (35, 35)))
        self.add_bezier('e7', (40, 28), ((40.573, 27.345), (42, 26.982), (42, 26)))
        self.add_bezier('e8', (42, 17), ((42, 16.632), (41.853, 16.743), (41.689, 16.415)), ((40.887, 14.804), (38.915, 15.229), (37.467, 14.885)), ((36.363, 14.615), (35.258, 14.026), (34.432, 13.241)), ((33.376, 12.226), (32.501, 10.762), (32.215, 9.322)), ((31.895, 7.767), (32.054, 6), (30, 6)))
        self.add_bezier('e9', (18, 6), ((17.943, 6.008), (18.15, 6.008), (18.093, 6.016)), ((17.381, 6.016), (16.62, 6.63), (16.334, 7.252)), ((16.031, 7.898), (15.974, 8.716), (15.81, 9.404)), ((15.507, 10.713), (14.795, 11.899), (13.912, 12.889)), ((12.897, 14.035), (11.465, 14.894), (9.952, 15.155)), ((8.037, 15.491), (7.473, 15.454), (6, 17)))
        self.add_bezier('e10', (6, 24), ((6, 24.417), (6.008, 24.843), (6.008, 25.26)), ((6.008, 26.602), (7.002, 28.116), (8, 29)))
        self.add_bezier('e11', (15, 35), ((16.923, 36.71), (17.517, 39.529), (18, 42)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11')
        self.add_contour('c1', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
