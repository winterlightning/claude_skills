"""Warp fish (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf262ac0-6a03-43ea-a2f5-d9b248545818'
SOURCE_PATH = 'icons-json/design/warp fish_cf262ac0-6a03-43ea-a2f5-d9b248545818.json'
AUTHOR = 'json_to_solo'

class WarpFishDesign(Solo48):
    icon_id = 'warp-fish-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'fish', 'design')

    def build(self):
        self.add_line('e0', (44, 36), (41, 32))
        self.add_line('e1', (31, 31), (28, 36))
        self.add_line('e2', (27, 12), (31, 17))
        self.add_line('e3', (42, 15), (44, 12))
        self.add_line('e4', (44, 12), (44, 36))
        self.add_arc('e5', (41, 32), (31, 31), radius_x=6, sweep=False)
        self.add_line('e6-1', (28, 36), (24, 39))
        self.add_line('e6-2', (24, 39), (19, 40))
        self.add_arc('e6-3', (19, 40), (4, 24), radius_x=17)
        self.add_arc('e6-4', (4, 24), (18, 8), radius_x=17)
        self.add_line('e6-5', (18, 8), (23, 9))
        self.add_line('e6-6', (23, 9), (27, 12))
        self.add_arc('e7', (31, 17), (42, 15), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e2', 'e7', 'e3', 'e4', closed=True)
