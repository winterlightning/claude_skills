"""Layout none (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7bc33403-2397-4bdd-984e-77f2e208ad65'
SOURCE_PATH = 'icons-json/interface-essential/layout none_7bc33403-2397-4bdd-984e-77f2e208ad65.json'
AUTHOR = 'gpt-6'

class LayoutNone(Solo48):
    icon_id = 'layout-none'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'none', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 39), (6, 9))
        self.add_arc('sym-e2', (6, 9), (9, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e4', (9, 6), (39, 6))
        self.add_arc('sym-e7', (39, 6), (42, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e8', (42, 9), (42, 39))
        self.add_arc('sym-e10', (42, 39), (39, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e12', (39, 42), (9, 42))
        self.add_arc('sym-e15', (9, 42), (6, 39), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e12', 'sym-e15', closed=True)
