"""Love lollipop (romance), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '911ef131-2509-56e7-8de2-02eb51318d04'
SOURCE_PATH = 'icons-json/romance/love lollipop_911ef131-2509-56e7-8de2-02eb51318d04.json'
AUTHOR = 'json_to_solo'

class LoveLollipopRomance(Solo48):
    icon_id = 'love-lollipop-romance'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('love', 'lollipop', 'romance')

    def build(self):
        self.add_line('sym-e0', (24, 27), (24, 44))
        self.add_bezier('sym-e1', (24, 8), ((24.021, 8.024), (23.98, 7.976), (24, 8)))
        self.add_bezier('sym-e2', (24, 8), ((24.012, 8.009), (24.717, 7.336), (25, 7)))
        self.add_bezier('sym-e3', (25, 7), ((25.32, 6.618), (25.618, 6.364), (26, 6)))
        self.add_bezier('sym-e4', (26, 6), ((27.169, 4.882), (29.043, 4), (31, 4)))
        self.add_bezier('sym-e5', (31, 4), ((31.098, 4), (30.914, 4.009), (31, 4)))
        self.add_bezier('sym-e6', (31, 4), ((31.111, 4), (31.889, 4), (32, 4)))
        self.add_bezier('sym-e7', (32, 4), ((36.32, 4), (40, 6.755), (40, 10)))
        self.add_bezier('sym-e8', (40, 10), ((40, 10.218), (40, 10.782), (40, 11)))
        self.add_bezier('sym-e9', (40, 11), ((40, 11.273), (40, 11.727), (40, 12)))
        self.add_bezier('sym-e10', (40, 12), ((40, 14.045), (37.932, 16.573), (36, 18)))
        self.add_line('sym-e11', (36, 18), (24, 27))
        self.add_line('sym-e12', (24, 27), (12, 18))
        self.add_bezier('sym-e13', (12, 18), ((10.068, 16.573), (8, 14.045), (8, 12)))
        self.add_bezier('sym-e14', (8, 12), ((8, 11.727), (8, 11.273), (8, 11)))
        self.add_bezier('sym-e15', (8, 11), ((8, 10.782), (8, 10.218), (8, 10)))
        self.add_bezier('sym-e16', (8, 10), ((8, 6.755), (11.68, 4), (16, 4)))
        self.add_bezier('sym-e17', (16, 4), ((16.111, 4), (16.889, 4), (17, 4)))
        self.add_bezier('sym-e18', (17, 4), ((17.086, 4.009), (16.902, 4), (17, 4)))
        self.add_bezier('sym-e19', (17, 4), ((18.957, 4), (20.831, 4.882), (22, 6)))
        self.add_bezier('sym-e20', (22, 6), ((22.382, 6.364), (22.68, 6.618), (23, 7)))
        self.add_bezier('sym-e21', (23, 7), ((23.283, 7.336), (23.988, 8.009), (24, 8)))
        self.add_bezier('sym-e22', (24, 8), ((24.02, 7.976), (23.979, 8.024), (24, 8)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
