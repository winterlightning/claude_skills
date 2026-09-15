"""Water bottle glass (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8717b7d0-2a5a-5dcc-9d53-f284ee945681'
SOURCE_PATH = 'pictographic-primitives/drinks/water bottle glass_8717b7d0-2a5a-5dcc-9d53-f284ee945681.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WaterBottleGlass(Solo48):
    icon_id = 'water-bottle-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'bottle', 'glass', 'drinks')

    def build(self):
        self.add_line('e0', (40, 19), (40, 24))
        self.add_line('e1', (8, 18), (8, 22))
        self.add_line('e2', (38, 24), (40, 24))
        self.add_line('e3', (8, 22), (8, 39))
        self.add_line('e4', (15, 44), (33, 44))
        self.add_line('e5', (40, 39), (40, 24))
        self.add_bezier('e6', (18, 4), ((17.175, 4), (15.825, 4), (15, 4)))
        self.add_bezier('e7', (33, 4), ((32.262, 4), (31.138, 4), (30.4, 4)), ((30.4, 4.545), (30.4, 5.091), (30.4, 5.636)), ((30.388, 6.418), (30.314, 7.173), (30.966, 7.836)), ((31.926, 8.8), (33.686, 9.264), (34.966, 9.964)), ((37.748, 11.509), (39.975, 13.718), (39.975, 16.391)), ((39.975, 16.682), (40, 16.973), (40, 17.255)), ((40, 17.691), (40, 18.573), (40, 19)))
        self.add_bezier('e8', (18, 4), ((17.938, 5.045), (18.142, 6.745), (17.243, 7.709)), ((16.295, 8.718), (14.375, 9.173), (13.046, 9.855)), ((10.215, 11.309), (8.025, 13.445), (8.025, 16.091)), ((8.025, 16.455), (8, 16.827), (8, 17.2)), ((8, 17.345), (8, 17.855), (8, 18)))
        self.add_bezier('e9', (8, 22), ((11.766, 21.191), (15.36, 20.682), (19.262, 21.4)), ((21.957, 21.891), (24.086, 23.109), (26.609, 23.864)), ((30.215, 24.936), (34.345, 24.873), (38, 24)))
        self.add_bezier('e10', (8, 39), ((8, 39.427), (8.025, 39.4), (8.025, 39.827)), ((8.025, 42.2), (11.151, 43.982), (14.215, 43.982)), ((14.4, 43.991), (14.597, 43.991), (14.794, 44)), ((14.991, 44), (14.803, 44), (15, 44)))
        self.add_bezier('e11', (33, 44), ((33.468, 44), (33.563, 43.982), (34.031, 43.982)), ((36.726, 43.982), (39.988, 41.909), (39.988, 39.864)), ((39.988, 39.645), (40, 39.427), (40, 39.209)), ((40, 38.982), (40, 39.218), (40, 39)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7', 'e0')
        self.add_contour('c2', 'e8', 'e1')
        self.add_contour('c3', 'e9', 'e2')
        self.add_contour('c4', 'e3', 'e10', 'e4', 'e11', 'e5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
