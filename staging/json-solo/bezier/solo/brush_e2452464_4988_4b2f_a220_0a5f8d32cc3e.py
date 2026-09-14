"""Batch-01/brush (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'icons-json/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.json'
AUTHOR = 'json_to_solo'

class Batch01Brush(Solo48):
    icon_id = 'batch-01-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'brush', 'decoration')

    def build(self):
        self.add_line('e0', (8, 37), (9, 32))
        self.add_line('e1', (22, 32), (26, 29))
        self.add_line('e2', (17, 27), (21, 22))
        self.add_line('e3', (21, 22), (38, 7))
        self.add_line('e4', (42, 10), (29, 26))
        self.add_line('e5', (29, 26), (26, 29))
        self.add_bezier('e6', (17, 27), ((18.972, 28.342), (20.462, 30.208), (22, 32)))
        self.add_bezier('e7', (22, 32), ((23.039, 38.513), (17.422, 41.992), (11.474, 41.992)), ((11.031, 41.992), (10.588, 42), (10.137, 42)), ((10.13, 42), (10.123, 42), (10.115, 42)), ((9.96, 42), (9.796, 41.984), (9.641, 41.984)), ((8.774, 41.984), (7.865, 41.812), (7.047, 41.558)), ((6.701, 41.453), (6, 41.349), (6, 41.244)), ((6, 41.242), (6.005, 41.241), (6, 41.239)), ((6.352, 40.846), (6.712, 40.454), (7.064, 40.061)), ((7.08, 40.036), (7.105, 40.02), (7.129, 39.995)), ((7.833, 39.251), (7.836, 37.998), (8, 37)))
        self.add_bezier('e8', (9, 32), ((9.646, 28.105), (13.375, 26.46), (17, 27)))
        self.add_bezier('e9', (38, 7), ((38.344, 6.689), (39.022, 6.008), (39.496, 6.008)), ((39.529, 6.008), (39.561, 6), (39.585, 6)), ((39.586, 6), (39.586, 6), (39.586, 6)), ((39.668, 6), (39.742, 6.016), (39.815, 6.016)), ((40.29, 6.016), (42, 6.998), (42, 7.546)), ((42, 8.397), (42, 9.149), (42, 10)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7', 'e0', 'e8')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e3', 'e9', 'e4', 'e5')
