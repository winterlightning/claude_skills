"""Layout 6 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a299b5ca-1eed-416f-a091-4bb307b869ec'
SOURCE_PATH = 'icons-json/interface-essential/layout 6_a299b5ca-1eed-416f-a091-4bb307b869ec.json'
AUTHOR = 'json_to_solo'

class Layout6InterfaceEssential(Solo48):
    icon_id = 'layout-6-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 24), (18, 24))
        self.add_line('sym-e1', (18, 24), (18, 42))
        self.add_line('sym-e2', (18, 42), (30, 42))
        self.add_line('sym-e3', (30, 42), (30, 24))
        self.add_line('sym-e4', (30, 24), (42, 24))
        self.add_line('sym-e5', (42, 24), (42, 40))
        self.add_bezier('sym-e6', (42, 40), ((41.468, 41.415), (41.375, 41.444), (40, 42)))
        self.add_line('sym-e7', (40, 42), (30, 42))
        self.add_line('sym-e8', (42, 24), (42, 8))
        self.add_bezier('sym-e9', (42, 8), ((41.926, 7.812), (42, 8.188), (42, 8)))
        self.add_bezier('sym-e10', (42, 8), ((41.599, 7.141), (41.031, 6), (40, 6)))
        self.add_line('sym-e11', (40, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (8, 6))
        self.add_bezier('sym-e13', (8, 6), ((6.969, 6), (6.401, 7.141), (6, 8)))
        self.add_bezier('sym-e14', (6, 8), ((6, 8.188), (6.074, 7.812), (6, 8)))
        self.add_line('sym-e15', (6, 8), (6, 24))
        self.add_line('sym-e16', (6, 24), (18, 24))
        self.add_line('sym-e17', (18, 42), (8, 42))
        self.add_bezier('sym-e18', (8, 42), ((6.625, 41.444), (6.532, 41.415), (6, 40)))
        self.add_line('sym-e19', (6, 40), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19')
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
