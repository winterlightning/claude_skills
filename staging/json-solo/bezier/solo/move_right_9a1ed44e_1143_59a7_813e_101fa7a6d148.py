"""Move right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a1ed44e-1143-59a7-813e-101fa7a6d148'
SOURCE_PATH = 'icons-json/interface-essential/move right_9a1ed44e-1143-59a7-813e-101fa7a6d148.json'
AUTHOR = 'json_to_solo'

class MoveRightInterfaceEssential(Solo48):
    icon_id = 'move-right-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'right', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (44, 24), (24, 24))
        self.add_line('sym-e1', (37, 16), (44, 24))
        self.add_line('sym-e2', (44, 24), (37, 32))
        self.add_line('sym-e3', (7, 8), (12, 8))
        self.add_bezier('sym-e4', (12, 8), ((12.136, 8), (12.864, 8), (13, 8)))
        self.add_bezier('sym-e5', (13, 8), ((14.445, 8), (16, 9.22), (16, 11)))
        self.add_line('sym-e6', (16, 11), (16, 24))
        self.add_line('sym-e7', (16, 24), (16, 37))
        self.add_bezier('sym-e8', (16, 37), ((16, 38.78), (14.445, 40), (13, 40)))
        self.add_bezier('sym-e9', (13, 40), ((12.864, 40), (12.136, 40), (12, 40)))
        self.add_line('sym-e10', (12, 40), (7, 40))
        self.add_bezier('sym-e11', (7, 40), ((5.7, 40), (4, 38.4), (4, 37)))
        self.add_line('sym-e12', (4, 37), (4, 24))
        self.add_line('sym-e13', (4, 24), (4, 11))
        self.add_bezier('sym-e14', (4, 11), ((4, 9.6), (5.7, 8), (7, 8)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
