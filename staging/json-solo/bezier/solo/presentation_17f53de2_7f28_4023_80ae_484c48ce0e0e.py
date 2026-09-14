"""Presentation (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'icons-json/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.json'
AUTHOR = 'json_to_solo'

class PresentationOffice(Solo48):
    icon_id = 'presentation-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'office')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (41, 8), (41, 30))
        self.add_line('e2', (39, 32), (9, 32))
        self.add_line('e3', (7, 30), (7, 8))
        self.add_line('e4', (24, 36), (24, 32))
        self.add_bezier('e5', (24, 36), ((24.582, 36.396), (25.518, 36.648), (25.818, 37.305)), ((26.418, 38.577), (25.327, 39.992), (23.836, 39.992)), ((23.755, 39.992), (23.673, 40), (23.591, 40)), ((23.59, 40), (23.588, 40), (23.587, 40)), ((23.507, 40), (23.426, 40), (23.345, 40)), ((22.027, 40), (20.927, 38.754), (21.309, 37.566)), ((21.545, 36.817), (22.464, 36.421), (23, 36)))
        self.add_bezier('e6', (41, 30), ((41, 31.802), (40.845, 32), (39, 32)))
        self.add_bezier('e7', (9, 32), ((7.455, 32), (7, 31.491), (7, 30)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
