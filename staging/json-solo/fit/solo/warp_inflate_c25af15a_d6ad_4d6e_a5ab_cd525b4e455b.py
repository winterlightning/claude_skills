"""Warp inflate (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c25af15a-d6ad-4d6e-a5ab-cd525b4e455b'
SOURCE_PATH = 'icons-json/design/warp inflate_c25af15a-d6ad-4d6e-a5ab-cd525b4e455b.json'
AUTHOR = 'json_to_solo'

class WarpInflateDesign(Solo48):
    icon_id = 'warp-inflate-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'inflate', 'design')

    def build(self):
        self.add_arc('e0-1', (11, 11), (7, 15), radius_x=17)
        self.add_line('e0-2', (7, 15), (5, 18))
        self.add_line('e0-3', (5, 18), (4, 24))
        self.add_line('e0-4', (4, 24), (5, 30))
        self.add_arc('e0-5', (5, 30), (7, 33), radius_x=13, sweep=False)
        self.add_arc('e0-6', (7, 33), (13, 38), radius_x=17, sweep=False)
        self.add_line('e0-7', (13, 38), (23, 40))
        self.add_line('e0-8', (23, 40), (32, 39))
        self.add_arc('e0-9', (32, 39), (38, 36), radius_x=20, sweep=False)
        self.add_arc('e0-10', (38, 36), (44, 24), radius_x=15, sweep=False)
        self.add_line('e0-11', (44, 24), (43, 18))
        self.add_arc('e0-12', (43, 18), (39, 13), radius_x=14, sweep=False)
        self.add_arc('e0-13', (39, 13), (32, 9), radius_x=21, sweep=False)
        self.add_line('e0-14', (32, 9), (24, 8))
        self.add_line('e0-15', (24, 8), (17, 9))
        self.add_arc('e0-16', (17, 9), (11, 11), radius_x=26, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', 'e0-14', 'e0-15', 'e0-16', closed=True)
