"""Curve up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '072e6fc6-3fac-441e-8cf4-0f3d62f34544'
SOURCE_PATH = 'icons-json/arrows/curve up large head_072e6fc6-3fac-441e-8cf4-0f3d62f34544.json'
AUTHOR = 'json_to_solo'

class CurveUpLargeHeadArrows(Solo48):
    icon_id = 'curve-up-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (37, 6), (42, 11))
        self.add_line('e1', (6, 28), (6, 35))
        self.add_line('e2', (22, 35), (22, 20))
        self.add_line('e3', (31, 11), (42, 11))
        self.add_line('e4', (38, 16), (42, 11))
        self.add_bezier('e5', (6, 35), ((6, 38.665), (9.747, 41.992), (13.413, 41.992)), ((13.477, 41.992), (13.534, 42), (13.598, 42)), ((13.599, 42), (13.6, 42), (13.601, 42)), ((13.789, 42), (13.977, 41.992), (14.165, 41.992)), ((17.545, 41.992), (20.285, 39.3), (21.185, 36.183)), ((21.316, 35.741), (22, 35.45), (22, 35)))
        self.add_bezier('e6', (22, 20), ((22, 19.55), (21.75, 18.845), (21.873, 18.404)), ((22.822, 14.926), (25.735, 12.145), (29.22, 11.245)), ((29.384, 11.204), (30.943, 11), (31, 11)))
        self.add_bezier('e7', (37, 17), ((37.27, 16.73), (37.755, 16.295), (38, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e7', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
