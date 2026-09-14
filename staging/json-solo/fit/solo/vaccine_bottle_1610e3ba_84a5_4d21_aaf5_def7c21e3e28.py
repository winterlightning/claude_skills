"""Vaccine bottle (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1610e3ba-84a5-4d21-aaf5-def7c21e3e28'
SOURCE_PATH = 'icons-json/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.json'
AUTHOR = 'json_to_solo'

class VaccineBottleHealth(Solo48):
    icon_id = 'vaccine-bottle-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('vaccine', 'bottle', 'health')

    def build(self):
        self.add_line('e0', (14, 4), (34, 4))
        self.add_line('e1', (30, 4), (30, 9))
        self.add_line('e2', (31, 9), (35, 11))
        self.add_line('e3', (40, 16), (40, 24))
        self.add_line('e4', (18, 4), (18, 9))
        self.add_line('e5', (17, 9), (12, 11))
        self.add_line('e6', (8, 17), (8, 23))
        self.add_line('e7', (22, 23), (26, 25))
        self.add_line('e8', (38, 25), (40, 24))
        self.add_line('e9', (8, 23), (8, 40))
        self.add_line('e10', (14, 44), (35, 44))
        self.add_line('e11', (40, 40), (40, 24))
        self.add_arc('e12', (30, 9), (31, 9), radius_x=26)
        self.add_arc('e13', (35, 11), (40, 16), radius_x=9)
        self.add_arc('e14', (18, 9), (17, 9), radius_x=10, sweep=False)
        self.add_arc('e15', (12, 11), (8, 17), radius_x=8, sweep=False)
        self.add_arc('e16', (8, 23), (22, 23), radius_x=24)
        self.add_arc('e17', (26, 25), (38, 25), radius_x=19, sweep=False)
        self.add_arc('e18', (8, 40), (14, 44), radius_x=7, sweep=False)
        self.add_arc('e19', (35, 44), (40, 40), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e12', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6')
        self.add_contour('c3', 'e16', 'e7', 'e17', 'e8')
        self.add_contour('c4', 'e9', 'e18', 'e10', 'e19', 'e11')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
