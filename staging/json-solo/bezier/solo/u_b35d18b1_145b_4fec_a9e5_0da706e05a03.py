"""U (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b35d18b1-145b-4fec-a9e5-0da706e05a03'
SOURCE_PATH = 'icons-json/typeface/u_b35d18b1-145b-4fec-a9e5-0da706e05a03.json'
AUTHOR = 'json_to_solo'

class UB35d18b1(Solo48):
    icon_id = 'u-b35d18b1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('u', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (40, 44))
        self.add_bezier('e1', (8, 4), ((8, 4), (8, 4), (8, 4)), ((8, 4), (8, 4.2), (8, 4.209)), ((8.01, 4.455), (8.02, 4.7), (8.02, 4.945)), ((8.02, 11.3), (8.27, 17.664), (8.37, 24.018)), ((8.4, 26.136), (8.44, 28.245), (8.46, 30.364)), ((8.52, 35.173), (8.79, 39.209), (13.97, 41.9)), ((15.2, 42.536), (16.55, 42.991), (17.92, 43.3)), ((19.81, 43.736), (21.8, 43.982), (23.75, 43.982)), ((24.13, 43.982), (24.52, 44), (24.9, 44)), ((25.17, 44), (25.43, 43.991), (25.7, 43.991)), ((31.45, 43.991), (37.03, 41.236), (39.16, 36.255)), ((39.55, 35.355), (39.98, 34.245), (39.98, 33.264)), ((39.98, 33.209), (40, 33.155), (40, 33.091)), ((40, 33.091), (40, 33), (40, 33)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0')
        self.relate('connect', 'c0', 'c1')
