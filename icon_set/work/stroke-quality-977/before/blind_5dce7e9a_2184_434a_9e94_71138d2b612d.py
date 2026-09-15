"""Blind (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Blind(Solo48):
    icon_id = 'blind'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('blind', 'interface-essential')

    def build(self):
        self.add_line('e0', (16, 38), (34, 12))
        self.add_line('e1', (16, 38), (19, 39))
        self.add_line('e2', (36, 13), (31, 10))
        self.add_bezier('e3', (19, 39), ((20.282, 39.578), (22.482, 39.988), (23.827, 39.988)), ((23.935, 39.988), (24.033, 40), (24.14, 40)), ((24.142, 40), (24.144, 40), (24.145, 40)), ((24.436, 40), (24.727, 39.975), (25.018, 39.975)), ((25.9, 39.975), (26.827, 39.717), (27.682, 39.495)), ((32.664, 38.203), (37.064, 34.523), (40.591, 29.674)), ((41.555, 28.357), (42.4, 26.892), (43.209, 25.403)), ((43.473, 24.923), (43.736, 24.431), (44, 23.951)), ((44, 23.946), (44, 23.941), (44, 23.935)), ((44, 23.569), (42.632, 21.26), (42.345, 20.788)), ((41.055, 18.695), (37.791, 13.972), (36, 13)))
        self.add_bezier('e4', (31, 10), ((30.482, 9.717), (30.173, 10.055), (29.645, 9.809)), ((27.7, 8.911), (25.636, 8.012), (23.545, 8.012)), ((23.456, 8), (23.366, 8), (23.286, 8)), ((23.284, 8), (23.283, 8), (23.282, 8)), ((23.091, 8), (22.9, 8.025), (22.718, 8.025)), ((21.736, 8.025), (20.755, 8.332), (19.809, 8.615)), ((15.027, 10.031), (10.691, 13.526), (7.3, 18.277)), ((6.391, 19.545), (5.564, 20.923), (4.791, 22.351)), ((4.527, 22.843), (4.264, 23.323), (4, 23.815)), ((4, 23.821), (4, 23.827), (4, 23.834)), ((4, 24.258), (5.968, 27.318), (6.273, 27.791)), ((8.818, 31.803), (12.227, 36.302), (16, 38)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3', 'e2', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
