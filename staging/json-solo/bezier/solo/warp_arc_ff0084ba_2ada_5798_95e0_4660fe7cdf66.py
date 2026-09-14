"""Warp arc (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff0084ba-2ada-5798-95e0-4660fe7cdf66'
SOURCE_PATH = 'icons-json/design/warp arc_ff0084ba-2ada-5798-95e0-4660fe7cdf66.json'
AUTHOR = 'json_to_solo'

class WarpArcDesign(Solo48):
    icon_id = 'warp-arc-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arc', 'design')

    def build(self):
        self.add_bezier('sym-e0', (44, 14), ((43.9, 13.877), (44, 14.123), (44, 14)))
        self.add_bezier('sym-e1', (44, 14), ((43.7, 13.791), (43.318, 13.197), (43, 13)))
        self.add_bezier('sym-e2', (43, 13), ((37.736, 9.702), (30.809, 8), (25, 8)))
        self.add_bezier('sym-e3', (25, 8), ((24.733, 8), (24.267, 8), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((23.733, 8), (23.267, 8), (23, 8)))
        self.add_bezier('sym-e5', (23, 8), ((17.191, 8), (10.264, 9.702), (5, 13)))
        self.add_bezier('sym-e6', (5, 13), ((4.682, 13.197), (4.3, 13.791), (4, 14)))
        self.add_bezier('sym-e7', (4, 14), ((4, 14.123), (4.1, 13.877), (4, 14)))
        self.add_line('sym-e8', (4, 14), (14, 40))
        self.add_bezier('sym-e9', (14, 40), ((14.555, 39.606), (13.464, 40), (14, 40)))
        self.add_bezier('sym-e10', (14, 40), ((14.236, 39.852), (14.764, 39.172), (15, 39)))
        self.add_bezier('sym-e11', (15, 39), ((15.809, 38.397), (17.136, 38.443), (18, 38)))
        self.add_bezier('sym-e12', (18, 38), ((19.974, 36.98), (21.819, 36), (24, 36)))
        self.add_bezier('sym-e13', (24, 36), ((26.181, 36), (28.026, 36.98), (30, 38)))
        self.add_bezier('sym-e14', (30, 38), ((30.864, 38.443), (32.191, 38.397), (33, 39)))
        self.add_bezier('sym-e15', (33, 39), ((33.236, 39.172), (33.764, 39.852), (34, 40)))
        self.add_bezier('sym-e16', (34, 40), ((34.536, 40), (33.445, 39.606), (34, 40)))
        self.add_line('sym-e17', (34, 40), (44, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
