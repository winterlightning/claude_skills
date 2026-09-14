"""Increase (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '221b5783-800f-49b5-82d0-cf19fce26cfc'
SOURCE_PATH = 'icons-json/arrows/increase_221b5783-800f-49b5-82d0-cf19fce26cfc.json'
AUTHOR = 'json_to_solo'

class IncreaseArrows(Solo48):
    icon_id = 'increase-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('increase', 'arrows')

    def build(self):
        self.add_line('e0', (34, 12), (39, 9))
        self.add_line('e1', (39, 9), (40, 8))
        self.add_line('e2', (4, 40), (22, 40))
        self.add_line('e3', (36, 27), (39, 10))
        self.add_line('e4', (39, 10), (40, 8))
        self.add_line('e5', (44, 15), (40, 8))
        self.add_bezier('e6', (22, 40), ((22.191, 40), (22.582, 40), (22.773, 40)), ((23.273, 40), (23.855, 39.84), (24.345, 39.76)), ((30.255, 38.84), (34.673, 33.19), (36, 27)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
