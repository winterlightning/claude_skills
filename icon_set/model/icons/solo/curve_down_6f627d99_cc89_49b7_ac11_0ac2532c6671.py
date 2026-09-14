"""Curve down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f627d99-cc89-49b7-ac11-0ac2532c6671'
SOURCE_PATH = 'icons-json/arrows/curve down_6f627d99-cc89-49b7-ac11-0ac2532c6671.json'
AUTHOR = 'json_to_solo'

class CurveDown(Solo48):
    icon_id = 'curve-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 13))
        self.add_line('e1', (12, 19), (31, 19))
        self.add_line('e2', (37, 25), (37, 42))
        self.add_line('e3', (31, 37), (37, 42))
        self.add_line('e4', (42, 37), (37, 42))
        self.add_arc('e5', (6, 13), (12, 19), radius_x=8, sweep=False)
        self.add_arc('e6', (31, 19), (37, 25), radius_x=7)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
