"""Arrows left right (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fae0335-97b9-4e1b-8d78-a1150a192b9f'
SOURCE_PATH = 'icons-json/symbol/arrows left right_4fae0335-97b9-4e1b-8d78-a1150a192b9f.json'
AUTHOR = 'json_to_solo'

class ArrowsLeftRightSymbol(Solo48):
    icon_id = 'arrows-left-right-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrows', 'left', 'right', 'symbol')

    def build(self):
        self.add_line('e0', (8, 11), (16, 4))
        self.add_line('e1', (16, 4), (16, 29))
        self.add_line('e2', (16, 4), (25, 11))
        self.add_line('e3', (32, 19), (32, 44))
        self.add_line('e4', (32, 44), (23, 37))
        self.add_line('e5', (32, 44), (40, 37))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
