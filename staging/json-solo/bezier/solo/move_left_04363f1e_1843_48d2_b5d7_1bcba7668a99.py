"""Move left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04363f1e-1843-48d2-b5d7-1bcba7668a99'
SOURCE_PATH = 'icons-json/interface-essential/move left_04363f1e-1843-48d2-b5d7-1bcba7668a99.json'
AUTHOR = 'json_to_solo'

class MoveLeft04363f1e(Solo48):
    icon_id = 'move-left-04363f1e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'left', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (8, 44), (8, 4))
        self.add_line('sym-e1', (19, 24), (40, 24))
        self.add_line('sym-e2', (19, 24), (27, 33))
        self.add_line('sym-e3', (19, 24), (27, 15))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
