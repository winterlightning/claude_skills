"""Layout (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '309fb1e3-e1dd-4884-9491-8855823b712b'
SOURCE_PATH = 'icons-json/interface-essential/layout_309fb1e3-e1dd-4884-9491-8855823b712b.json'
AUTHOR = 'json_to_solo'

class LayoutInterfaceEssential(Solo48):
    icon_id = 'layout-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 25), (42, 25))
        self.add_line('e1', (24, 25), (24, 42))
        self.add_line('e2', (24, 25), (24, 6))
        self.add_line('e3', (42, 25), (42, 40))
        self.add_line('e4', (40, 42), (24, 42))
        self.add_line('e5', (42, 25), (42, 8))
        self.add_line('e6', (40, 6), (24, 6))
        self.add_line('e7', (24, 42), (8, 42))
        self.add_line('e8', (6, 40), (6, 9))
        self.add_line('e9', (8, 6), (24, 6))
        self.add_bezier('e10', (42, 40), ((42, 40.965), (40.658, 41.992), (39.66, 41.992)), ((39.619, 41.992), (40.041, 42), (40, 42)))
        self.add_bezier('e11', (42, 8), ((41.64, 6.879), (41.407, 6), (40, 6)))
        self.add_bezier('e12', (8, 42), ((6.691, 42), (6.385, 41.006), (6, 40)))
        self.add_bezier('e13', (6, 9), ((6, 8.943), (6, 9.15), (6, 9.093)), ((6, 8.029), (6.822, 6), (8, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e10', 'e4')
        self.add_contour('c4', 'e5', 'e11', 'e6')
        self.add_contour('c5', 'e7', 'e12', 'e8', 'e13', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
