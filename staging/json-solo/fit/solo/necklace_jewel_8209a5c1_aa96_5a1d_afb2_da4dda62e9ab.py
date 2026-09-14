"""Batch-02/necklace jewel (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8209a5c1-aa96-5a1d-afb2-da4dda62e9ab'
SOURCE_PATH = 'icons-json/accessories/batch-02/necklace jewel_8209a5c1-aa96-5a1d-afb2-da4dda62e9ab.json'
AUTHOR = 'json_to_solo'

class Batch02NecklaceJewel(Solo48):
    icon_id = 'batch-02-necklace-jewel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'jewel', 'accessories')

    def build(self):
        self.add_line('e0', (6, 6), (6, 10))
        self.add_line('e1', (24, 27), (21, 31))
        self.add_arc('e2-1', (6, 10), (35, 22), radius_x=18, sweep=False)
        self.add_arc('e2-2', (35, 22), (42, 9), radius_x=17, sweep=False)
        self.add_line('e2-3', (42, 9), (42, 6))
        self.add_arc('e3-1', (21, 31), (24, 42), radius_x=6, sweep=False)
        self.add_arc('e3-2', (24, 42), (29, 38), radius_x=6, sweep=False)
        self.add_arc('e3-3', (29, 38), (24, 27), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e1', closed=True)
