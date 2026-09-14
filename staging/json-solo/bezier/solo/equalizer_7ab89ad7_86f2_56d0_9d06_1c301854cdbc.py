"""Equalizer (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ab89ad7-86f2-56d0-9d06-1c301854cdbc'
SOURCE_PATH = 'icons-json/audio/equalizer_7ab89ad7-86f2-56d0-9d06-1c301854cdbc.json'
AUTHOR = 'json_to_solo'

class Equalizer7ab89ad7(Solo48):
    icon_id = 'equalizer-7ab89ad7'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'audio')

    def build(self):
        self.add_line('e0', (9, 27), (9, 40))
        self.add_line('e1', (9, 18), (9, 8))
        self.add_line('e2', (24, 8), (24, 27))
        self.add_line('e3', (24, 40), (24, 34))
        self.add_line('e4', (39, 21), (39, 40))
        self.add_line('e5', (39, 8), (39, 12))
        self.add_arc('e6-top', (34, 16), (44, 16), radius_x=5, radius_y=4)
        self.add_arc('e6-bottom', (44, 16), (34, 16), radius_x=5, radius_y=4)
        self.add_arc('e7-top', (4, 22), (14, 22), radius_x=5, radius_y=4)
        self.add_arc('e7-bottom', (14, 22), (4, 22), radius_x=5, radius_y=4)
        self.add_arc('e8-top', (20, 31), (28, 31), radius_x=4, radius_y=3)
        self.add_arc('e8-bottom', (28, 31), (20, 31), radius_x=4, radius_y=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c4', 'e6')
        self.relate('connect', 'c5', 'e6')
