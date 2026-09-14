"""Rate stretch tool (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7be4363f-746d-5909-9b6e-3dba795301f6'
SOURCE_PATH = 'icons-json/arrows/rate stretch tool_7be4363f-746d-5909-9b6e-3dba795301f6.json'
AUTHOR = 'json_to_solo'

class RateStretchToolArrows(Solo48):
    icon_id = 'rate-stretch-tool-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rate', 'stretch', 'tool', 'arrows')

    def build(self):
        self.add_line('e0', (9, 8), (4, 13))
        self.add_line('e1', (9, 18), (4, 13))
        self.add_line('e2', (4, 13), (20, 13))
        self.add_line('e3', (25, 16), (25, 21))
        self.add_line('e4', (25, 27), (25, 32))
        self.add_line('e5', (29, 36), (44, 36))
        self.add_line('e6', (39, 40), (44, 36))
        self.add_line('e7', (44, 36), (39, 31))
        self.add_bezier('e8', (20, 13), ((21.7, 13), (25, 14.24), (25, 16)))
        self.add_bezier('e9', (25, 32), ((25, 33.432), (25.736, 34.905), (27.255, 35.503)), ((27.936, 35.764), (28.273, 36), (29, 36)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
