"""Reality vr (technology), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0284d3a8-c0bf-450e-8702-f6e30af3b263'
SOURCE_PATH = 'icons-json/technology/reality vr_0284d3a8-c0bf-450e-8702-f6e30af3b263.json'
AUTHOR = 'json_to_solo'

class RealityVr(Solo48):
    icon_id = 'reality-vr'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('reality', 'vr', 'technology')

    def build(self):
        self.add_line('e0', (9, 29), (18, 29))
        self.add_line('e1', (30, 29), (38, 29))
        self.add_line('e2', (6, 26), (6, 17))
        self.add_line('e3', (8, 13), (10, 13))
        self.add_line('e4', (40, 29), (41, 28))
        self.add_line('e5', (42, 26), (42, 17))
        self.add_line('e6', (38, 13), (10, 13))
        self.add_line('e7', (28, 6), (20, 6))
        self.add_arc('e8-1', (18, 29), (24, 27), radius_x=7)
        self.add_arc('e8-2', (24, 27), (30, 29), radius_x=7)
        self.add_line('e9', (38, 29), (40, 29))
        self.add_arc('e10-1', (9, 29), (14, 38), radius_x=15, sweep=False)
        self.add_arc('e10-2', (14, 38), (24, 42), radius_x=15, sweep=False)
        self.add_line('e10-3', (24, 42), (32, 40))
        self.add_arc('e10-4', (32, 40), (40, 29), radius_x=17, sweep=False)
        self.add_arc('e11', (9, 29), (6, 26), radius_x=4)
        self.add_line('e12', (6, 17), (8, 13))
        self.add_line('e13', (41, 28), (42, 26))
        self.add_arc('e14', (42, 17), (38, 13), radius_x=4, sweep=False)
        self.add_arc('e15', (38, 13), (28, 6), radius_x=11, sweep=False)
        self.add_arc('e16', (20, 6), (10, 13), radius_x=11, sweep=False)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1', 'e9')
        self.add_contour('c1', 'e10-1', 'e10-2', 'e10-3', 'e10-4')
        self.add_contour('c2', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5', 'e14')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e15', 'e7', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
