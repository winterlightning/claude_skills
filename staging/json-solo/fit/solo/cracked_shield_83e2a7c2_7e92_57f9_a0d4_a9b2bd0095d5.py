"""Cracked shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5'
SOURCE_PATH = 'icons-json/protection/cracked shield_83e2a7c2-7e92-57f9-a0d4-a9b2bd0095d5.json'
AUTHOR = 'json_to_solo'

class CrackedShieldProtection(Solo48):
    icon_id = 'cracked-shield-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('cracked', 'shield', 'protection')

    def build(self):
        self.add_line('e0', (29, 7), (21, 20))
        self.add_line('e1', (21, 20), (29, 23))
        self.add_line('e2', (29, 23), (22, 34))
        self.add_line('e3', (24, 4), (21, 6))
        self.add_arc('e4-1', (21, 6), (8, 9), radius_x=34)
        self.add_line('e4-2', (8, 9), (8, 16))
        self.add_line('e4-3', (8, 16), (9, 24))
        self.add_arc('e4-4', (9, 24), (12, 32), radius_x=30, sweep=False)
        self.add_arc('e4-5', (12, 32), (24, 44), radius_x=33, sweep=False)
        self.add_arc('e4-6', (24, 44), (37, 30), radius_x=31, sweep=False)
        self.add_arc('e4-7', (37, 30), (39, 25), radius_x=30, sweep=False)
        self.add_line('e4-8', (39, 25), (40, 16))
        self.add_line('e4-9', (40, 16), (40, 9))
        self.add_arc('e4-10', (40, 9), (24, 4), radius_x=29)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', closed=True)
        self.relate('connect', 'c0', 'c1')
