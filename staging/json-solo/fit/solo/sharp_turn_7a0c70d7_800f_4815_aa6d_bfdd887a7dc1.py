"""Sharp turn (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a0c70d7-800f-4815-aa6d-bfdd887a7dc1'
SOURCE_PATH = 'icons-json/transportation/sharp turn_7a0c70d7-800f-4815-aa6d-bfdd887a7dc1.json'
AUTHOR = 'json_to_solo'

class SharpTurnTransportation(Solo48):
    icon_id = 'sharp-turn-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('sharp', 'turn', 'transportation')

    def build(self):
        self.add_line('e0', (30, 4), (38, 10))
        self.add_line('e1', (38, 10), (40, 12))
        self.add_line('e2', (8, 44), (8, 23))
        self.add_line('e3', (22, 12), (40, 12))
        self.add_line('e4', (30, 20), (40, 12))
        self.add_arc('e5', (8, 23), (22, 12), radius_x=14)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
