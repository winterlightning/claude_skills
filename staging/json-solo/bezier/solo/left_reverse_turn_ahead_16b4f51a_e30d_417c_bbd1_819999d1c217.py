"""Left reverse turn ahead (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16b4f51a-e30d-417c-bbd1-819999d1c217'
SOURCE_PATH = 'icons-json/transportation/left reverse turn ahead_16b4f51a-e30d-417c-bbd1-819999d1c217.json'
AUTHOR = 'json_to_solo'

class LeftReverseTurnAheadTransportation(Solo48):
    icon_id = 'left-reverse-turn-ahead-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('left', 'reverse', 'turn', 'ahead', 'transportation')

    def build(self):
        self.add_line('e0', (8, 12), (17, 4))
        self.add_line('e1', (40, 44), (40, 32))
        self.add_line('e2', (33, 27), (24, 27))
        self.add_line('e3', (17, 20), (17, 4))
        self.add_line('e4', (27, 13), (17, 4))
        self.add_bezier('e5', (40, 32), ((40, 28.909), (36.16, 27), (33, 27)))
        self.add_bezier('e6', (24, 27), ((20.75, 27), (17, 22.955), (17, 20)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
