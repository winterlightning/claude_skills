"""Equalizer stereo (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36dab9b9-612f-5996-9e36-283d9015d62a'
SOURCE_PATH = 'icons-json/audio/equalizer stereo_36dab9b9-612f-5996-9e36-283d9015d62a.json'
AUTHOR = 'json_to_solo'

class EqualizerStereoAudio(Solo48):
    icon_id = 'equalizer-stereo-audio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'stereo', 'audio')

    def build(self):
        self.add_line('e0', (10, 6), (10, 20))
        self.add_line('e1', (10, 28), (10, 42))
        self.add_line('e2', (24, 26), (24, 6))
        self.add_line('e3', (24, 42), (24, 35))
        self.add_line('e4', (38, 12), (38, 6))
        self.add_line('e5', (38, 20), (38, 42))
        self.add_arc('e6-top', (6, 24), (14, 24), radius_x=4)
        self.add_arc('e6-bottom', (14, 24), (6, 24), radius_x=4)
        self.add_arc('e7-top', (20, 31), (28, 31), radius_x=4)
        self.add_arc('e7-bottom', (28, 31), (20, 31), radius_x=4)
        self.add_arc('e8-top', (34, 16), (42, 16), radius_x=4)
        self.add_arc('e8-bottom', (42, 16), (34, 16), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e7')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c4', 'e8')
        self.relate('connect', 'c5', 'e8')
