"""Curvy both direction (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d07f4a9-676f-4b08-ad2a-73d2ff083486'
SOURCE_PATH = 'icons-json/arrows/curvy both direction_7d07f4a9-676f-4b08-ad2a-73d2ff083486.json'
AUTHOR = 'json_to_solo'

class CurvyBothDirection(Solo48):
    icon_id = 'curvy-both-direction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'both', 'direction', 'arrows')

    def build(self):
        self.add_line('e0', (39, 8), (44, 12))
        self.add_line('e1', (9, 32), (4, 36))
        self.add_line('e2', (9, 40), (4, 36))
        self.add_line('e3', (39, 16), (44, 12))
        self.add_line('e4', (44, 12), (20, 12))
        self.add_line('e5', (21, 24), (26, 24))
        self.add_line('e6', (27, 36), (4, 36))
        self.add_arc('e7-1', (20, 12), (15, 19), radius_x=6, sweep=False)
        self.add_arc('e7-2', (15, 19), (21, 24), radius_x=6, sweep=False)
        self.add_arc('e8-1', (26, 24), (32, 29), radius_x=6)
        self.add_arc('e8-2', (32, 29), (27, 36), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7-1', 'e7-2', 'e5', 'e8-1', 'e8-2', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
