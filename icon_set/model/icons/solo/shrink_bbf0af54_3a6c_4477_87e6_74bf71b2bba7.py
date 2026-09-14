"""Shrink (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbf0af54-3a6c-4477-87e6-74bf71b2bba7'
SOURCE_PATH = 'icons-json/interface-essential/shrink_bbf0af54-3a6c-4477-87e6-74bf71b2bba7.json'
AUTHOR = 'json_to_solo'

class ShrinkBbf0af54(Solo48):
    icon_id = 'shrink-bbf0af54'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shrink', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (32, 17))
        self.add_line('e1', (32, 17), (30, 18))
        self.add_line('e2', (30, 18), (39, 18))
        self.add_line('e3', (30, 8), (30, 18))
        self.add_line('e4', (6, 6), (18, 18))
        self.add_line('e5', (9, 18), (18, 18))
        self.add_line('e6', (18, 8), (18, 18))
        self.add_line('e7', (39, 30), (30, 30))
        self.add_line('e8', (30, 39), (30, 30))
        self.add_line('e9', (42, 42), (30, 30))
        self.add_line('e10', (9, 30), (18, 30))
        self.add_line('e11', (6, 42), (18, 30))
        self.add_line('e12', (18, 39), (18, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11')
        self.add_contour('c10', 'e12')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
