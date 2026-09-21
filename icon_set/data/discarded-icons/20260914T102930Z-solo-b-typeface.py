"""B (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f75edd9-c897-46e0-892c-e11aada52bf0'
SOURCE_PATH = 'icons-json/typeface/b_8f75edd9-c897-46e0-892c-e11aada52bf0.json'
AUTHOR = 'json_to_solo'

class BTypeface(Solo48):
    icon_id = 'b-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('b', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 33))
        self.add_bezier('e1', (32, 19), ((29.28, 18.145), (26.48, 17.345), (23.48, 17.491)), ((16.147, 17.836), (11.52, 20.973), (9.253, 25.564)), ((8.64, 26.8), (8.013, 28.245), (8.013, 29.573)), ((8.013, 29.655), (8, 29.727), (8, 29.809)), ((8.04, 30.9), (8, 32), (8, 33.091)), ((8.013, 33.191), (8.013, 33.3), (8.027, 33.4)), ((8.027, 39.327), (13.56, 43.991), (22.587, 43.991)), ((22.875, 43.991), (23.164, 44), (23.453, 44)), ((23.458, 44), (23.462, 44), (23.467, 44)), ((23.773, 44), (24.08, 43.991), (24.387, 43.991)), ((33.987, 43.991), (39.973, 37.982), (39.973, 31.891)), ((39.973, 31.587), (40, 31.274), (40, 30.96)), ((40, 30.955), (40, 30.95), (40, 30.945)), ((40, 30.627), (39.973, 30.309), (39.973, 29.982)), ((39.973, 25.636), (37.6, 21.345), (32, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
