"""Ampersand (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd56b7596-2f3c-5aab-89b8-85d1e917187c'
SOURCE_PATH = 'icons-json/interface-essential/ampersand_d56b7596-2f3c-5aab-89b8-85d1e917187c.json'
AUTHOR = 'json_to_solo'

class Ampersand(Solo48):
    icon_id = 'ampersand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('ampersand', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 25), (23, 19))
        self.add_line('e1', (18, 16), (35, 37))
        self.add_line('e2', (35, 37), (40, 42))
        self.add_bezier('e3', (40, 31), ((38.31, 32.791), (36.88, 35.091), (35, 36.727)), ((31.87, 39.445), (23.96, 43.982), (19.53, 43.982)), ((19.29, 43.982), (19.06, 44), (18.82, 44)), ((18.816, 44), (18.812, 44), (18.809, 44)), ((18.572, 44), (18.336, 43.991), (18.1, 43.991)), ((12.99, 43.991), (8.02, 40.318), (8.02, 35.455)), ((8.01, 35.382), (8.01, 35.3), (8, 35.227)), ((8, 35.226), (8, 35.225), (8, 35.224)), ((8, 35.152), (8.01, 35.072), (8.01, 35)), ((8.01, 31.591), (10.89, 26.882), (14, 25)))
        self.add_bezier('e4', (23, 19), ((25.45, 17.509), (28.47, 14.145), (28.92, 11.473)), ((29.51, 8), (26.95, 4.018), (22.71, 4.018)), ((22.64, 4.009), (22.56, 4.009), (22.49, 4)), ((22.487, 4), (22.485, 4), (22.483, 4)), ((22.325, 4), (22.177, 4.009), (22.02, 4.018)), ((20.45, 4.018), (18.98, 4.573), (17.83, 5.527)), ((14.29, 8.445), (15.46, 12.882), (18, 16)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1', 'e2')
