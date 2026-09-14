"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fca3db3-620d-4288-b69b-2fa7ea2255ff'
SOURCE_PATH = 'icons-json/interface-essential/house_7fca3db3-620d-4288-b69b-2fa7ea2255ff.json'
AUTHOR = 'json_to_solo'

class House7fca3db3(Solo48):
    icon_id = 'house-7fca3db3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 24), (11, 19))
        self.add_line('e1', (42, 24), (37, 19))
        self.add_line('e2', (24, 33), (24, 42))
        self.add_line('e3', (37, 19), (24, 6))
        self.add_line('e4', (24, 6), (11, 19))
        self.add_line('e5', (37, 19), (37, 42))
        self.add_line('e6', (37, 42), (11, 42))
        self.add_line('e7', (11, 42), (11, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5', 'e6', 'e7')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
