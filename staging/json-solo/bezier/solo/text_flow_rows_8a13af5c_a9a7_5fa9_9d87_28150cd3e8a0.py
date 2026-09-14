"""Text flow rows (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0'
SOURCE_PATH = 'icons-json/interface-essential/text flow rows_8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0.json'
AUTHOR = 'json_to_solo'

class TextFlowRowsInterfaceEssential(Solo48):
    icon_id = 'text-flow-rows-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'flow', 'rows', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 18), (35, 18))
        self.add_line('e1', (35, 18), (40, 18))
        self.add_line('e2', (42, 15), (42, 8))
        self.add_line('e3', (40, 6), (32, 6))
        self.add_line('e4', (31, 8), (31, 13))
        self.add_line('e5', (31, 13), (31, 18))
        self.add_line('e6', (31, 18), (18, 31))
        self.add_line('e7', (16, 30), (8, 30))
        self.add_line('e8', (6, 32), (6, 40))
        self.add_line('e9', (8, 42), (15, 42))
        self.add_line('e10', (17, 40), (17, 31))
        self.add_line('e11', (31, 12), (17, 12))
        self.add_line('e12', (17, 36), (42, 36))
        self.add_line('e13', (42, 36), (37, 41))
        self.add_line('e14', (37, 31), (42, 35))
        self.add_line('e15', (16, 6), (8, 6))
        self.add_line('e16', (6, 8), (6, 16))
        self.add_line('e17', (8, 18), (16, 18))
        self.add_line('e18', (17, 16), (17, 8))
        self.add_bezier('e19', (40, 18), ((40.884, 18), (41.992, 17.283), (41.992, 16.465)), ((41.992, 16.186), (42, 15.908), (42, 15.622)), ((42, 15.417), (42, 15.205), (42, 15)))
        self.add_bezier('e20', (42, 8), ((42, 6.985), (40.761, 6.303), (40, 6)))
        self.add_bezier('e21', (32, 6), ((31.075, 6), (31, 7.075), (31, 8)))
        self.add_bezier('e22', (17, 31), ((16.476, 30.575), (16.712, 30), (16, 30)))
        self.add_bezier('e23', (8, 30), ((6.724, 30), (6, 30.529), (6, 31.904)), ((6, 32.002), (6, 31.91), (6, 32)))
        self.add_bezier('e24', (6, 40), ((6, 40.18), (6, 39.897), (6, 40.077)), ((6, 41.059), (7.105, 41.984), (8.062, 41.984)), ((8.127, 41.992), (8.193, 41.992), (8.258, 42)), ((8.324, 42), (7.935, 42), (8, 42)))
        self.add_bezier('e25', (15, 42), ((15.18, 42), (15.352, 41.992), (15.524, 41.992)), ((16.882, 41.992), (17, 41.162), (17, 40)))
        self.add_bezier('e26', (17, 8), ((17, 7.059), (17.135, 6.736), (16.366, 6.188)), ((16.195, 6.074), (16.18, 6.098), (16, 6)))
        self.add_bezier('e27', (8, 6), ((7.91, 6), (8.275, 6), (8.185, 6)), ((6.925, 6), (6.008, 6.949), (6.008, 8.201)), ((6, 8.283), (6, 7.918), (6, 8)))
        self.add_bezier('e28', (6, 16), ((6, 16.131), (6, 16.08), (6.008, 16.211)), ((6.008, 17.144), (6.826, 18.117), (7.726, 18.297)), ((7.988, 18.355), (7.746, 18), (8, 18)))
        self.add_bezier('e29', (16, 18), ((17.685, 18), (17, 17.342), (17, 16)))
        self.add_contour('c0', 'e0', 'e1', 'e19', 'e2', 'e20', 'e3', 'e21', 'e4', 'e5', closed=True)
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e22', 'e7', 'e23', 'e8', 'e24', 'e9', 'e25', 'e10')
        self.add_contour('c3', 'e11')
        self.add_contour('c4', 'e12', 'e13')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e26', 'e15', 'e27', 'e16', 'e28', 'e17', 'e29', 'e18', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c2')
