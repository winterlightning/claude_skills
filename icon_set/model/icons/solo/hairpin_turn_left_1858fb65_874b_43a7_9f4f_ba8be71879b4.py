"""Hairpin turn left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1858fb65-874b-43a7-9f4f-ba8be71879b4'
SOURCE_PATH = 'icons-json/transportation/hairpin turn left_1858fb65-874b-43a7-9f4f-ba8be71879b4.json'
AUTHOR = 'json_to_solo'

class HairpinTurnLeft(Solo48):
    icon_id = 'hairpin-turn-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('hairpin', 'turn', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (40, 44), (40, 18))
        self.add_line('e1', (13, 18), (13, 32))
        self.add_line('e2', (8, 27), (13, 32))
        self.add_line('e3', (18, 27), (13, 32))
        self.add_arc('e4-1', (40, 18), (27, 4), radius_x=15, sweep=False)
        self.add_arc('e4-2', (27, 4), (13, 18), radius_x=14, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
