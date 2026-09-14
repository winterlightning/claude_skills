"""Layout 5 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00a510ed-d94a-4187-aafa-6dd3cdcc5eed'
SOURCE_PATH = 'icons-json/interface-essential/layout 5_00a510ed-d94a-4187-aafa-6dd3cdcc5eed.json'
AUTHOR = 'json_to_solo'

class Layout5InterfaceEssential(Solo48):
    icon_id = 'layout-5-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 32), (44, 32))
        self.add_line('e1', (24, 32), (24, 40))
        self.add_line('e2', (24, 32), (24, 24))
        self.add_line('e3', (24, 24), (44, 24))
        self.add_line('e4', (24, 24), (24, 16))
        self.add_line('e5', (44, 24), (44, 32))
        self.add_line('e6', (44, 24), (44, 16))
        self.add_line('e7', (24, 16), (44, 16))
        self.add_line('e8', (24, 16), (24, 8))
        self.add_line('e9', (44, 32), (44, 37))
        self.add_line('e10', (41, 40), (24, 40))
        self.add_line('e11', (24, 40), (7, 40))
        self.add_line('e12', (4, 37), (4, 10))
        self.add_line('e13', (7, 8), (24, 8))
        self.add_line('e14', (44, 16), (44, 10))
        self.add_line('e15', (41, 8), (24, 8))
        self.add_bezier('e16', (44, 37), ((43.4, 38.448), (42.555, 39.402), (41, 40)))
        self.add_bezier('e17', (7, 40), ((6.073, 39.646), (4.018, 38.728), (4.018, 37.583)), ((4.009, 37.549), (4.009, 37.034), (4, 37)))
        self.add_bezier('e18', (4, 10), ((4.573, 9.133), (5.336, 8.008), (6.564, 8.008)), ((6.618, 8.008), (6.945, 8), (7, 8)))
        self.add_bezier('e19', (44, 10), ((43.882, 9.848), (43.891, 9.347), (43.764, 9.196)), ((43.091, 8.421), (41.973, 8.202), (41, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9', 'e16', 'e10')
        self.add_contour('c10', 'e11', 'e17', 'e12', 'e18', 'e13')
        self.add_contour('c11', 'e14', 'e19', 'e15')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c11', 'c6')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c11', 'c8')
