"""Arrow turn right (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1bcfe64-3284-42f4-938d-a4971fc66eef'
SOURCE_PATH = 'icons-json/state/arrow turn right_f1bcfe64-3284-42f4-938d-a4971fc66eef.json'
AUTHOR = 'json_to_solo'

class ArrowTurnRightState(Solo48):
    icon_id = 'arrow-turn-right-state'
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
        self.add_arc('e4', (6, 22), (15, 13), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
