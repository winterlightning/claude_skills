"""Batch-05/earring (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdcf8f0c-b460-5564-8495-792c693562c8'
SOURCE_PATH = 'icons-json/accessories/batch-05/earring_bdcf8f0c-b460-5564-8495-792c693562c8.json'
AUTHOR = 'json_to_solo'

class Batch05Earring(Solo48):
    icon_id = 'batch-05-earring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'earring', 'accessories')

    def build(self):
        self.add_line('e0', (24, 15), (24, 19))
        self.add_bezier('e1', (13, 10), ((13.048, 9.136), (12.8, 8.527), (13.28, 7.691)), ((14.384, 5.755), (18.592, 4.009), (22.224, 4.009)), ((22.46, 4.009), (22.697, 4), (22.948, 4)), ((22.952, 4), (22.956, 4), (22.96, 4)), ((23.328, 4), (23.696, 4.009), (24.064, 4.009)), ((30.48, 4.009), (36.384, 7.745), (33.424, 11.364)), ((31.584, 13.636), (28.032, 14.518), (24, 15)))
        self.add_bezier('e2', (24, 19), ((29.424, 22.427), (39.984, 30.464), (39.984, 35.282)), ((39.984, 35.416), (40, 35.559), (40, 35.702)), ((40, 35.705), (40, 35.707), (40, 35.709)), ((40, 35.909), (39.968, 36.118), (39.968, 36.318)), ((39.968, 40), (32.224, 43.982), (25.872, 43.982)), ((25.504, 43.982), (25.152, 44), (24.8, 44)), ((24.794, 44), (24.788, 44), (24.782, 44)), ((24.405, 44), (24.042, 43.991), (23.68, 43.991)), ((16.128, 43.991), (8.032, 40.664), (8.032, 36.073)), ((8.032, 35.836), (8, 35.6), (8, 35.364)), ((8, 35.362), (8, 35.361), (8, 35.36)), ((8, 35.279), (8, 35.19), (8, 35.109)), ((8, 33.309), (9.536, 31.409), (10.928, 29.827)), ((14.272, 26.055), (18.912, 22.064), (24, 19)))
        self.add_contour('c0', 'e1', 'e0')
        self.add_contour('c1', 'e2', closed=True)
        self.relate('connect', 'c0', 'c1')
