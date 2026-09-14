"""Car retro (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed61a709-0dae-5f64-b395-d0f1995bb267'
SOURCE_PATH = 'icons-json/transportation/car retro_ed61a709-0dae-5f64-b395-d0f1995bb267.json'
AUTHOR = 'json_to_solo'

class CarRetroTransportation(Solo48):
    icon_id = 'car-retro-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'retro', 'transportation')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (38, 19), (17, 19))
        self.add_line('e2', (17, 19), (19, 13))
        self.add_line('e3', (24, 8), (31, 8))
        self.add_line('e4', (30, 34), (17, 34))
        self.add_line('e5', (30, 19), (30, 8))
        self.add_arc('e6-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_bezier('e8', (42, 34), ((42.573, 34), (44, 33.538), (44, 32.615)), ((44, 30.683), (43.991, 28.751), (43.991, 26.818)), ((43.991, 23.754), (41.736, 19.606), (39.455, 19.077)), ((38.873, 18.942), (38.591, 19), (38, 19)))
        self.add_bezier('e9', (19, 13), ((19.936, 10.883), (21.927, 8), (24, 8)))
        self.add_bezier('e10', (31, 8), ((31.073, 8.012), (31.427, 8.012), (31.5, 8.025)), ((31.927, 8.025), (32.382, 8.234), (32.791, 8.369)), ((35.336, 9.194), (37.5, 11.582), (38.645, 14.757)), ((39.127, 16.074), (38.809, 17.572), (39, 19)))
        self.add_bezier('e11', (20, 19), ((18.791, 18.988), (17.936, 19.052), (16.727, 19.077)), ((14.318, 19.138), (11.991, 19.36), (9.655, 20.16)), ((9.109, 20.345), (8.445, 20.492), (7.945, 20.849)), ((5.5, 22.585), (4.018, 25.797), (4.018, 29.551)), ((4.018, 29.846), (4, 30.129), (4, 30.412)), ((4, 30.415), (4, 30.418), (4, 30.422)), ((4, 30.615), (4.009, 30.809), (4.009, 31.003)), ((4.009, 31.434), (4.209, 31.975), (4.345, 32.345)), ((4.973, 34.117), (6.773, 33.988), (8, 34)))
        self.add_bezier('e12', (44, 31), ((44, 31.406), (44, 32.594), (44, 33)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e2', 'e9', 'e3', 'e10')
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e12')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'e6')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c4', 'c0')
