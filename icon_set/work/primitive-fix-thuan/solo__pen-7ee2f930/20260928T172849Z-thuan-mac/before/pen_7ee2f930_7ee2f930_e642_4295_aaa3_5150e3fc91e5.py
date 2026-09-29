"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ee2f930-e642-4295-aaa3-5150e3fc91e5'
SOURCE_PATH = 'pictographic-primitives/design/pen_7ee2f930-e642-4295-aaa3-5150e3fc91e5.svg'
AUTHOR = 'gpt-6'

class Pen7ee2f930(Solo48):
    icon_id = 'pen-7ee2f930'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'state')
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_line('e0', (6, 42), (10, 30))
        self.add_line('e2', (40, 17), (21, 37))
        self.add_line('e3', (19, 38), (6, 42))
        self.add_line('e4', (10, 30), (32, 8))
        self.add_arc('e5-1', (32, 8), (36, 6), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e5-2', (36, 6), (42, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e5-3', (42, 12), (40, 17))
        self.add_line('e6', (21, 37), (19, 38))
        self.add_contour('c0', 'e0', 'e4', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6', 'e3', closed=True)
