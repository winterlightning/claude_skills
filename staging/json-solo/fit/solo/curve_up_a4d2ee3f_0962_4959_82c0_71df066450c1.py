"""Curve up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4d2ee3f-0962-4959-82c0-71df066450c1'
SOURCE_PATH = 'icons-json/arrows/curve up_a4d2ee3f-0962-4959-82c0-71df066450c1.json'
AUTHOR = 'json_to_solo'

class CurveUpA4d2ee3f(Solo48):
    icon_id = 'curve-up-a4d2ee3f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (37, 6), (42, 11))
        self.add_line('e1', (6, 42), (17, 42))
        self.add_line('e2', (22, 35), (22, 17))
        self.add_line('e3', (28, 11), (42, 11))
        self.add_line('e4', (37, 16), (42, 11))
        self.add_arc('e5', (17, 42), (22, 35), radius_x=6, sweep=False)
        self.add_arc('e6', (22, 17), (28, 11), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
