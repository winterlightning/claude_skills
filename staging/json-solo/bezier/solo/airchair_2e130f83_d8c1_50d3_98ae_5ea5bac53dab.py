"""Airchair (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e130f83-d8c1-50d3-98ae-5ea5bac53dab'
SOURCE_PATH = 'icons-json/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.json'
AUTHOR = 'json_to_solo'

class AirchairSymbol(Solo48):
    icon_id = 'airchair-symbol'
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
        self.add_bezier('sym-e4', (21, 4), ((20.907, 4), (21.093, 4), (21, 4)))
        self.add_bezier('sym-e5', (21, 4), ((17.008, 4), (12, 8.527), (12, 13)))
        self.add_line('sym-e6', (12, 13), (12, 19))
        self.add_bezier('sym-e7', (12, 19), ((13.053, 19), (14.436, 19.045), (15, 20)))
        self.add_bezier('sym-e8', (15, 20), ((15.177, 20.309), (15.882, 20.673), (16, 21)))
        self.add_line('sym-e9', (16, 21), (16, 27))
        self.add_line('sym-e10', (16, 27), (24, 27))
        self.add_line('sym-e11', (24, 27), (32, 27))
        self.add_line('sym-e12', (32, 27), (32, 21))
        self.add_bezier('sym-e13', (32, 21), ((32.118, 20.673), (32.823, 20.309), (33, 20)))
        self.add_bezier('sym-e14', (33, 20), ((33.564, 19.045), (34.947, 19), (36, 19)))
        self.add_line('sym-e15', (36, 19), (36, 13))
        self.add_bezier('sym-e16', (36, 13), ((36, 8.527), (30.992, 4), (27, 4)))
        self.add_bezier('sym-e17', (27, 4), ((26.907, 4), (27.093, 4), (27, 4)))
        self.add_line('sym-e18', (27, 4), (24, 4))
        self.add_line('sym-e19', (12, 19), (10, 19))
        self.add_bezier('sym-e20', (10, 19), ((9.368, 19.227), (8, 19.045), (8, 20)))
        self.add_bezier('sym-e21', (8, 20), ((8, 20.055), (8, 19.945), (8, 20)))
        self.add_bezier('sym-e22', (8, 20), ((8, 20.045), (8, 19.945), (8, 20)))
        self.add_bezier('sym-e23', (8, 20), ((8, 20.109), (8, 20.891), (8, 21)))
        self.add_bezier('sym-e24', (8, 21), ((8, 21.064), (8, 20.936), (8, 21)))
        self.add_bezier('sym-e25', (8, 21), ((8, 21.155), (8, 20.855), (8, 21)))
        self.add_line('sym-e26', (8, 21), (10, 30))
        self.add_bezier('sym-e27', (10, 30), ((10.455, 32.436), (10.709, 34.236), (13, 35)))
        self.add_line('sym-e28', (36, 19), (38, 19))
        self.add_bezier('sym-e29', (38, 19), ((38.632, 19.227), (40, 19.045), (40, 20)))
        self.add_bezier('sym-e30', (40, 20), ((40, 20.055), (40, 19.945), (40, 20)))
        self.add_bezier('sym-e31', (40, 20), ((40, 20.045), (40, 19.945), (40, 20)))
        self.add_bezier('sym-e32', (40, 20), ((40, 20.109), (40, 20.891), (40, 21)))
        self.add_bezier('sym-e33', (40, 21), ((40, 21.064), (40, 20.936), (40, 21)))
        self.add_bezier('sym-e34', (40, 21), ((40, 21.155), (40, 20.855), (40, 21)))
        self.add_line('sym-e35', (40, 21), (38, 30))
        self.add_bezier('sym-e36', (38, 30), ((37.545, 32.436), (37.291, 34.236), (35, 35)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.add_contour('sym-c3', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
