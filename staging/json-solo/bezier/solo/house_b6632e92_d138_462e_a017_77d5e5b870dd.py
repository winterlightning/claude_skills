"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6632e92-d138-462e-a017-77d5e5b870dd'
SOURCE_PATH = 'icons-json/interface-essential/house_b6632e92-d138-462e-a017-77d5e5b870dd.json'
AUTHOR = 'json_to_solo'

class House(Solo48):
    icon_id = 'house'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 25), (24, 8))
        self.add_line('e1', (24, 8), (4, 25))
        self.add_line('e2', (38, 20), (38, 40))
        self.add_line('e3', (38, 40), (9, 40))
        self.add_line('e4', (9, 40), (9, 21))
        self.add_line('e5', (29, 30), (19, 30))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
