"""Warp flag (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31055c7d-f823-51b5-a0be-5eb87af6158d'
SOURCE_PATH = 'pictographic-primitives/design/warp flag_31055c7d-f823-51b5-a0be-5eb87af6158d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WarpFlag(Solo48):
    icon_id = 'warp-flag'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'flag', 'design')

    def build(self):
        self.add_line('e0', (26, 26), (20, 22))
        self.add_line('e1', (44, 10), (44, 34))
        self.add_line('e2', (26, 38), (20, 35))
        self.add_line('e3', (4, 37), (4, 13))
        self.add_line('e4', (22, 11), (26, 13))
        self.add_bezier('e5', (44, 22), ((43.882, 22.101), (43.873, 22.611), (43.745, 22.703)), ((43.527, 22.855), (43.255, 22.914), (43.027, 23.057)), ((41.536, 24.008), (40.309, 25.221), (38.727, 26.055)), ((35.055, 27.983), (31.627, 28.253), (27.773, 26.602)), ((27.127, 26.324), (26.6, 26.371), (26, 26)))
        self.add_bezier('e6', (20, 22), ((18.845, 21.284), (17.691, 21.069), (16.345, 20.808)), ((11.318, 19.832), (7.845, 22.347), (4, 25)))
        self.add_bezier('e7', (44, 34), ((43.991, 34.084), (43.991, 34.265), (43.982, 34.349)), ((43.982, 35.192), (42.645, 35.941), (42.045, 36.404)), ((40.273, 37.785), (36.882, 39.992), (34.473, 39.992)), ((34.267, 39.992), (34.052, 40), (33.837, 40)), ((33.834, 40), (33.831, 40), (33.827, 40)), ((32.891, 40), (31.955, 39.983), (31.018, 39.983)), ((29.282, 39.983), (27.427, 38.884), (26, 38)))
        self.add_bezier('e8', (20, 35), ((19.382, 34.621), (18.945, 34.316), (18.255, 34.055)), ((15.109, 32.834), (11.6, 32.952), (8.582, 34.417)), ((7.273, 35.057), (6.209, 36.017), (4.982, 36.758)), ((4.755, 36.893), (4.473, 36.943), (4.255, 37.095)), ((4.127, 37.187), (4.118, 36.899), (4, 37)))
        self.add_bezier('e9', (4, 13), ((4, 12.006), (5.4, 11.453), (6.136, 10.931)), ((8.155, 9.516), (11.4, 8.017), (14, 8.017)), ((14.145, 8.008), (14.282, 8.008), (14.427, 8)), ((14.429, 8), (14.432, 8), (14.434, 8)), ((14.568, 8), (14.711, 8.008), (14.855, 8.008)), ((17.3, 8.008), (20.073, 9.661), (22, 11)))
        self.add_bezier('e10', (26, 13), ((30.127, 15.863), (34.791, 15.629), (39.073, 13.272)), ((40.855, 12.295), (42.409, 11.204), (44, 10)))
        self.add_contour('c0', 'e5', 'e0', 'e6')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
