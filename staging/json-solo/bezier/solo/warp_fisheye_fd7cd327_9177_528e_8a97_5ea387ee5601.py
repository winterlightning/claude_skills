"""Warp fisheye (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd7cd327-9177-528e-8a97-5ea387ee5601'
SOURCE_PATH = 'icons-json/design/warp fisheye_fd7cd327-9177-528e-8a97-5ea387ee5601.json'
AUTHOR = 'json_to_solo'

class WarpFisheyeDesign(Solo48):
    icon_id = 'warp-fisheye-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'fisheye', 'design')

    def build(self):
        self.add_arc('sym-e0', (13, 24), (35, 24), radius_x=11)
        self.add_arc('sym-e1', (35, 24), (13, 24), radius_x=11)
        self.add_line('sym-e2', (6, 24), (6, 8))
        self.add_bezier('sym-e3', (6, 8), ((6, 7.877), (6, 8.115), (6, 8)))
        self.add_bezier('sym-e4', (6, 8), ((6, 7.075), (7.018, 6), (8, 6)))
        self.add_bezier('sym-e5', (8, 6), ((8.196, 6), (7.812, 6), (8, 6)))
        self.add_line('sym-e6', (8, 6), (40, 6))
        self.add_bezier('sym-e7', (40, 6), ((40.123, 6), (39.869, 6), (40, 6)))
        self.add_bezier('sym-e8', (40, 6), ((40.589, 6), (42, 6.28), (42, 7)))
        self.add_bezier('sym-e9', (42, 7), ((42, 7.352), (42, 7.648), (42, 8)))
        self.add_line('sym-e10', (42, 8), (42, 24))
        self.add_line('sym-e11', (42, 24), (42, 40))
        self.add_bezier('sym-e12', (42, 40), ((42, 40.352), (42, 40.648), (42, 41)))
        self.add_bezier('sym-e13', (42, 41), ((42, 41.72), (40.589, 42), (40, 42)))
        self.add_bezier('sym-e14', (40, 42), ((39.869, 42), (40.123, 42), (40, 42)))
        self.add_line('sym-e15', (40, 42), (8, 42))
        self.add_bezier('sym-e16', (8, 42), ((7.812, 42), (8.196, 42), (8, 42)))
        self.add_bezier('sym-e17', (8, 42), ((7.018, 42), (6, 40.925), (6, 40)))
        self.add_bezier('sym-e18', (6, 40), ((6, 39.885), (6, 40.123), (6, 40)))
        self.add_line('sym-e19', (6, 40), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
