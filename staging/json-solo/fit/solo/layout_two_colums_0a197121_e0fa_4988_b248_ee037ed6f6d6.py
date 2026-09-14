"""Layout two colums (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a197121-e0fa-4988-b248-ee037ed6f6d6'
SOURCE_PATH = 'icons-json/interface-essential/layout two colums_0a197121-e0fa-4988-b248-ee037ed6f6d6.json'
AUTHOR = 'json_to_solo'

class LayoutTwoColumsInterfaceEssential(Solo48):
    icon_id = 'layout-two-colums-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'two', 'colums', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 42))
        self.add_line('sym-e1', (24, 42), (40, 42))
        self.add_arc('sym-e3', (40, 42), (42, 39), radius_x=4, sweep=False)
        self.add_line('sym-e5', (42, 39), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 9))
        self.add_arc('sym-e8', (42, 9), (40, 6), radius_x=4, sweep=False)
        self.add_line('sym-e10', (40, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (8, 6))
        self.add_arc('sym-e13', (8, 6), (6, 9), radius_x=4, sweep=False)
        self.add_line('sym-e15', (6, 9), (6, 24))
        self.add_line('sym-e16', (6, 24), (6, 39))
        self.add_arc('sym-e18', (6, 39), (8, 42), radius_x=4, sweep=False)
        self.add_line('sym-e20', (8, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e20')
