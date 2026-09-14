"""Layout right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29ad656c-72e5-47fe-9a76-8b377da539c2'
SOURCE_PATH = 'icons-json/interface-essential/layout right_29ad656c-72e5-47fe-9a76-8b377da539c2.json'
AUTHOR = 'json_to_solo'

class LayoutRight(Solo48):
    icon_id = 'layout-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'right', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 6), (30, 42))
        self.add_line('sym-e1', (30, 42), (39, 42))
        self.add_arc('sym-e2', (39, 42), (42, 39), radius_x=4, sweep=False)
        self.add_line('sym-e4', (42, 39), (42, 24))
        self.add_line('sym-e5', (42, 24), (42, 9))
        self.add_arc('sym-e7', (42, 9), (39, 6), radius_x=4, sweep=False)
        self.add_line('sym-e8', (39, 6), (30, 6))
        self.add_line('sym-e9', (30, 6), (9, 6))
        self.add_arc('sym-e10', (9, 6), (6, 9), radius_x=4, sweep=False)
        self.add_line('sym-e11', (6, 9), (6, 24))
        self.add_line('sym-e12', (6, 24), (6, 39))
        self.add_arc('sym-e13', (6, 39), (9, 42), radius_x=5, sweep=False)
        self.add_line('sym-e14', (9, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
