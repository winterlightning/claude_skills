"""Layout 8 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '968ebc82-99c6-4e6a-8713-e6c0ea0278cd'
SOURCE_PATH = 'icons-json/interface-essential/layout 8_968ebc82-99c6-4e6a-8713-e6c0ea0278cd.json'
AUTHOR = 'json_to_solo'

class Layout8InterfaceEssential(Solo48):
    icon_id = 'layout-8-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 30), (6, 18))
        self.add_line('sym-e1', (6, 18), (6, 8))
        self.add_bezier('sym-e2', (6, 8), ((6.368, 6.985), (6.691, 6), (8, 6)))
        self.add_line('sym-e3', (8, 6), (18, 6))
        self.add_line('sym-e4', (18, 6), (30, 6))
        self.add_line('sym-e5', (30, 6), (30, 18))
        self.add_line('sym-e6', (30, 18), (30, 30))
        self.add_line('sym-e7', (30, 30), (18, 30))
        self.add_line('sym-e8', (18, 30), (18, 18))
        self.add_line('sym-e9', (18, 18), (30, 18))
        self.add_line('sym-e10', (30, 18), (42, 18))
        self.add_line('sym-e11', (42, 18), (42, 30))
        self.add_line('sym-e12', (42, 30), (42, 40))
        self.add_bezier('sym-e13', (42, 40), ((41.632, 41.015), (41.309, 42), (40, 42)))
        self.add_line('sym-e14', (40, 42), (30, 42))
        self.add_line('sym-e15', (30, 42), (18, 42))
        self.add_line('sym-e16', (18, 42), (18, 30))
        self.add_line('sym-e17', (18, 30), (6, 30))
        self.add_line('sym-e18', (6, 30), (6, 40))
        self.add_bezier('sym-e19', (6, 40), ((6.368, 41.015), (6.691, 42), (8, 42)))
        self.add_line('sym-e20', (8, 42), (18, 42))
        self.add_line('sym-e21', (30, 42), (30, 30))
        self.add_line('sym-e22', (30, 30), (42, 30))
        self.add_line('sym-e23', (18, 6), (18, 18))
        self.add_line('sym-e24', (18, 18), (6, 18))
        self.add_line('sym-e25', (30, 6), (40, 6))
        self.add_bezier('sym-e26', (40, 6), ((41.309, 6), (41.632, 6.985), (42, 8)))
        self.add_line('sym-e27', (42, 8), (42, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c1', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c3', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
