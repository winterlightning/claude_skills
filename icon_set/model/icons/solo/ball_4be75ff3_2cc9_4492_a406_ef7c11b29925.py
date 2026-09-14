"""Ball (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4be75ff3-2cc9-4492-a406-ef7c11b29925'
SOURCE_PATH = 'icons-json/sports/ball_4be75ff3-2cc9-4492-a406-ef7c11b29925.json'
AUTHOR = 'json_to_solo'

class Ball(Solo48):
    icon_id = 'ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('ball', 'sports')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (5, 19), ((8.118, 19.664), (10.309, 22.091), (12.827, 23.936)), ((14.027, 24.818), (15.318, 25.555), (16.482, 26.491)), ((19.2, 28.664), (22.282, 32.355), (23.209, 35.773)), ((23.945, 38.445), (23.836, 41.255), (24, 44)))
        self.add_bezier('e2', (19, 5), ((19.336, 8.3), (20.482, 10.418), (21.973, 13.282)), ((22.882, 15.045), (23.682, 16.809), (24.827, 18.436)), ((28.773, 24.045), (36.336, 27.773), (43, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c1', 'e0')
        self.relate('connect', 'c1', 'e0')
