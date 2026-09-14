"""Round join (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e10', (16, 22), (22, 17), radius_x=7)
        self.add_arc('e11', (6, 16), (15, 6), radius_x=11)
        self.add_contour('c0', 'e0', 'e10', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e6', 'e7', 'e11', 'e8', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
