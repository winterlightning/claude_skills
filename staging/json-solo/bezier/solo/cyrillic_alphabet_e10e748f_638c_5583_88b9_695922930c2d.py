"""Cyrillic alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e10e748f-638c-5583-88b9-695922930c2d'
SOURCE_PATH = 'icons-json/interface-essential/cyrillic alphabet_e10e748f-638c-5583-88b9-695922930c2d.json'
AUTHOR = 'json_to_solo'

class CyrillicAlphabetInterfaceEssential(Solo48):
    icon_id = 'cyrillic-alphabet-interface-essential'
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
        self.add_bezier('e5', (22, 26), ((21.05, 25.818), (20.11, 25.445), (19.16, 25.264)), ((16.91, 24.809), (14.85, 23.536), (13.43, 21.9)), ((9.06, 16.873), (10.29, 9), (16.41, 5.618)), ((17.26, 5.145), (20.12, 4), (21, 4)))
        self.add_bezier('e6', (22, 26), ((19.56, 28.109), (17.21, 30.073), (16, 33)))
        self.add_bezier('e7', (13, 40), ((12.21, 41.909), (9.94, 43.291), (8, 44)))
        self.add_contour('c0', 'e5', 'e0')
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
