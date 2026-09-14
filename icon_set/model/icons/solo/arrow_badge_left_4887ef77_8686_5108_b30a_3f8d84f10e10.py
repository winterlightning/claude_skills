"""Arrow badge left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4887ef77-8686-5108-b30a-3f8d84f10e10'
SOURCE_PATH = 'icons-json/arrows/arrow badge left_4887ef77-8686-5108-b30a-3f8d84f10e10.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeLeft(Solo48):
    icon_id = 'arrow-badge-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (16, 39), (4, 24))
        self.add_line('e1', (17, 8), (41, 8))
        self.add_bezier('e2', (4, 24), ((4.055, 23.85), (4.109, 23.7), (4.155, 23.55)), ((4.309, 23.24), (4.609, 23.02), (4.8, 22.73)), ((6.018, 20.88), (7.5, 19.24), (8.864, 17.53)), ((11.445, 14.31), (14.327, 11.1), (17, 8)))
        self.add_bezier('e3', (41, 8), ((41.064, 8), (41.4, 8), (41.464, 8)), ((43.9, 8), (43.645, 10.54), (43.755, 12.33)), ((43.836, 13.62), (43.9, 14.91), (43.945, 16.2)), ((43.973, 16.99), (43.982, 17.78), (43.982, 18.57)), ((43.982, 23.44), (44, 28.31), (44, 33.18)), ((44, 33.202), (44, 33.224), (44, 33.246)), ((44, 34.624), (43.991, 36.012), (43.991, 37.39)), ((43.991, 39.02), (42.936, 39.99), (41.5, 39.99)), ((41.428, 39.99), (41.366, 40), (41.303, 40)), ((41.302, 40), (41.301, 40), (41.3, 40)), ((35.536, 40), (29.773, 39.98), (24.009, 39.98)), ((22.791, 39.98), (21.573, 39.96), (20.355, 39.94)), ((19.036, 39.92), (17.018, 40), (16, 39)))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3', closed=True)
