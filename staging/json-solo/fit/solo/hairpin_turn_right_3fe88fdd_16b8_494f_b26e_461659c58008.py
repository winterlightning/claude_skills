"""Hairpin turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'icons-json/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.json'
AUTHOR = 'json_to_solo'

class HairpinTurnRightTransportation(Solo48):
    icon_id = 'hairpin-turn-right-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('hairpin', 'turn', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (27, 26), (34, 34))
        self.add_line('e1', (34, 34), (40, 29))
        self.add_line('e2', (34, 34), (34, 18))
        self.add_line('e3', (8, 19), (8, 44))
        self.add_arc('e4-1', (34, 18), (22, 4), radius_x=14, sweep=False)
        self.add_line('e4-2', (22, 4), (15, 6))
        self.add_arc('e4-3', (15, 6), (10, 11), radius_x=15, sweep=False)
        self.add_line('e4-4', (10, 11), (8, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
