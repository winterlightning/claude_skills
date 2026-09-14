"""Right reverse turn ahead (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '182f0248-c380-4521-a855-6c9c834f593d'
SOURCE_PATH = 'icons-json/transportation/right reverse turn ahead_182f0248-c380-4521-a855-6c9c834f593d.json'
AUTHOR = 'json_to_solo'

class RightReverseTurnAheadTransportation(Solo48):
    icon_id = 'right-reverse-turn-ahead-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('right', 'reverse', 'turn', 'ahead', 'transportation')

    def build(self):
        self.add_line('e0', (8, 44), (8, 24))
        self.add_line('e1', (10, 23), (29, 23))
        self.add_line('e2', (30, 22), (30, 4))
        self.add_line('e3', (30, 4), (21, 12))
        self.add_line('e4', (30, 4), (40, 12))
        self.add_bezier('e5', (8, 24), ((8.016, 23.936), (8.016, 23.873), (8.032, 23.809)), ((8.032, 23.227), (9.456, 23.2), (10, 23)))
        self.add_bezier('e6', (29, 23), ((29.208, 22.918), (29.424, 23.045), (29.68, 22.945)), ((30.24, 22.727), (29.696, 22.264), (30, 22)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
