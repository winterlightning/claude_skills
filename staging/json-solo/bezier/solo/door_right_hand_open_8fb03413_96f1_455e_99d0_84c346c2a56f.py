"""Door right hand open (building), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fb03413-96f1-455e-99d0-84c346c2a56f'
SOURCE_PATH = 'icons-json/building/door right hand open_8fb03413-96f1-455e-99d0-84c346c2a56f.json'
AUTHOR = 'json_to_solo'

class DoorRightHandOpenBuilding(Solo48):
    icon_id = 'door-right-hand-open-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'right', 'hand', 'open', 'building')

    def build(self):
        self.add_line('e0', (6, 42), (10, 42))
        self.add_line('e1', (10, 42), (10, 8))
        self.add_line('e2', (12, 6), (36, 6))
        self.add_line('e3', (38, 8), (38, 42))
        self.add_line('e4', (42, 42), (38, 42))
        self.add_line('e5', (36, 6), (26, 13))
        self.add_line('e6', (26, 13), (26, 39))
        self.add_line('e7', (26, 39), (32, 41))
        self.add_bezier('e8', (10, 8), ((10.295, 7.46), (10.705, 6.442), (11.285, 6.139)), ((11.433, 6.065), (11.853, 6.074), (12, 6)))
        self.add_bezier('e9', (36, 6), ((37.137, 6.581), (37.485, 6.994), (38, 8)))
        self.add_bezier('e10', (32, 41), ((33.407, 41.532), (35.307, 41.984), (36.813, 41.984)), ((36.944, 41.984), (37.075, 42), (37.197, 42)), ((37.435, 42), (37.763, 42), (38, 42)))
        self.add_contour('c0', 'e0', 'e1', 'e8', 'e2', 'e9', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
