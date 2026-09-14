"""Equalizer (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cb200bc-b63a-5cdf-b3df-b8eaf3162ee7'
SOURCE_PATH = 'icons-json/audio/equalizer_3cb200bc-b63a-5cdf-b3df-b8eaf3162ee7.json'
AUTHOR = 'json_to_solo'

class Equalizer(Solo48):
    icon_id = 'equalizer'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'audio')

    def build(self):
        self.add_line('e0', (39, 28), (39, 8))
        self.add_line('e1', (39, 40), (39, 37))
        self.add_line('e2', (8, 24), (8, 8))
        self.add_line('e3', (8, 31), (8, 40))
        self.add_line('e4', (24, 8), (24, 15))
        self.add_line('e5', (24, 21), (24, 40))
        self.add_arc('e6-top', (20, 18), (28, 18), radius_x=4, radius_y=3)
        self.add_arc('e6-bottom', (28, 18), (20, 18), radius_x=4, radius_y=3)
        self.add_arc('e7-top', (4, 27), (12, 27), radius_x=4, radius_y=3)
        self.add_arc('e7-bottom', (12, 27), (4, 27), radius_x=4, radius_y=3)
        self.add_arc('e8-top', (34, 32), (44, 32), radius_x=5, radius_y=4)
        self.add_arc('e8-bottom', (44, 32), (34, 32), radius_x=5, radius_y=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c2', 'e7')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c4', 'e6')
        self.relate('connect', 'c5', 'e6')
