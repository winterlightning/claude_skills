"""Curvy both direction (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d07f4a9-676f-4b08-ad2a-73d2ff083486'
SOURCE_PATH = 'icons-json/arrows/curvy both direction_7d07f4a9-676f-4b08-ad2a-73d2ff083486.json'
AUTHOR = 'json_to_solo'

class CurvyBothDirectionArrows(Solo48):
    icon_id = 'curvy-both-direction-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'both', 'direction', 'arrows')

    def build(self):
        self.add_line('e0', (39, 8), (44, 12))
        self.add_line('e1', (9, 32), (4, 36))
        self.add_line('e2', (9, 40), (4, 36))
        self.add_line('e3', (39, 16), (44, 12))
        self.add_line('e4', (44, 12), (20, 12))
        self.add_line('e5', (21, 24), (26, 24))
        self.add_line('e6', (27, 36), (4, 36))
        self.add_bezier('e7', (20, 12), ((19.618, 12), (19.4, 12.455), (19.036, 12.573)), ((16.627, 13.356), (14.773, 15.571), (14.809, 17.971)), ((14.855, 21.128), (17.545, 24), (21, 24)))
        self.add_bezier('e8', (26, 24), ((29.391, 24), (31.964, 26.771), (32.155, 29.802)), ((32.3, 32.303), (30.564, 34.577), (28.073, 35.461)), ((27.691, 35.587), (27.4, 36), (27, 36)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7', 'e5', 'e8', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
