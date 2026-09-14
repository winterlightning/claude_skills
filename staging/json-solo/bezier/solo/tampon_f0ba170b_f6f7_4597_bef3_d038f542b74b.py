"""Tampon (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0ba170b-f6f7-4597-bef3-d038f542b74b'
SOURCE_PATH = 'icons-json/health/tampon_f0ba170b-f6f7-4597-bef3-d038f542b74b.json'
AUTHOR = 'json_to_solo'

class TamponHealth(Solo48):
    icon_id = 'tampon-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tampon', 'health')

    def build(self):
        self.add_line('e0', (12, 38), (13, 33))
        self.add_line('e1', (15, 30), (18, 27))
        self.add_line('e2', (16, 19), (29, 6))
        self.add_line('e3', (38, 16), (26, 29))
        self.add_line('e4', (20, 28), (18, 26))
        self.add_bezier('e5', (8, 44), ((10.021, 42.345), (11.486, 40.782), (12, 38)))
        self.add_bezier('e6', (13, 33), ((13.185, 32), (14.36, 30.691), (15, 30)))
        self.add_bezier('e7', (18, 27), ((18, 26.7), (18, 26.3), (18, 26)))
        self.add_bezier('e8', (18, 26), ((16.712, 24.6), (14.577, 22.782), (15.116, 20.5)), ((15.2, 20.155), (15.756, 19.245), (16, 19)))
        self.add_bezier('e9', (29, 6), ((29.876, 5.118), (32.076, 4.018), (33.288, 4.018)), ((33.415, 4.009), (33.541, 4.009), (33.667, 4)), ((33.668, 4), (33.669, 4), (33.67, 4)), ((33.728, 4), (33.795, 4.009), (33.853, 4.009)), ((36.825, 4.009), (39.992, 7.227), (39.992, 10.482)), ((39.992, 10.616), (40, 10.75), (40, 10.885)), ((40, 10.887), (40, 10.889), (40, 10.891)), ((40, 11.018), (39.992, 11.155), (39.992, 11.291)), ((39.992, 12.636), (38.884, 15.045), (38, 16)))
        self.add_bezier('e10', (26, 29), ((25.705, 29.318), (24.851, 29.936), (24.463, 30.027)), ((22.484, 30.473), (21.339, 29.327), (20, 28)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7')
        self.add_contour('c1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
