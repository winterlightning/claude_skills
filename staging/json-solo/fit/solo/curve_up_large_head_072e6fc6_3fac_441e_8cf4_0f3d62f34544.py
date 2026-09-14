"""Curve up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e5-1', (6, 35), (10, 41), radius_x=7, sweep=False)
        self.add_line('e5-2', (10, 41), (14, 42))
        self.add_line('e5-3', (14, 42), (19, 40))
        self.add_line('e5-4', (19, 40), (22, 35))
        self.add_arc('e6', (22, 20), (31, 11), radius_x=10)
        self.add_line('e7', (37, 17), (38, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e7', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
