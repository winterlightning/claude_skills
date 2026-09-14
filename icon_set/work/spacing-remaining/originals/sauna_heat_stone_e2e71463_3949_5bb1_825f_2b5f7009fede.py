"""Sauna heat stone (spas), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2e71463-3949-5bb1-825f-2b5f7009fede'
SOURCE_PATH = 'icons-json/spas/sauna heat stone_e2e71463-3949-5bb1-825f-2b5f7009fede.json'
AUTHOR = 'json_to_solo'

class SaunaHeatStone(Solo48):
    icon_id = 'sauna-heat-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('sauna', 'heat', 'stone', 'spas')

    def build(self):
        self.add_line('e0', (15, 22), (13, 16))
        self.add_arc('e1-1', (22, 29), (25, 23), radius_x=12, sweep=False)
        self.add_line('e1-2', (25, 23), (22, 12))
        self.add_arc('e1-3', (22, 12), (25, 6), radius_x=11)
        self.add_line('e2-1', (6, 31), (7, 35))
        self.add_arc('e2-2', (7, 35), (10, 38), radius_x=12, sweep=False)
        self.add_arc('e2-3', (10, 38), (23, 42), radius_x=24, sweep=False)
        self.add_line('e2-4', (23, 42), (32, 41))
        self.add_arc('e2-5', (32, 41), (38, 38), radius_x=19, sweep=False)
        self.add_arc('e2-6', (38, 38), (42, 32), radius_x=7, sweep=False)
        self.add_line('e2-7', (42, 32), (42, 31))
        self.add_arc('e3-1', (33, 27), (34, 20), radius_x=6, sweep=False)
        self.add_arc('e3-2', (34, 20), (32, 13), radius_x=14)
        self.add_arc('e3-3', (32, 13), (35, 8), radius_x=10)
        self.add_arc('e4', (13, 27), (15, 22), radius_x=8, sweep=False)
        self.add_arc('e5', (13, 16), (15, 8), radius_x=11)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3')
        self.add_contour('c3', 'e4', 'e0', 'e5')
