"""Smile (chat), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b89f261-bd85-4abc-8e75-64ff35cd7b4f'
SOURCE_PATH = 'icons-json/chat/smile_5b89f261-bd85-4abc-8e75-64ff35cd7b4f.json'
AUTHOR = 'json_to_solo'

class SmileChat(Solo48):
    icon_id = 'smile-chat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('smile', 'chat')

    def build(self):
        self.add_line('e0', (33, 21), (39, 16))
        self.add_line('e1', (44, 19), (44, 32))
        self.add_line('e2', (44, 32), (43, 34))
        self.add_line('e3', (43, 34), (33, 28))
        self.add_line('e4', (4, 33), (4, 13))
        self.add_line('e5', (9, 8), (29, 8))
        self.add_line('e6', (33, 14), (33, 34))
        self.add_line('e7', (28, 40), (9, 40))
        self.add_bezier('e8', (39, 16), ((40.036, 15.19), (41.618, 14.56), (42.8, 14.06)), ((42.9, 14.01), (43.855, 13.66), (43.864, 13.67)), ((43.873, 13.73), (43.873, 13.79), (43.882, 13.85)), ((43.955, 14.95), (43.982, 16.07), (43.982, 17.18)), ((43.982, 17.57), (44, 17.97), (44, 18.37)), ((44, 18.58), (44, 18.79), (44, 19)))
        self.add_bezier('e9', (9, 40), ((8.936, 40), (8.409, 40), (8.345, 40)), ((5.464, 40), (4.009, 36.65), (4.009, 33.93)), ((4.009, 33.62), (4, 33.31), (4, 33)))
        self.add_bezier('e10', (4, 13), ((4.009, 12.87), (4.009, 12.74), (4.018, 12.61)), ((4.018, 9.76), (6.2, 8.01), (8.591, 8.01)), ((8.682, 8.01), (8.773, 8), (8.864, 8)), ((9.064, 8), (8.8, 8), (9, 8)))
        self.add_bezier('e11', (29, 8), ((29.136, 8), (28.818, 8), (28.945, 8.01)), ((30.791, 8.01), (32.382, 9.45), (32.9, 11.36)), ((33.127, 12.17), (33, 13.17), (33, 14)))
        self.add_bezier('e12', (33, 34), ((33, 36.18), (32.264, 38.29), (30.5, 39.43)), ((30.109, 39.69), (29.573, 39.99), (29.1, 39.99)), ((29.036, 40), (28.964, 40), (28.891, 40)), ((28.827, 40), (28.755, 40), (28.682, 39.99)), ((28.545, 39.99), (28.409, 39.99), (28.264, 39.99)), ((28.191, 40), (28.127, 40), (28.055, 40)), ((27.918, 40), (28.136, 40), (28, 40)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
