"""Circinus (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be9f8244-ccfa-43c2-ae5f-b81294c4fbd1'
SOURCE_PATH = 'icons-json/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.json'
AUTHOR = 'json_to_solo'

class CircinusBe9f8244(Solo48):
    icon_id = 'circinus-be9f8244'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circinus', 'state')

    def build(self):
        self.add_line('e0', (22, 22), (35, 32))
        self.add_line('e1', (35, 32), (35, 34))
        self.add_line('e2', (42, 6), (39, 9))
        self.add_line('e3', (6, 31), (28, 17))
        self.add_line('e4', (26, 42), (34, 21))
        self.add_arc('e5-top', (27, 14), (41, 14), radius_x=7)
        self.add_arc('e5-bottom', (41, 14), (27, 14), radius_x=7)
        self.add_line('e6', (35, 32), (36, 31))
        self.add_contour('c0', 'e0', 'e6')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c3', 'e5')
        self.relate('connect', 'c4', 'e5')
