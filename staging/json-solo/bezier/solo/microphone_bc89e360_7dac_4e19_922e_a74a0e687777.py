"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc89e360-7dac-4e19-922e-a74a0e687777'
SOURCE_PATH = 'icons-json/audio/microphone_bc89e360-7dac-4e19-922e-a74a0e687777.json'
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
        self.add_line('e0', (24, 44), (24, 4))
        self.add_line('e1', (16, 10), (16, 38))
        self.add_line('e2', (32, 34), (32, 14))
        self.add_line('e3', (8, 30), (8, 18))
        self.add_line('e4', (40, 27), (40, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
