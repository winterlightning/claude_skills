"""Airchair (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e130f83-d8c1-50d3-98ae-5ea5bac53dab'
SOURCE_PATH = 'icons-json/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.json'
AUTHOR = 'json_to_solo'

class Airchair(Solo48):
    icon_id = 'airchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('airchair', 'symbol')

    def build(self):
        self.add_line('sym-e0', (11, 44), (13, 35))
        self.add_line('sym-e1', (13, 35), (35, 35))
        self.add_line('sym-e2', (35, 35), (37, 44))
        self.add_line('sym-e3', (24, 4), (21, 4))
        self.add_arc('sym-e5', (21, 4), (12, 13), radius_x=11, sweep=False)
        self.add_line('sym-e6', (12, 13), (12, 19))
        self.add_arc('sym-e7', (12, 19), (15, 20), radius_x=4)
        self.add_arc('sym-e8', (15, 20), (16, 21), radius_x=4, sweep=False)
        self.add_line('sym-e9', (16, 21), (16, 27))
        self.add_line('sym-e10', (16, 27), (24, 27))
        self.add_line('sym-e11', (24, 27), (32, 27))
        self.add_line('sym-e12', (32, 27), (32, 21))
        self.add_arc('sym-e13', (32, 21), (33, 20), radius_x=4, sweep=False)
        self.add_arc('sym-e14', (33, 20), (36, 19), radius_x=4)
        self.add_line('sym-e15', (36, 19), (36, 13))
        self.add_arc('sym-e16', (36, 13), (27, 4), radius_x=11, sweep=False)
        self.add_line('sym-e18', (27, 4), (24, 4))
        self.add_line('sym-e19', (12, 19), (10, 19))
        self.add_arc('sym-e20', (10, 19), (8, 20), radius_x=2, sweep=False)
        self.add_line('sym-e23', (8, 20), (8, 21))
        self.add_line('sym-e26', (8, 21), (10, 30))
        self.add_arc('sym-e27', (10, 30), (13, 35), radius_x=4, sweep=False)
        self.add_line('sym-e28', (36, 19), (38, 19))
        self.add_arc('sym-e29', (38, 19), (40, 20), radius_x=2)
        self.add_arc('sym-e32', (40, 20), (40, 21), radius_x=25, sweep=False)
        self.add_line('sym-e35', (40, 21), (38, 30))
        self.add_arc('sym-e36', (38, 30), (35, 35), radius_x=4)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', closed=True)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', 'sym-e23', 'sym-e26', 'sym-e27')
        self.add_contour('sym-c3', 'sym-e28', 'sym-e29', 'sym-e32', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
