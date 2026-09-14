"""Camping tent (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b621e1c-a261-5113-bae2-aea7a2add5c6'
SOURCE_PATH = 'icons-json/outdoors/camping tent_0b621e1c-a261-5113-bae2-aea7a2add5c6.json'
AUTHOR = 'json_to_solo'

class CampingTent0b621e1c(Solo48):
    icon_id = 'camping-tent-0b621e1c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('camping', 'tent', 'outdoors')

    def build(self):
        self.add_line('e0', (33, 40), (24, 23))
        self.add_line('e1', (24, 23), (17, 40))
        self.add_line('e2', (20, 8), (24, 13))
        self.add_line('e3', (24, 13), (4, 40))
        self.add_line('e4', (4, 40), (44, 40))
        self.add_line('e5', (44, 40), (24, 13))
        self.add_line('e6', (24, 13), (28, 8))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
