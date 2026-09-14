"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43ee606c-4f75-4eea-ae65-cbce49a24ba4'
SOURCE_PATH = 'icons-json/audio/microphone_43ee606c-4f75-4eea-ae65-cbce49a24ba4.json'
AUTHOR = 'json_to_solo'

class Microphone43ee606c(Solo48):
    icon_id = 'microphone-43ee606c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('e0', (20, 20), (15, 20))
        self.add_line('e1', (15, 14), (21, 14))
        self.add_line('e2', (24, 37), (24, 44))
        self.add_line('e3', (15, 12), (15, 21))
        self.add_line('e4', (33, 22), (33, 12))
        self.add_arc('e5-1', (8, 21), (29, 36), radius_x=16, sweep=False)
        self.add_arc('e5-2', (29, 36), (40, 23), radius_x=14, sweep=False)
        self.add_arc('e5-3', (40, 23), (40, 21), radius_x=27)
        self.add_arc('e6-1', (33, 12), (31, 7), radius_x=8, sweep=False)
        self.add_arc('e6-2', (31, 7), (26, 4), radius_x=9, sweep=False)
        self.add_arc('e6-3', (26, 4), (24, 4), radius_x=15)
        self.add_line('e6-4', (24, 4), (18, 6))
        self.add_arc('e6-5', (18, 6), (15, 12), radius_x=8, sweep=False)
        self.add_arc('e7-1', (15, 21), (23, 31), radius_x=9, sweep=False)
        self.add_arc('e7-2', (23, 31), (33, 22), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e3', 'e7-1', 'e7-2', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c2')
