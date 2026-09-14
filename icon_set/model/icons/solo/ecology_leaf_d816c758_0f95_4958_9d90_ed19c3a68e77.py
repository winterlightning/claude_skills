"""Ecology leaf (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd816c758-0f95-4958-9d90-ed19c3a68e77'
SOURCE_PATH = 'icons-json/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.json'
AUTHOR = 'json_to_solo'

class EcologyLeaf(Solo48):
    icon_id = 'ecology-leaf'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('ecology', 'leaf')

    def build(self):
        self.add_line('e0', (4, 37), (8, 34))
        self.add_line('e1', (34, 12), (23, 12))
        self.add_bezier('e2', (27, 22), ((19.945, 24.779), (13.436, 28.964), (8, 34)))
        self.add_bezier('e3', (23, 12), ((20.618, 12), (18.127, 13.288), (16.082, 14.333)), ((13.891, 15.461), (11.836, 16.851), (10.191, 18.619)), ((6.373, 22.728), (4.518, 29.154), (7.636, 34.105)), ((9.809, 37.566), (14.836, 39.992), (19.127, 39.992)), ((19.27, 39.992), (19.405, 40), (19.548, 40)), ((19.55, 40), (19.552, 40), (19.555, 40)), ((19.845, 40), (20.127, 39.992), (20.418, 39.992)), ((23.391, 39.992), (26.464, 38.973), (29.064, 37.718)), ((38.836, 33.002), (43.991, 24.573), (43.991, 14.459)), ((43.991, 14.326), (44, 14.194), (44, 14.061)), ((44, 14.059), (44, 14.057), (44, 14.055)), ((44, 13.575), (43.991, 13.095), (43.991, 12.615)), ((43.991, 11.554), (43.909, 10.493), (43.818, 9.44)), ((43.773, 8.96), (43.736, 8.48), (43.691, 8)), ((43.689, 8), (43.688, 8), (43.685, 8)), ((43.533, 8), (41.436, 9.496), (40.855, 9.844)), ((38.909, 11.015), (36.373, 12), (34, 12)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
