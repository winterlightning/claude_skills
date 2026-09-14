"""Building (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265ecf16-9a75-43f1-970c-76948410da91'
SOURCE_PATH = 'icons-json/building/building_265ecf16-9a75-43f1-970c-76948410da91.json'
AUTHOR = 'json_to_solo'

class Building265ecf16(Solo48):
    icon_id = 'building-265ecf16'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self):
        self.add_line('e0', (33, 19), (42, 23))
        self.add_line('e1', (42, 23), (42, 42))
        self.add_line('e2', (42, 42), (6, 42))
        self.add_line('e3', (33, 42), (33, 6))
        self.add_line('e4', (33, 6), (11, 6))
        self.add_line('e5', (11, 6), (11, 42))
        self.add_line('e6', (19, 17), (24, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
