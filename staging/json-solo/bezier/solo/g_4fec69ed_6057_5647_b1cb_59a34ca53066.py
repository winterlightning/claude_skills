"""G (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fec69ed-6057-5647-b1cb-59a34ca53066'
SOURCE_PATH = 'icons-json/typeface/G_4fec69ed-6057-5647-b1cb-59a34ca53066.json'
AUTHOR = 'json_to_solo'

class G4fec69ed(Solo48):
    icon_id = 'g-4fec69ed'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('g', 'typeface')

    def build(self):
        self.add_line('e0', (40, 30), (40, 25))
        self.add_line('e1', (40, 25), (27, 25))
        self.add_bezier('e2', (38, 10), ((35.77, 5.8), (32.17, 4.018), (26.94, 4.018)), ((26.723, 4.018), (26.497, 4), (26.28, 4)), ((26.277, 4), (26.273, 4), (26.27, 4)), ((25.97, 4), (25.66, 4.018), (25.36, 4.018)), ((23.62, 4.018), (21.87, 4.255), (20.19, 4.664)), ((10.21, 7.127), (8.01, 14.764), (8.01, 23.191)), ((8.01, 23.585), (8, 23.978), (8, 24.372)), ((8, 24.378), (8, 24.385), (8, 24.391)), ((8, 25.009), (8.02, 25.618), (8.02, 26.227)), ((8.02, 33.518), (10.51, 40.336), (18.67, 42.964)), ((20.4, 43.527), (22.34, 43.982), (24.2, 43.982)), ((24.43, 43.982), (24.67, 44), (24.91, 44)), ((24.915, 44), (24.92, 44), (24.925, 44)), ((25.24, 44), (25.545, 43.982), (25.86, 43.982)), ((27.27, 43.982), (28.74, 43.691), (30.1, 43.355)), ((36.62, 41.709), (39.98, 36.982), (39.98, 31)), ((39.99, 30.891), (39.99, 30.791), (40, 30.691)), ((40, 30.582), (40, 30.109), (40, 30)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
