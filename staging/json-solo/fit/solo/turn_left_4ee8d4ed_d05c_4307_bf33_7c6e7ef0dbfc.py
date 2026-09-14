"""Turn left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc'
SOURCE_PATH = 'icons-json/transportation/turn left_4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc.json'
AUTHOR = 'json_to_solo'

class TurnLeftTransportation(Solo48):
    icon_id = 'turn-left-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('turn', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (16, 4), (8, 12))
        self.add_line('e1', (8, 12), (17, 22))
        self.add_line('e2', (8, 12), (27, 12))
        self.add_line('e3', (40, 24), (40, 44))
        self.add_arc('e4-1', (27, 12), (37, 16), radius_x=13)
        self.add_arc('e4-2', (37, 16), (39, 19), radius_x=11)
        self.add_line('e4-3', (39, 19), (40, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
