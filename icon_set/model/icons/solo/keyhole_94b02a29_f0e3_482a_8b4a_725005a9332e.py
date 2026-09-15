"""Keyhole (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94b02a29-f0e3-482a-8b4a-725005a9332e'
SOURCE_PATH = 'icons-json/symbol/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.json'
AUTHOR = 'gpt-6'

class Keyhole(Solo48):
    icon_id = 'keyhole'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('keyhole', 'symbol')

    def build(self):
        self.add_line('e0', (26, 4), (20, 4))
        self.add_line('e1', (15, 24), (10, 44))
        self.add_line('e2', (10, 44), (38, 44))
        self.add_line('e3', (38, 44), (33, 24))
        self.add_arc('e4-1', (33, 24), (40, 15), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e4-2', (40, 15), (35, 7), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e4-3', (35, 7), (26, 4), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_arc('e5-1', (20, 4), (8, 15), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('e5-2', (8, 15), (15, 24), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5-1', 'e5-2', 'e1', 'e2', 'e3', closed=True)
