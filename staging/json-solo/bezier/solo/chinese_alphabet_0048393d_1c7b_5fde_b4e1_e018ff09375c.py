"""Chinese alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e5', (34, 12), ((33.092, 16.59), (31.365, 20.925), (29, 25)))
        self.add_bezier('sym-e6', (29, 25), ((27.556, 27.488), (25.987, 29.969), (24, 32)))
        self.add_bezier('sym-e7', (24, 32), ((22.013, 29.969), (20.444, 27.488), (19, 25)))
        self.add_bezier('sym-e8', (19, 25), ((16.635, 20.925), (14.908, 16.59), (14, 12)))
        self.add_bezier('sym-e9', (24, 31), ((28.658, 35.88), (34.728, 39.929), (42, 42)))
        self.add_bezier('sym-e10', (24, 31), ((19.342, 35.88), (13.272, 39.929), (6, 42)))
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
