"""Xd (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '745c0a55-b6f3-45b5-8923-20698c6b86de'
SOURCE_PATH = 'icons-json/symbol/Xd_745c0a55-b6f3-45b5-8923-20698c6b86de.json'
AUTHOR = 'json_to_solo'

class Xd(Solo48):
    icon_id = 'xd'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('xd', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (22, 40))
        self.add_line('e1', (4, 40), (22, 8))
        self.add_line('e2', (44, 8), (44, 35))
        self.add_arc('e3-1', (44, 35), (42, 39), radius_x=6)
        self.add_line('e3-2', (42, 39), (38, 40))
        self.add_arc('e3-3', (38, 40), (37, 40), radius_x=19, sweep=False)
        self.add_arc('e3-4', (37, 40), (32, 35), radius_x=7)
        self.add_arc('e3-5', (32, 35), (35, 20), radius_x=15)
        self.add_arc('e3-6', (35, 20), (44, 23), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6')
