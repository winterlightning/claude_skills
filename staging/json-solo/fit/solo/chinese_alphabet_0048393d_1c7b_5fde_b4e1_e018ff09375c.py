"""Chinese alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0048393d-1c7b-5fde-b4e1-e018ff09375c'
SOURCE_PATH = 'icons-json/interface-essential/chinese alphabet_0048393d-1c7b-5fde-b4e1-e018ff09375c.json'
AUTHOR = 'json_to_solo'

class ChineseAlphabetInterfaceEssential(Solo48):
    icon_id = 'chinese-alphabet-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('chinese', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 12), (34, 12))
        self.add_line('sym-e1', (34, 12), (24, 12))
        self.add_line('sym-e2', (24, 12), (14, 12))
        self.add_line('sym-e3', (14, 12), (6, 12))
        self.add_line('sym-e4', (24, 6), (24, 12))
        self.add_arc('sym-e5', (34, 12), (29, 25), radius_x=42)
        self.add_line('sym-e6', (29, 25), (24, 32))
        self.add_arc('sym-e7', (24, 32), (19, 25), radius_x=35)
        self.add_arc('sym-e8', (19, 25), (14, 12), radius_x=42)
        self.add_arc('sym-e9', (24, 31), (42, 42), radius_x=39, sweep=False)
        self.add_arc('sym-e10', (24, 31), (6, 42), radius_x=40)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c3', 'sym-e9')
        self.add_contour('sym-c4', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
