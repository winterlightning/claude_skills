"""Arrow turn right (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1bcfe64-3284-42f4-938d-a4971fc66eef'
SOURCE_PATH = 'icons-json/state/arrow turn right_f1bcfe64-3284-42f4-938d-a4971fc66eef.json'
AUTHOR = 'json_to_solo'

class ArrowTurnRightF1bcfe64(Solo48):
    icon_id = 'arrow-turn-right-f1bcfe64'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'turn', 'right', 'state')

    def build(self):
        self.add_line('e0', (34, 6), (42, 13))
        self.add_line('e1', (6, 42), (6, 22))
        self.add_line('e2', (15, 13), (42, 13))
        self.add_line('e3', (35, 21), (42, 13))
        self.add_bezier('e4', (6, 22), ((6, 21.509), (6.213, 21.349), (6.344, 20.883)), ((7.342, 17.43), (10.394, 14.476), (13.863, 13.593)), ((14.198, 13.511), (14.656, 13), (15, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
