"""Round join (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f5aab0a-147a-4c15-abd8-9edc17c0fea2'
SOURCE_PATH = 'icons-json/design/round join_9f5aab0a-147a-4c15-abd8-9edc17c0fea2.json'
AUTHOR = 'json_to_solo'

class RoundJoinDesign(Solo48):
    icon_id = 'round-join-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('round', 'join', 'design')

    def build(self):
        self.add_line('e0', (16, 42), (16, 22))
        self.add_line('e1', (22, 17), (42, 17))
        self.add_line('e2', (16, 42), (26, 42))
        self.add_line('e3', (26, 42), (26, 26))
        self.add_line('e4', (26, 26), (42, 26))
        self.add_line('e5', (42, 26), (42, 17))
        self.add_line('e6', (16, 42), (6, 42))
        self.add_line('e7', (6, 42), (6, 16))
        self.add_line('e8', (15, 6), (42, 6))
        self.add_line('e9', (42, 6), (42, 17))
        self.add_bezier('e10', (16, 22), ((16, 19.145), (19.325, 17), (22, 17)))
        self.add_bezier('e11', (6, 16), ((6, 15.935), (6.008, 15.687), (6.008, 15.622)), ((6.008, 15.033), (6.213, 14.386), (6.36, 13.83)), ((7.276, 10.345), (9.886, 7.227), (13.445, 6.278)), ((13.871, 6.164), (14.37, 6), (14.812, 6)), ((14.877, 6), (14.935, 6), (15, 6)))
        self.add_contour('c0', 'e0', 'e10', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e6', 'e7', 'e11', 'e8', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
