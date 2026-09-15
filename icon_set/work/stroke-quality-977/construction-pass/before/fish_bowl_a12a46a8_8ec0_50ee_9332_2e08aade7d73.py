"""Fish bowl (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a12a46a8-8ec0-50ee-9332-2e08aade7d73'
SOURCE_PATH = 'pictographic-primitives/pets/fish bowl_a12a46a8-8ec0-50ee-9332-2e08aade7d73.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FishBowl(Solo48):
    icon_id = 'fish-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('fish', 'bowl', 'pets')

    def build(self):
        self.add_line('e0', (44, 16), (4, 16))
        self.add_line('e1', (18, 25), (20, 28))
        self.add_line('e2', (19, 28), (18, 30))
        self.add_line('e3', (7, 8), (41, 8))
        self.add_bezier('e4', (20, 28), ((22.936, 25.06), (25.445, 23.7), (29.418, 25.7)), ((29.827, 25.9), (32.173, 27.66), (32.182, 27.96)), ((32.191, 28.25), (29.809, 30.08), (29.445, 30.27)), ((25.691, 32.26), (22.027, 30.63), (19, 28)))
        self.add_bezier('e5', (41, 8), ((41.318, 8.13), (41.864, 8.06), (42.127, 8.35)), ((42.964, 9.26), (43.982, 14.35), (43.982, 15.74)), ((43.991, 15.83), (43.991, 15.91), (44, 16)), ((44, 17.02), (43.991, 18.04), (43.991, 19.05)), ((43.991, 28.18), (37.536, 36.52), (29.782, 39.1)), ((28.409, 39.56), (26.836, 39.99), (25.391, 39.99)), ((25.122, 39.99), (24.854, 40), (24.586, 40)), ((24.581, 40), (24.577, 40), (24.573, 40)), ((24.164, 40), (23.755, 39.98), (23.336, 39.98)), ((14.945, 39.98), (7.282, 33.19), (4.855, 24.51)), ((4.436, 23.02), (4.009, 21.31), (4.009, 19.74)), ((4.009, 19.66), (4, 19.57), (4, 19.49)), ((4, 18.33), (4, 17.16), (4, 16)), ((4, 13.18), (5.855, 10.41), (7, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
