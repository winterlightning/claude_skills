"""Symbol medical (protection), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2218007-b6c4-5c1b-9355-0c9d6d72fb5c'
SOURCE_PATH = 'icons-json/protection/symbol medical_c2218007-b6c4-5c1b-9355-0c9d6d72fb5c.json'
AUTHOR = 'gpt-6'

class SymbolMedical(Solo48):
    icon_id = 'symbol-medical'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'medical', 'protection')

    def build(self):
        self.add_line('e0', (30, 18), (30, 8))
        self.add_line('e1', (27, 6), (19, 6))
        self.add_line('e2', (18, 8), (18, 18))
        self.add_line('e3', (18, 18), (8, 18))
        self.add_line('e4', (6, 19), (6, 28))
        self.add_line('e5', (9, 30), (18, 30))
        self.add_line('e6', (18, 30), (18, 39))
        self.add_line('e7', (19, 42), (26, 42))
        self.add_line('e8', (30, 41), (30, 30))
        self.add_line('e9', (30, 30), (40, 30))
        self.add_line('e10', (42, 28), (42, 20))
        self.add_line('e11', (40, 18), (30, 18))
        self.add_arc('e12-1', (30, 8), (28, 6), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e12-2', (28, 6), (27, 6), radius_x=65, radius_y=65, large_arc=False, sweep=True)
        self.add_arc('e13-2', (19, 6), (18, 8), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e14', (8, 18), (6, 19))
        self.add_arc('e15-1', (6, 28), (6, 29), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e15-2', (6, 29), (9, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e16', (18, 39), (19, 42), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e17', (26, 42), (30, 41))
        self.add_arc('e18', (40, 30), (42, 28), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e19', (42, 20), (40, 18), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e12-1', 'e12-2', 'e1', 'e13-2', 'e2', 'e3', 'e14', 'e4', 'e15-1', 'e15-2', 'e5', 'e6', 'e16', 'e7', 'e17', 'e8', 'e9', 'e18', 'e10', 'e19', 'e11', closed=True)
