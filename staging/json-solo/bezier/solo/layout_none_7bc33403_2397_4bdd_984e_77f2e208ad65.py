"""Layout none (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bc33403-2397-4bdd-984e-77f2e208ad65'
SOURCE_PATH = 'icons-json/interface-essential/layout none_7bc33403-2397-4bdd-984e-77f2e208ad65.json'
AUTHOR = 'json_to_solo'

class LayoutNoneInterfaceEssential(Solo48):
    icon_id = 'layout-none-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'none', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 39), (6, 24))
        self.add_line('sym-e1', (6, 24), (6, 9))
        self.add_bezier('sym-e2', (6, 9), ((6, 7.634), (7.625, 6), (9, 6)))
        self.add_bezier('sym-e3', (9, 6), ((9.025, 6), (8.975, 6.008), (9, 6)))
        self.add_line('sym-e4', (9, 6), (24, 6))
        self.add_line('sym-e5', (24, 6), (39, 6))
        self.add_bezier('sym-e6', (39, 6), ((39.025, 6.008), (38.975, 6), (39, 6)))
        self.add_bezier('sym-e7', (39, 6), ((40.375, 6), (42, 7.634), (42, 9)))
        self.add_line('sym-e8', (42, 9), (42, 24))
        self.add_line('sym-e9', (42, 24), (42, 39))
        self.add_bezier('sym-e10', (42, 39), ((42, 40.366), (40.375, 42), (39, 42)))
        self.add_bezier('sym-e11', (39, 42), ((38.975, 42), (39.025, 41.992), (39, 42)))
        self.add_line('sym-e12', (39, 42), (24, 42))
        self.add_line('sym-e13', (24, 42), (9, 42))
        self.add_bezier('sym-e14', (9, 42), ((8.975, 41.992), (9.025, 42), (9, 42)))
        self.add_bezier('sym-e15', (9, 42), ((7.625, 42), (6, 40.366), (6, 39)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
