"""Bathroom robe female (spas), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96d753e-96ad-5e09-8189-08d080845f4b'
SOURCE_PATH = 'icons-json/spas/bathroom robe female_b96d753e-96ad-5e09-8189-08d080845f4b.json'
AUTHOR = 'json_to_solo'

class BathroomRobeFemaleSpas(Solo48):
    icon_id = 'bathroom-robe-female-spas'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('bathroom', 'robe', 'female', 'spas')

    def build(self):
        self.add_line('e0', (34, 34), (34, 39))
        self.add_line('e1', (27, 44), (16, 44))
        self.add_line('e2', (15, 32), (16, 25))
        self.add_line('e3', (32, 25), (27, 25))
        self.add_line('e4', (27, 25), (27, 44))
        self.add_line('e5', (32, 25), (32, 16))
        self.add_line('e6', (27, 25), (16, 25))
        self.add_line('e7', (8, 30), (12, 9))
        self.add_line('e8', (19, 4), (28, 4))
        self.add_line('e9', (36, 10), (40, 31))
        self.add_line('e10', (40, 31), (34, 34))
        self.add_line('e11', (16, 25), (16, 16))
        self.add_line('e12', (30, 4), (24, 17))
        self.add_arc('e13', (32, 25), (34, 34), radius_x=47, sweep=False)
        self.add_line('e14-1', (34, 39), (34, 43))
        self.add_line('e14-2', (34, 43), (27, 44))
        self.add_arc('e15-1', (16, 44), (14, 42), radius_x=2)
        self.add_arc('e15-2', (14, 42), (15, 32), radius_x=14)
        self.add_line('e16-1', (18, 4), (27, 23))
        self.add_arc('e16-2', (27, 23), (27, 25), radius_x=21, sweep=False)
        self.add_arc('e17', (14, 34), (8, 30), radius_x=21)
        self.add_arc('e18-1', (12, 9), (18, 4), radius_x=7)
        self.add_arc('e18-2', (18, 4), (19, 4), radius_x=44, sweep=False)
        self.add_line('e19-1', (28, 4), (32, 5))
        self.add_arc('e19-2', (32, 5), (36, 10), radius_x=8)
        self.add_contour('c0', 'e13', 'e0', 'e14-1', 'e14-2', 'e1', 'e15-1', 'e15-2', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e16-1', 'e16-2', 'e6')
        self.add_contour('c4', 'e17', 'e7', 'e18-1', 'e18-2', 'e8', 'e19-1', 'e19-2', 'e9', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e12')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c6', 'c4')
        self.relate('connect', 'c6', 'c3')
