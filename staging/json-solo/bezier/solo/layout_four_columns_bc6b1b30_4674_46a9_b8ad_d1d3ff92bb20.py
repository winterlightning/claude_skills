"""Layout four columns (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20'
SOURCE_PATH = 'icons-json/interface-essential/layout four columns_bc6b1b30-4674-46a9-b8ad-d1d3ff92bb20.json'
AUTHOR = 'json_to_solo'

class LayoutFourColumnsInterfaceEssential(Solo48):
    icon_id = 'layout-four-columns-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'four', 'columns', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (18, 6), (18, 42))
        self.add_line('sym-e1', (18, 42), (30, 42))
        self.add_line('sym-e2', (30, 42), (30, 6))
        self.add_line('sym-e3', (30, 6), (18, 6))
        self.add_line('sym-e4', (18, 6), (8, 6))
        self.add_bezier('sym-e5', (8, 6), ((7.092, 6.352), (6, 6.814), (6, 8)))
        self.add_bezier('sym-e6', (6, 8), ((6, 8.025), (6, 7.975), (6, 8)))
        self.add_line('sym-e7', (6, 8), (6, 24))
        self.add_line('sym-e8', (6, 24), (6, 40))
        self.add_bezier('sym-e9', (6, 40), ((6, 40.025), (6, 39.975), (6, 40)))
        self.add_bezier('sym-e10', (6, 40), ((6, 41.186), (7.092, 41.648), (8, 42)))
        self.add_line('sym-e11', (8, 42), (18, 42))
        self.add_line('sym-e12', (30, 6), (40, 6))
        self.add_bezier('sym-e13', (40, 6), ((40.908, 6.352), (42, 6.814), (42, 8)))
        self.add_bezier('sym-e14', (42, 8), ((42, 8.025), (42, 7.975), (42, 8)))
        self.add_line('sym-e15', (42, 8), (42, 24))
        self.add_line('sym-e16', (42, 24), (42, 40))
        self.add_bezier('sym-e17', (42, 40), ((42, 40.025), (42, 39.975), (42, 40)))
        self.add_bezier('sym-e18', (42, 40), ((42, 41.186), (40.908, 41.648), (40, 42)))
        self.add_line('sym-e19', (40, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
