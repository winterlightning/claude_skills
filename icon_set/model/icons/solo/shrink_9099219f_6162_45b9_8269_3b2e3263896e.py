"""Shrink (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9099219f-6162-45b9-8269-3b2e3263896e'
SOURCE_PATH = 'icons-json/interface-essential/shrink_9099219f-6162-45b9-8269-3b2e3263896e.json'
AUTHOR = 'json_to_solo'

class ShrinkInterfaceEssential(Solo48):
    icon_id = 'shrink-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shrink', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (17, 18))
        self.add_line('e1', (12, 18), (17, 18))
        self.add_line('e2', (17, 12), (17, 18))
        self.add_line('e3', (42, 6), (31, 18))
        self.add_line('e4', (31, 18), (31, 12))
        self.add_line('e5', (36, 18), (31, 18))
        self.add_line('e6', (12, 30), (17, 30))
        self.add_line('e7', (6, 42), (17, 30))
        self.add_line('e8', (17, 36), (17, 30))
        self.add_line('e9', (36, 30), (31, 30))
        self.add_line('e10', (31, 36), (31, 30))
        self.add_line('e11', (31, 30), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8')
        self.add_contour('c8', 'e9')
        self.add_contour('c9', 'e10', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
