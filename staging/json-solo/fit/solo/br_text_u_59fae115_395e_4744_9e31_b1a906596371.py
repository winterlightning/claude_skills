"""Br (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59fae115-395e-4744-9e31-b1a906596371'
SOURCE_PATH = 'icons-json/symbol/br (text u)_59fae115-395e-4744-9e31-b1a906596371.json'
AUTHOR = 'json_to_solo'

class BrTextUSymbol(Solo48):
    icon_id = 'br-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('br', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (14, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (32, 13), (32, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_arc('e6-1', (14, 27), (22, 19), radius_x=7, sweep=False)
        self.add_arc('e6-2', (22, 19), (16, 15), radius_x=7, sweep=False)
        self.add_arc('e6-3', (16, 15), (20, 6), radius_x=6, sweep=False)
        self.add_line('e6-4', (20, 6), (15, 4))
        self.add_arc('e7', (40, 13), (32, 17), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
