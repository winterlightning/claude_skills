"""Handwritten text character (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3'
SOURCE_PATH = 'icons-json/interface-essential/handwritten text character_0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3.json'
AUTHOR = 'json_to_solo'

class HandwrittenTextCharacterInterfaceEssential(Solo48):
    icon_id = 'handwritten-text-character-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('handwritten', 'text', 'character', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 13), (22, 25))
        self.add_line('e1', (28, 26), (34, 12))
        self.add_line('e2-1', (6, 42), (12, 12))
        self.add_arc('e2-2', (12, 12), (17, 6), radius_x=6)
        self.add_arc('e2-3', (17, 6), (21, 13), radius_x=6)
        self.add_arc('e3-1', (22, 25), (25, 30), radius_x=6, sweep=False)
        self.add_arc('e3-2', (25, 30), (28, 26), radius_x=4, sweep=False)
        self.add_arc('e4-1', (34, 12), (39, 6), radius_x=7)
        self.add_arc('e4-2', (39, 6), (41, 9), radius_x=3)
        self.add_line('e4-3', (41, 9), (42, 42))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3')
