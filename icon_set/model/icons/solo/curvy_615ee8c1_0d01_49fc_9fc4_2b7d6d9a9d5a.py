"""Curvy (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '615ee8c1-0d01-49fc-9fc4-2b7d6d9a9d5a'
SOURCE_PATH = 'icons-json/arrows/curvy_615ee8c1-0d01-49fc-9fc4-2b7d6d9a9d5a.json'
AUTHOR = 'json_to_solo'

class Curvy(Solo48):
    icon_id = 'curvy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (4, 32))
        self.add_line('e1', (25, 32), (25, 21))
        self.add_line('e2', (33, 14), (44, 14))
        self.add_line('e3', (39, 18), (44, 14))
        self.add_line('e4', (39, 10), (44, 14))
        self.add_arc('e5-1', (4, 32), (14, 40), radius_x=11, sweep=False)
        self.add_line('e5-2', (14, 40), (21, 38))
        self.add_arc('e5-3', (21, 38), (25, 32), radius_x=8, sweep=False)
        self.add_arc('e6', (25, 21), (33, 14), radius_x=9)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
