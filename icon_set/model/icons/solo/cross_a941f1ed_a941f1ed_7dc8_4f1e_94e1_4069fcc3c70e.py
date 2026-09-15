"""Cross (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e'
SOURCE_PATH = 'icons-json/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.json'
AUTHOR = 'gpt-6'

class CrossA941f1ed(Solo48):
    icon_id = 'cross-a941f1ed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cross', 'health')

    def build(self):
        self.add_line('e0', (30, 6), (19, 6))
        self.add_line('e1', (17, 8), (17, 17))
        self.add_line('e2', (17, 17), (7, 17))
        self.add_line('e3', (6, 19), (6, 28))
        self.add_line('e4', (8, 31), (17, 31))
        self.add_line('e5', (17, 31), (17, 40))
        self.add_line('e6', (19, 42), (28, 42))
        self.add_line('e7', (31, 41), (31, 31))
        self.add_line('e8', (31, 31), (40, 31))
        self.add_line('e9', (42, 29), (42, 19))
        self.add_line('e10', (40, 17), (31, 17))
        self.add_arc('e11', (31, 17), (30, 6), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('e12', (19, 6), (17, 8), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e13', (7, 17), (6, 19))
        self.add_line('e14', (6, 28), (8, 31))
        self.add_arc('e15', (17, 40), (19, 42), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e16', (28, 42), (31, 41))
        self.add_line('e17', (40, 31), (42, 29))
        self.add_arc('e18-2', (42, 19), (40, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3', 'e14', 'e4', 'e5', 'e15', 'e6', 'e16', 'e7', 'e8', 'e17', 'e9', 'e18-2', 'e10', closed=True)
