"""Layout 15 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9fe05bf-2f0b-4d8e-9c4d-0df06cd7b99b'
SOURCE_PATH = 'icons-json/interface-essential/layout 15_f9fe05bf-2f0b-4d8e-9c4d-0df06cd7b99b.json'
AUTHOR = 'json_to_solo'

class Layout15InterfaceEssential(Solo48):
    icon_id = 'layout-15-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 16), (18, 16))
        self.add_line('sym-e1', (18, 16), (18, 42))
        self.add_line('sym-e2', (18, 42), (30, 42))
        self.add_line('sym-e3', (30, 42), (30, 16))
        self.add_line('sym-e4', (30, 16), (42, 16))
        self.add_line('sym-e5', (42, 16), (42, 40))
        self.add_bezier('sym-e6', (42, 40), ((42, 41.047), (41.055, 42), (40, 42)))
        self.add_line('sym-e7', (40, 42), (30, 42))
        self.add_line('sym-e8', (42, 16), (42, 8))
        self.add_bezier('sym-e9', (42, 8), ((42, 6.814), (40.933, 6.352), (40, 6)))
        self.add_line('sym-e10', (40, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (8, 6))
        self.add_bezier('sym-e12', (8, 6), ((7.067, 6.352), (6, 6.814), (6, 8)))
        self.add_line('sym-e13', (6, 8), (6, 16))
        self.add_line('sym-e14', (6, 16), (18, 16))
        self.add_line('sym-e15', (18, 42), (8, 42))
        self.add_bezier('sym-e16', (8, 42), ((6.945, 42), (6, 41.047), (6, 40)))
        self.add_line('sym-e17', (6, 40), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c2', 'sym-e15', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
