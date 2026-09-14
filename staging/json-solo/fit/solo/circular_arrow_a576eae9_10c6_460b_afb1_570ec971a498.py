"""Circular arrow (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icons-json/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.json'
AUTHOR = 'json_to_solo'

class CircularArrowState(Solo48):
    icon_id = 'circular-arrow-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circular', 'arrow', 'state')

    def build(self):
        self.add_line('e0', (41, 15), (36, 11))
        self.add_line('e1', (40, 31), (42, 26))
        self.add_line('e2', (32, 16), (41, 16))
        self.add_line('e3', (41, 16), (41, 7))
        self.add_arc('e4-1', (36, 11), (24, 6), radius_x=17, sweep=False)
        self.add_arc('e4-2', (24, 6), (9, 14), radius_x=19, sweep=False)
        self.add_arc('e4-3', (9, 14), (6, 23), radius_x=16, sweep=False)
        self.add_line('e4-4', (6, 23), (8, 32))
        self.add_arc('e4-5', (8, 32), (16, 40), radius_x=18, sweep=False)
        self.add_arc('e4-6', (16, 40), (24, 42), radius_x=17, sweep=False)
        self.add_arc('e4-7', (24, 42), (40, 31), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')
