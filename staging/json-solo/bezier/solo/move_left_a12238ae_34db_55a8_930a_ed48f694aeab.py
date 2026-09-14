"""Move left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a12238ae-34db-55a8-930a-ed48f694aeab'
SOURCE_PATH = 'icons-json/interface-essential/move left_a12238ae-34db-55a8-930a-ed48f694aeab.json'
AUTHOR = 'json_to_solo'

class MoveLeft(Solo48):
    icon_id = 'move-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
