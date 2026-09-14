"""Shapes (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80482a3e-5b08-4ded-ac07-3afb54321744'
SOURCE_PATH = 'icons-json/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.json'
AUTHOR = 'json_to_solo'

class Shapes80482a3e(Solo48):
    icon_id = 'shapes-80482a3e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'design')

    def build(self):
        self.add_line('e0', (31, 20), (42, 20))
        self.add_line('e1', (42, 20), (42, 42))
        self.add_line('e2', (42, 42), (20, 42))
        self.add_line('e3', (20, 42), (20, 31))
        self.add_line('e4', (31, 20), (20, 20))
        self.add_line('e5', (20, 20), (20, 31))
        self.add_arc('e6-1', (31, 20), (19, 6), radius_x=13, sweep=False)
        self.add_line('e6-2', (19, 6), (13, 7))
        self.add_arc('e6-3', (13, 7), (8, 12), radius_x=14, sweep=False)
        self.add_arc('e6-4', (8, 12), (6, 18), radius_x=11, sweep=False)
        self.add_line('e6-5', (6, 18), (7, 24))
        self.add_line('e6-6', (7, 24), (10, 28))
        self.add_arc('e6-7', (10, 28), (20, 31), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
