"""Alcove (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c5e171c-ba31-4513-a36c-dbb30aad9abc'
SOURCE_PATH = 'icons-json/_uncategorized_01/alcove_5c5e171c-ba31-4513-a36c-dbb30aad9abc.json'
AUTHOR = 'json_to_solo'

class AlcoveUncategorized01(Solo48):
    icon_id = 'alcove-uncategorized-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('alcove', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (16, 35), (32, 35))
        self.add_line('e1', (16, 35), (16, 20))
        self.add_line('e2', (32, 20), (32, 35))
        self.add_line('e3', (38, 41), (40, 44))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_line('e5', (8, 44), (8, 39))
        self.add_line('e6', (8, 39), (8, 19))
        self.add_line('e7', (40, 19), (40, 44))
        self.add_bezier('e8', (16, 35), ((12.446, 36.936), (9.937, 40.4), (8, 44)))
        self.add_bezier('e9', (16, 20), ((16, 19.482), (15.949, 18.764), (16.135, 18.264)), ((17.726, 13.891), (22.341, 12.009), (26.383, 13.127)), ((29.819, 14.082), (31.133, 16.536), (32, 20)))
        self.add_bezier('e10', (32, 35), ((34.577, 36.427), (36.425, 38.445), (38, 41)))
        self.add_bezier('e11', (8, 19), ((8, 17.582), (8.531, 15.473), (9.036, 14.182)), ((11.427, 8.064), (17.339, 4.009), (23.469, 4.009)), ((23.577, 4.009), (23.677, 4), (23.784, 4)), ((23.786, 4), (23.788, 4), (23.789, 4)), ((24.067, 4), (24.354, 4.009), (24.632, 4.009)), ((30.897, 4.009), (37.255, 8.564), (39.276, 15.036)), ((39.604, 16.118), (40, 17.864), (40, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e1', 'e9', 'e2')
        self.add_contour('c3', 'e10', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e11', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
