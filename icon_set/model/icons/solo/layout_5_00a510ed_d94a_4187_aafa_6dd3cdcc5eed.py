"""Layout 5 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00a510ed-d94a-4187-aafa-6dd3cdcc5eed'
SOURCE_PATH = 'icons-json/interface-essential/layout 5_00a510ed-d94a-4187-aafa-6dd3cdcc5eed.json'
AUTHOR = 'json_to_solo'

class Layout5(Solo48):
    icon_id = 'layout-5'
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
        self.add_arc('e16', (44, 37), (41, 40), radius_x=3)
        self.add_arc('e17', (7, 40), (4, 37), radius_x=3)
        self.add_line('e18', (4, 10), (7, 8))
        self.add_line('e19', (44, 10), (41, 8))
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
