"""Phone with down arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14b5fcaa-27a4-4bd9-8940-7690a86b2fe1'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PhoneWithDownArrow(Solo48):
    icon_id = 'phone-with-down-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'with', 'down', 'arrow', 'symbol')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (42, 6), (31, 18))
        self.add_line('e1', (31, 18), (40, 18))
        self.add_line('e2', (31, 8), (31, 18))
        self.add_line('e3', (35, 31), (39, 34))
        self.add_line('e4', (13, 7), (17, 11))
        self.add_line('e5', (17, 16), (10, 22))
        self.add_bezier('e6', (24, 37), ((25.751, 35.38), (27.371, 33.72), (29.007, 31.985)), ((31.233, 29.637), (31.981, 27.981), (35, 31)))
        self.add_bezier('e7', (39, 34), ((40.915, 35.915), (38.924, 37.991), (37.639, 39.57)), ((36.919, 40.462), (36.142, 41.444), (35.005, 41.828)), ((34.587, 41.967), (34.055, 41.992), (33.622, 41.992)), ((33.541, 41.992), (33.461, 42), (33.38, 42)), ((29.997, 42), (26.43, 39.194), (24, 37.091)), ((18.895, 32.673), (13.994, 27.911), (10.091, 22.364)), ((8.414, 19.975), (6.008, 16.145), (6.008, 13.184)), ((6, 13.103), (6, 13.015), (6, 12.934)), ((6, 12.693), (6.016, 12.455), (6.016, 12.218)), ((6.016, 11.277), (6.327, 10.353), (6.851, 9.575)), ((7.53, 8.577), (10.075, 6), (11.359, 6)), ((12.177, 6.008), (12.534, 6.534), (13, 7)))
        self.add_bezier('e8', (17, 11), ((18.481, 12.481), (18.031, 14.462), (17, 16)))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', closed=False)
