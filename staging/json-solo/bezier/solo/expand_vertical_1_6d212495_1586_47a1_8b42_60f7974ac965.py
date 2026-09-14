"""Expand vertical 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d212495-1586-47a1-8b42-60f7974ac965'
SOURCE_PATH = 'icons-json/interface-essential/expand vertical 1_6d212495-1586-47a1-8b42-60f7974ac965.json'
AUTHOR = 'json_to_solo'

class ExpandVertical1InterfaceEssential(Solo48):
    icon_id = 'expand-vertical-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'vertical', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 11), (25, 6))
        self.add_line('e1', (6, 24), (25, 24))
        self.add_line('e2', (20, 37), (25, 42))
        self.add_line('e3', (30, 37), (25, 42))
        self.add_line('e4', (42, 24), (25, 24))
        self.add_line('e5', (30, 11), (25, 6))
        self.add_line('e6', (25, 42), (25, 24))
        self.add_line('e7', (25, 6), (25, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
