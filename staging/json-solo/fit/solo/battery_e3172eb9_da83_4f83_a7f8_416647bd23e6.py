"""Battery (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3172eb9-da83-4f83-a7f8-416647bd23e6'
SOURCE_PATH = 'icons-json/photography/battery_e3172eb9-da83-4f83-a7f8-416647bd23e6.json'
AUTHOR = 'json_to_solo'

class BatteryE3172eb9(Solo48):
    icon_id = 'battery-e3172eb9'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography')

    def build(self):
        self.add_line('e0', (44, 19), (44, 29))
        self.add_line('e1', (42, 31), (37, 31))
        self.add_line('e2', (36, 17), (36, 31))
        self.add_line('e3', (36, 17), (36, 10))
        self.add_line('e4', (33, 8), (29, 8))
        self.add_line('e5', (29, 8), (31, 8))
        self.add_line('e6', (31, 8), (6, 8))
        self.add_line('e7', (4, 10), (4, 38))
        self.add_line('e8', (6, 40), (31, 40))
        self.add_line('e9', (31, 40), (29, 40))
        self.add_line('e10', (29, 40), (33, 40))
        self.add_line('e11', (36, 38), (36, 31))
        self.add_arc('e12', (37, 17), (44, 19), radius_x=5)
        self.add_arc('e13', (44, 29), (42, 31), radius_x=2)
        self.add_line('e14', (36, 10), (33, 8))
        self.add_line('e15', (6, 8), (4, 10))
        self.add_line('e16', (4, 38), (6, 40))
        self.add_line('e17', (33, 40), (36, 38))
        self.add_arc('e18', (36, 17), (37, 17), radius_x=48)
        self.add_arc('e19', (36, 31), (37, 31), radius_x=37, sweep=False)
        self.add_contour('c0', 'e12', 'e0', 'e13', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e14', 'e4', 'e5', 'e6', 'e15', 'e7', 'e16', 'e8', 'e9', 'e10', 'e17', 'e11')
        self.add_contour('c3', 'e18')
        self.add_contour('c4', 'e19')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
