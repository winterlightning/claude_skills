"""Paragraph 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (15, 25), ((14.378, 25), (13.642, 24.573), (13.036, 24.409)), ((9.273, 23.386), (6.008, 20.13), (6.008, 16.047)), ((6.008, 15.991), (6, 15.927), (6, 15.87)), ((6, 15.869), (6, 15.868), (6, 15.867)), ((6, 15.622), (6.008, 15.368), (6.008, 15.123)), ((6.008, 10.975), (9.42, 7.587), (13.184, 6.417)), ((13.74, 6.245), (14.427, 6), (15, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
