"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b72da6ab-adc1-4364-be21-8572894c8a90'
SOURCE_PATH = 'icons-json/audio/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.json'
AUTHOR = 'json_to_solo'

class Microphone(Solo48):
    icon_id = 'microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('e0', (16, 13), (21, 13))
        self.add_line('e1', (24, 39), (24, 44))
        self.add_line('e2', (16, 11), (16, 20))
        self.add_line('e3', (32, 21), (32, 11))
        self.add_line('e4-1', (8, 19), (8, 22))
        self.add_arc('e4-2', (8, 22), (11, 31), radius_x=18, sweep=False)
        self.add_arc('e4-3', (11, 31), (20, 38), radius_x=16, sweep=False)
        self.add_arc('e4-4', (20, 38), (40, 23), radius_x=16, sweep=False)
        self.add_arc('e4-5', (40, 23), (40, 20), radius_x=25)
        self.add_line('e5-1', (32, 11), (29, 6))
        self.add_arc('e5-2', (29, 6), (24, 4), radius_x=8, sweep=False)
        self.add_arc('e5-3', (24, 4), (19, 6), radius_x=8, sweep=False)
        self.add_arc('e5-4', (19, 6), (16, 11), radius_x=8, sweep=False)
        self.add_arc('e6-1', (16, 20), (21, 28), radius_x=8, sweep=False)
        self.add_arc('e6-2', (21, 28), (32, 21), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e6-1', 'e6-2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
