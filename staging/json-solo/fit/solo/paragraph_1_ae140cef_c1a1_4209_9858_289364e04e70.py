"""Paragraph 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae140cef-c1a1-4209-9858-289364e04e70'
SOURCE_PATH = 'icons-json/interface-essential/paragraph 1_ae140cef-c1a1-4209-9858-289364e04e70.json'
AUTHOR = 'json_to_solo'

class Paragraph1InterfaceEssential(Solo48):
    icon_id = 'paragraph-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paragraph', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 42), (27, 25))
        self.add_line('e1', (42, 6), (27, 6))
        self.add_line('e2', (27, 25), (15, 25))
        self.add_line('e3', (15, 6), (27, 6))
        self.add_line('e4', (27, 25), (27, 6))
        self.add_arc('e5-1', (15, 25), (6, 16), radius_x=10)
        self.add_line('e5-2', (6, 16), (7, 11))
        self.add_line('e5-3', (7, 11), (10, 8))
        self.add_arc('e5-4', (10, 8), (15, 6), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
