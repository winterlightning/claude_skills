"""Microphone karaoke (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae391a9-9356-50c7-bd0a-64b441bf643b'
SOURCE_PATH = 'icons-json/audio/microphone karaoke_5ae391a9-9356-50c7-bd0a-64b441bf643b.json'
AUTHOR = 'json_to_solo'

class MicrophoneKaraoke(Solo48):
    icon_id = 'microphone-karaoke'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'karaoke', 'audio')

    def build(self):
        self.add_line('e0', (21, 15), (10, 32))
        self.add_line('e1', (16, 37), (30, 24))
        self.add_line('e2', (11, 44), (27, 44))
        self.add_arc('e3-top', (22, 14), (40, 14), radius_x=9, radius_y=10)
        self.add_arc('e3-bottom', (40, 14), (22, 14), radius_x=9, radius_y=10)
        self.add_arc('e4', (10, 32), (11, 38), radius_x=5, sweep=False)
        self.add_arc('e5', (11, 38), (16, 37), radius_x=5, sweep=False)
        self.add_arc('e6-1', (11, 38), (8, 41), radius_x=4, sweep=False)
        self.add_arc('e6-2', (8, 41), (11, 44), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e4')
        self.add_contour('c1', 'e5', 'e1')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
