"""Duster (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f67a6c5a-82c0-459f-849b-7118b51d21fb'
SOURCE_PATH = 'icons-json/wayfinding/duster_f67a6c5a-82c0-459f-849b-7118b51d21fb.json'
AUTHOR = 'json_to_solo'

class DusterWayfinding(Solo48):
    icon_id = 'duster-wayfinding'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('duster', 'wayfinding')

    def build(self):
        self.add_line('e0', (6, 42), (20, 28))
        self.add_line('e1', (40, 12), (36, 8))
        self.add_line('e2', (20, 28), (21, 28))
        self.add_arc('e3-1', (36, 8), (33, 6), radius_x=6, sweep=False)
        self.add_arc('e3-2', (33, 6), (28, 11), radius_x=6, sweep=False)
        self.add_arc('e3-3', (28, 11), (24, 13), radius_x=5, sweep=False)
        self.add_arc('e3-4', (24, 13), (23, 16), radius_x=5, sweep=False)
        self.add_line('e3-5', (23, 16), (19, 18))
        self.add_arc('e3-6', (19, 18), (24, 31), radius_x=9, sweep=False)
        self.add_arc('e3-7', (24, 31), (28, 31), radius_x=5, sweep=False)
        self.add_arc('e3-8', (28, 31), (32, 25), radius_x=6, sweep=False)
        self.add_arc('e3-9', (32, 25), (36, 23), radius_x=5, sweep=False)
        self.add_arc('e3-10', (36, 23), (37, 20), radius_x=5, sweep=False)
        self.add_arc('e3-11', (37, 20), (42, 15), radius_x=5, sweep=False)
        self.add_arc('e3-12', (42, 15), (40, 12), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', closed=True)
        self.relate('connect', 'c0', 'c1')
