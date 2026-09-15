"""Layers front (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dbf0ac16-2a71-5d64-b2cd-16f26ce22d99'
SOURCE_PATH = 'icons-json/design/layers front_dbf0ac16-2a71-5d64-b2cd-16f26ce22d99.json'
AUTHOR = 'gpt-6'

class LayersFront(Solo48):
    icon_id = 'layers-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('layers', 'front', 'design')

    def build(self):
        self.add_line('e0', (32, 16), (32, 7))
        self.add_line('e2', (6, 8), (6, 31))
        self.add_line('e3', (7, 32), (16, 32))
        self.add_line('e4', (20, 16), (36, 16))
        self.add_line('e5', (42, 17), (42, 40))
        self.add_line('e6', (40, 42), (17, 42))
        self.add_line('e7', (16, 41), (16, 17))
        self.add_line('e8-1', (32, 7), (30, 6))
        self.add_line('e8-2', (30, 6), (8, 6))
        self.add_arc('e9', (8, 6), (6, 8), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e10', (6, 31), (7, 32), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e11', (36, 16), (42, 17), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e12', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('e13', (17, 42), (16, 41))
        self.add_arc('e14', (16, 17), (20, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e9', 'e2', 'e10', 'e3', closed=False)
        self.add_contour('c1', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13', 'e7', 'e14', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
