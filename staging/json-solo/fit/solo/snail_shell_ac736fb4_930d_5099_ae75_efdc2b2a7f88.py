"""Snail shell (animals), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac736fb4-930d-5099-ae75-efdc2b2a7f88'
SOURCE_PATH = 'icons-json/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.json'
AUTHOR = 'json_to_solo'

class SnailShell(Solo48):
    icon_id = 'snail-shell'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('snail', 'shell', 'animals')

    def build(self):
        self.add_line('e0', (4, 31), (4, 27))
        self.add_arc('e1-1', (4, 27), (6, 19), radius_x=17)
        self.add_arc('e1-2', (6, 19), (15, 10), radius_x=21)
        self.add_line('e1-3', (15, 10), (25, 8))
        self.add_arc('e1-4', (25, 8), (38, 13), radius_x=20)
        self.add_arc('e1-5', (38, 13), (44, 25), radius_x=16)
        self.add_arc('e1-6', (44, 25), (29, 40), radius_x=15)
        self.add_line('e1-7', (29, 40), (23, 39))
        self.add_arc('e1-8', (23, 39), (16, 33), radius_x=14)
        self.add_arc('e1-9', (16, 33), (15, 26), radius_x=11)
        self.add_arc('e1-10', (15, 26), (34, 24), radius_x=10)
        self.add_arc('e1-11', (34, 24), (30, 31), radius_x=6)
        self.add_arc('e1-12', (30, 31), (23, 29), radius_x=5)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12')
