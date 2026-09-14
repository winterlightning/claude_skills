"""Cyrillic alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e10e748f-638c-5583-88b9-695922930c2d'
SOURCE_PATH = 'icons-json/interface-essential/cyrillic alphabet_e10e748f-638c-5583-88b9-695922930c2d.json'
AUTHOR = 'json_to_solo'

class CyrillicAlphabet(Solo48):
    icon_id = 'cyrillic-alphabet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cyrillic', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 4), (40, 4))
        self.add_line('e1', (16, 33), (13, 40))
        self.add_line('e2', (22, 26), (35, 26))
        self.add_line('e3', (35, 44), (35, 4))
        self.add_line('e4', (31, 44), (40, 44))
        self.add_arc('e5-1', (22, 26), (11, 14), radius_x=11)
        self.add_arc('e5-2', (11, 14), (21, 4), radius_x=11)
        self.add_arc('e6', (22, 26), (16, 33), radius_x=20, sweep=False)
        self.add_arc('e7', (13, 40), (8, 44), radius_x=7)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e7')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c0')
