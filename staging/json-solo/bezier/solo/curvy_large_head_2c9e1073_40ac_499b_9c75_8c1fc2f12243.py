"""Curvy large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c9e1073-40ac-499b-9c75-8c1fc2f12243'
SOURCE_PATH = 'icons-json/arrows/curvy large head_2c9e1073-40ac-499b-9c75-8c1fc2f12243.json'
AUTHOR = 'json_to_solo'

class CurvyLargeHeadArrows(Solo48):
    icon_id = 'curvy-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (39, 8), (44, 13))
        self.add_line('e1', (20, 33), (20, 21))
        self.add_line('e2', (29, 13), (44, 13))
        self.add_line('e3', (39, 19), (44, 13))
        self.add_bezier('e4', (4, 32), ((4, 32.286), (4.018, 32.16), (4.018, 32.446)), ((4.018, 36.362), (7.527, 39.992), (11.891, 39.992)), ((11.962, 39.992), (12.034, 40), (12.106, 40)), ((12.107, 40), (12.108, 40), (12.109, 40)), ((12.327, 40), (12.536, 39.992), (12.755, 39.992)), ((16.2, 39.992), (19.182, 37.457), (20.036, 34.484)), ((20.136, 34.139), (20, 33.337), (20, 33)))
        self.add_bezier('e5', (20, 21), ((20, 20.789), (20.536, 20.051), (20.591, 19.823)), ((21.273, 16.901), (24.018, 14.349), (27.036, 13.406)), ((27.473, 13.272), (28.536, 13), (29, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
