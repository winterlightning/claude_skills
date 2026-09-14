"""Thumb (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5652a88-5c11-499a-8e2e-486a9b3a75d1'
SOURCE_PATH = 'icons-json/symbol/thumb_c5652a88-5c11-499a-8e2e-486a9b3a75d1.json'
AUTHOR = 'json_to_solo'

class ThumbSymbol(Solo48):
    icon_id = 'thumb-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('thumb', 'symbol')

    def build(self):
        self.add_line('e0', (28, 19), (30, 12))
        self.add_line('e1', (8, 23), (8, 39))
        self.add_line('e2', (16, 41), (19, 43))
        self.add_line('e3', (23, 44), (32, 44))
        self.add_line('e4', (37, 39), (40, 25))
        self.add_bezier('e5', (30, 12), ((30.741, 8.791), (30.08, 4), (26.072, 4)), ((26.07, 4), (26.069, 4), (26.068, 4)), ((25.985, 4), (25.902, 4.009), (25.819, 4.009)), ((23.705, 4.009), (23.183, 6.491), (22.829, 8.227)), ((22.189, 11.355), (20.859, 14.4), (18.846, 16.773)), ((17.44, 18.436), (15.621, 19.782), (13.549, 20.209)), ((12.362, 20.455), (11.116, 20.173), (9.954, 20.518)), ((8.909, 20.827), (8, 21.791), (8, 23)))
        self.add_bezier('e6', (8, 39), ((8.008, 39.091), (8.017, 38.736), (8.025, 38.827)), ((8.067, 38.955), (8.101, 39.073), (8.135, 39.2)), ((9.558, 42.227), (13.709, 39.764), (16, 41)))
        self.add_bezier('e7', (19, 43), ((20.002, 43.545), (21.785, 44), (22.914, 44)), ((22.998, 44), (22.916, 44), (23, 44)))
        self.add_bezier('e8', (32, 44), ((34.173, 43.364), (36.394, 41.609), (37, 39)))
        self.add_bezier('e9', (40, 25), ((40, 24.582), (40, 24.064), (40, 23.645)), ((40, 22.209), (38.813, 20.627), (37.566, 20.209)), ((36.387, 19.809), (35.015, 19.873), (33.794, 19.809)), ((31.924, 19.727), (29.861, 19.182), (28, 19)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
