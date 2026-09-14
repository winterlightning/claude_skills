"""Headphones (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90ffd8be-8c2b-43c1-9cda-658b2b74c820'
SOURCE_PATH = 'icons-json/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.json'
AUTHOR = 'json_to_solo'

class Headphones(Solo48):
    icon_id = 'headphones'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self):
        self.add_line('e0', (37, 40), (37, 28))
        self.add_line('e1', (37, 28), (37, 20))
        self.add_line('e2', (11, 40), (11, 28))
        self.add_line('e3', (11, 28), (11, 20))
        self.add_arc('e4-1', (11, 21), (24, 8), radius_x=13)
        self.add_line('e4-2', (24, 8), (31, 10))
        self.add_arc('e4-3', (31, 10), (35, 14), radius_x=12)
        self.add_arc('e4-4', (35, 14), (37, 20), radius_x=12)
        self.add_line('e5-1', (37, 40), (41, 39))
        self.add_arc('e5-2', (41, 39), (44, 34), radius_x=6, sweep=False)
        self.add_arc('e5-3', (44, 34), (37, 28), radius_x=7, sweep=False)
        self.add_arc('e6-1', (11, 28), (4, 34), radius_x=7, sweep=False)
        self.add_arc('e6-2', (4, 34), (10, 40), radius_x=6, sweep=False)
        self.add_arc('e6-3', (10, 40), (11, 40), radius_x=22)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e6-1', 'e6-2', 'e6-3', 'e2', closed=True)
        self.add_contour('c5', 'e3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c5', 'c1')
