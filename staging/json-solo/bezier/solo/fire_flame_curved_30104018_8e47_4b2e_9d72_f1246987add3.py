"""Fire flame curved (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30104018-8e47-4b2e-9d72-f1246987add3'
SOURCE_PATH = 'icons-json/symbol/fire flame curved_30104018-8e47-4b2e-9d72-f1246987add3.json'
AUTHOR = 'json_to_solo'

class FireFlameCurvedSymbol(Solo48):
    icon_id = 'fire-flame-curved-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fire', 'flame', 'curved', 'symbol')

    def build(self):
        self.add_line('e0', (18, 21), (17, 20))
        self.add_line('e1', (16, 19), (14, 17))
        self.add_bezier('e2', (17, 20), ((16.67, 19.7), (16.33, 19.3), (16, 19)))
        self.add_bezier('e3', (14, 17), ((10.87, 20.618), (8.01, 23.891), (8.01, 28.745)), ((8.01, 28.844), (8, 28.951), (8, 29.05)), ((8, 29.051), (8, 29.053), (8, 29.055)), ((8, 29.373), (8.02, 29.682), (8.02, 30)), ((8.02, 37.364), (15.48, 44), (23.52, 44)), ((23.524, 44), (23.528, 44), (23.532, 44)), ((23.778, 44), (24.014, 44), (24.26, 44)), ((33.34, 44), (39.99, 36.236), (39.99, 28.345)), ((39.99, 28.256), (40, 28.166), (40, 28.077)), ((40, 28.076), (40, 28.074), (40, 28.073)), ((40, 27.773), (39.99, 27.464), (39.99, 27.164)), ((39.99, 25.736), (39.68, 24.264), (39.33, 22.882)), ((37.91, 17.209), (34.91, 11.873), (30.26, 7.827)), ((29.374, 7.058), (25.436, 4), (25.036, 4)), ((25.03, 4), (25.025, 4), (25.02, 4)), ((25.14, 5.118), (25.27, 6.236), (25.39, 7.355)), ((25.52, 8.545), (25.46, 9.727), (25.28, 10.918)), ((24.58, 15.427), (21.96, 18.364), (18, 21)))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3', closed=True)
