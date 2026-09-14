"""Text flow columns (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02d53e70-609c-4226-aae6-46408f1a470b'
SOURCE_PATH = 'icons-json/interface-essential/text flow columns_02d53e70-609c-4226-aae6-46408f1a470b.json'
AUTHOR = 'json_to_solo'

class TextFlowColumnsInterfaceEssential(Solo48):
    icon_id = 'text-flow-columns-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'flow', 'columns', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 35), (36, 40))
        self.add_line('e1', (41, 35), (36, 40))
        self.add_line('e2', (17, 31), (12, 31))
        self.add_line('e3', (17, 31), (18, 32))
        self.add_line('e4', (18, 32), (18, 40))
        self.add_line('e5', (17, 42), (8, 42))
        self.add_line('e6', (6, 40), (6, 32))
        self.add_line('e7', (8, 31), (12, 31))
        self.add_line('e8', (30, 17), (36, 17))
        self.add_line('e9', (30, 17), (30, 7))
        self.add_line('e10', (31, 6), (40, 6))
        self.add_line('e11', (42, 8), (42, 17))
        self.add_line('e12', (40, 17), (36, 17))
        self.add_line('e13', (17, 30), (29, 17))
        self.add_line('e14', (12, 31), (12, 17))
        self.add_line('e15', (36, 17), (36, 40))
        self.add_line('e16', (18, 17), (18, 8))
        self.add_line('e17', (17, 6), (8, 6))
        self.add_line('e18', (6, 8), (6, 16))
        self.add_line('e19', (8, 17), (17, 17))
        self.add_arc('e20', (18, 40), (17, 42), radius_x=2)
        self.add_arc('e21', (8, 42), (6, 40), radius_x=2)
        self.add_arc('e22', (6, 32), (8, 31), radius_x=2)
        self.add_line('e23', (30, 7), (31, 6))
        self.add_arc('e24', (40, 6), (42, 8), radius_x=2)
        self.add_line('e25', (42, 17), (40, 17))
        self.add_arc('e26', (18, 8), (17, 6), radius_x=2, sweep=False)
        self.add_arc('e27', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_arc('e28', (6, 16), (8, 17), radius_x=2, sweep=False)
        self.add_arc('e29', (17, 17), (18, 17), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e20', 'e5', 'e21', 'e6', 'e22', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9', 'e23', 'e10', 'e24', 'e11', 'e25', 'e12')
        self.add_contour('c6', 'e13')
        self.add_contour('c7', 'e14')
        self.add_contour('c8', 'e15')
        self.add_contour('c9', 'e16', 'e26', 'e17', 'e27', 'e18', 'e28', 'e19', 'e29', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c9')
