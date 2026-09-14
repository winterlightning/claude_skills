"""Curvy (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '615ee8c1-0d01-49fc-9fc4-2b7d6d9a9d5a'
SOURCE_PATH = 'icons-json/arrows/curvy_615ee8c1-0d01-49fc-9fc4-2b7d6d9a9d5a.json'
AUTHOR = 'json_to_solo'

class CurvyArrows(Solo48):
    icon_id = 'curvy-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (4, 32))
        self.add_line('e1', (25, 32), (25, 21))
        self.add_line('e2', (33, 14), (44, 14))
        self.add_line('e3', (39, 18), (44, 14))
        self.add_line('e4', (39, 10), (44, 14))
        self.add_bezier('e5', (4, 32), ((4, 32.741), (4.345, 33.179), (4.636, 33.861)), ((6.064, 37.238), (9.718, 39.992), (13.745, 39.992)), ((13.817, 39.992), (13.88, 40), (13.951, 40)), ((13.952, 40), (13.953, 40), (13.955, 40)), ((14.273, 40), (14.582, 39.992), (14.9, 39.992)), ((18.7, 39.992), (22.582, 37.592), (24.255, 34.501)), ((24.582, 33.895), (25, 32.691), (25, 32)))
        self.add_bezier('e6', (25, 21), ((25, 20.453), (25.173, 19.478), (25.382, 18.981)), ((26.491, 16.429), (29.2, 14.669), (32.036, 14.097)), ((32.345, 14.029), (32.709, 14), (33, 14)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
