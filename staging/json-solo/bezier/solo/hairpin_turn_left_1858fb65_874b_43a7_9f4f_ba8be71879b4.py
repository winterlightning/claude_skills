"""Hairpin turn left (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1858fb65-874b-43a7-9f4f-ba8be71879b4'
SOURCE_PATH = 'icons-json/transportation/hairpin turn left_1858fb65-874b-43a7-9f4f-ba8be71879b4.json'
AUTHOR = 'json_to_solo'

class HairpinTurnLeftTransportation(Solo48):
    icon_id = 'hairpin-turn-left-transportation'
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
        self.add_bezier('e4', (40, 18), ((40, 17.027), (39.638, 15.491), (39.368, 14.555)), ((37.718, 8.736), (33.002, 4.009), (27.133, 4.009)), ((27.066, 4.009), (27, 4), (26.934, 4)), ((26.933, 4), (26.932, 4), (26.931, 4)), ((26.585, 4), (26.248, 4.009), (25.903, 4.009)), ((20.337, 4.009), (15.411, 8.436), (13.76, 14.036)), ((13.432, 15.145), (13, 16.818), (13, 18)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
