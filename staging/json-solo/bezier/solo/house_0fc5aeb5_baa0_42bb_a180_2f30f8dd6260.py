"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fc5aeb5-baa0-42bb-a180-2f30f8dd6260'
SOURCE_PATH = 'icons-json/interface-essential/house_0fc5aeb5-baa0-42bb-a180-2f30f8dd6260.json'
AUTHOR = 'json_to_solo'

class House0fc5aeb5(Solo48):
    icon_id = 'house-0fc5aeb5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 44), (24, 29))
        self.add_line('e1', (40, 44), (8, 44))
        self.add_line('e2', (8, 44), (8, 19))
        self.add_line('e3', (8, 19), (24, 4))
        self.add_line('e4', (24, 4), (40, 19))
        self.add_line('e5', (40, 19), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
