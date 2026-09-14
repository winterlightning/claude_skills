"""Layout three columns (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c319a64-cc6e-446f-8ebb-83acb449fdc8'
SOURCE_PATH = 'icons-json/interface-essential/layout three columns_6c319a64-cc6e-446f-8ebb-83acb449fdc8.json'
AUTHOR = 'json_to_solo'

class LayoutThreeColumnsInterfaceEssential(Solo48):
    icon_id = 'layout-three-columns-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'three', 'columns', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (18, 8), (18, 40))
        self.add_line('sym-e1', (18, 40), (30, 40))
        self.add_line('sym-e2', (30, 40), (30, 8))
        self.add_line('sym-e3', (30, 8), (18, 8))
        self.add_line('sym-e4', (18, 8), (8, 8))
        self.add_bezier('sym-e5', (8, 8), ((6.636, 8), (4, 9.695), (4, 11)))
        self.add_bezier('sym-e6', (4, 11), ((4, 11.034), (4, 10.966), (4, 11)))
        self.add_line('sym-e7', (4, 11), (4, 24))
        self.add_line('sym-e8', (4, 24), (4, 37))
        self.add_bezier('sym-e9', (4, 37), ((4, 37.034), (4, 36.966), (4, 37)))
        self.add_bezier('sym-e10', (4, 37), ((4, 38.305), (6.636, 40), (8, 40)))
        self.add_line('sym-e11', (8, 40), (18, 40))
        self.add_line('sym-e12', (30, 8), (40, 8))
        self.add_bezier('sym-e13', (40, 8), ((41.364, 8), (44, 9.695), (44, 11)))
        self.add_bezier('sym-e14', (44, 11), ((44, 11.034), (44, 10.966), (44, 11)))
        self.add_line('sym-e15', (44, 11), (44, 24))
        self.add_line('sym-e16', (44, 24), (44, 37))
        self.add_bezier('sym-e17', (44, 37), ((44, 37.034), (44, 36.966), (44, 37)))
        self.add_bezier('sym-e18', (44, 37), ((44, 38.305), (41.364, 40), (40, 40)))
        self.add_line('sym-e19', (40, 40), (30, 40))
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
