"""Table tools (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb0d6e1-411d-459c-b0d6-73e65e4e8c15'
SOURCE_PATH = 'icons-json/interface-essential/table tools_adb0d6e1-411d-459c-b0d6-73e65e4e8c15.json'
AUTHOR = 'json_to_solo'

class TableToolsInterfaceEssential(Solo48):
    icon_id = 'table-tools-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'tools', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (31, 40), (17, 40))
        self.add_line('sym-e1', (17, 40), (7, 40))
        self.add_bezier('sym-e2', (7, 40), ((5.664, 40), (4.382, 38.15), (4, 37)))
        self.add_line('sym-e3', (4, 37), (4, 29))
        self.add_line('sym-e4', (4, 29), (17, 29))
        self.add_line('sym-e5', (17, 29), (31, 29))
        self.add_line('sym-e6', (31, 29), (44, 29))
        self.add_line('sym-e7', (44, 29), (44, 37))
        self.add_bezier('sym-e8', (44, 37), ((43.618, 38.15), (42.336, 40), (41, 40)))
        self.add_line('sym-e9', (41, 40), (31, 40))
        self.add_line('sym-e10', (31, 40), (31, 29))
        self.add_line('sym-e11', (31, 29), (31, 18))
        self.add_line('sym-e12', (31, 18), (17, 18))
        self.add_line('sym-e13', (17, 18), (17, 29))
        self.add_line('sym-e14', (17, 29), (17, 40))
        self.add_line('sym-e15', (44, 29), (44, 18))
        self.add_line('sym-e16', (44, 18), (31, 18))
        self.add_line('sym-e17', (44, 18), (44, 11))
        self.add_bezier('sym-e18', (44, 11), ((43.936, 10.79), (44, 10.21), (44, 10)))
        self.add_bezier('sym-e19', (44, 10), ((43.609, 9.01), (42.082, 8), (41, 8)))
        self.add_line('sym-e20', (41, 8), (24, 8))
        self.add_line('sym-e21', (24, 8), (7, 8))
        self.add_bezier('sym-e22', (7, 8), ((5.918, 8), (4.391, 9.01), (4, 10)))
        self.add_bezier('sym-e23', (4, 10), ((4, 10.21), (4.064, 10.79), (4, 11)))
        self.add_line('sym-e24', (4, 11), (4, 18))
        self.add_line('sym-e25', (4, 18), (4, 29))
        self.add_line('sym-e26', (17, 18), (4, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.add_contour('sym-c3', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
