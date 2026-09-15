"""Layers back (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f17d8853-9c2e-4620-a59b-8439f073a9b7'
SOURCE_PATH = 'pictographic-primitives/design/layers back_f17d8853-9c2e-4620-a59b-8439f073a9b7.svg'
AUTHOR = 'gpt-6'

class LayersBack(Solo48):
    icon_id = 'layers-back'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('layers', 'back', 'design')

    def build(self):
        self.add_line('e0', (33, 14), (41, 14))
        self.add_line('e1', (42, 16), (42, 41))
        self.add_line('e2', (41, 42), (16, 42))
        self.add_line('e3', (15, 41), (15, 33))
        self.add_line('e4', (33, 14), (33, 32))
        self.add_line('e5', (32, 33), (15, 33))
        self.add_line('e6', (33, 14), (33, 7))
        self.add_line('e7', (32, 6), (6, 6))
        self.add_line('e9', (7, 33), (15, 33))
        self.add_line('e10', (41, 14), (42, 16))
        self.add_arc('e11', (42, 41), (41, 42), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e12', (16, 42), (15, 41), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e13', (33, 32), (32, 33), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e14', (33, 7), (32, 6), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('e15', (6, 6), (6, 32))
        self.add_arc('e16', (6, 32), (7, 33), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3', closed=False)
        self.add_contour('c1', 'e4', 'e13', 'e5', closed=False)
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e16', 'e9', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
