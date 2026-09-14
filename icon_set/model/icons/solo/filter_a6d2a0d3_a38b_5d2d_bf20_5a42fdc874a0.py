"""Filter (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6d2a0d3-a38b-5d2d-bf20-5a42fdc874a0'
SOURCE_PATH = 'icons-json/interface-essential/filter_a6d2a0d3-a38b-5d2d-bf20-5a42fdc874a0.json'
AUTHOR = 'json_to_solo'

class Filter(Solo48):
    icon_id = 'filter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('filter', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 42), (28, 34))
        self.add_line('e1', (28, 34), (28, 25))
        self.add_line('e2', (28, 25), (41, 9))
        self.add_line('e3', (39, 6), (8, 6))
        self.add_line('e4', (6, 8), (20, 25))
        self.add_line('e5', (20, 25), (20, 42))
        self.add_arc('e6-1', (41, 9), (42, 8), radius_x=2)
        self.add_line('e6-2', (42, 8), (42, 7))
        self.add_line('e6-3', (42, 7), (39, 6))
        self.add_arc('e7', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7', 'e4', 'e5', closed=True)
