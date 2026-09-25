"""Messages bubble with dots (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1a51949-b13a-41fa-81ae-78731ae3349e'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MessagesBubbleWithDots(Solo48):
    icon_id = 'messages-bubble-with-dots'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('messages', 'bubble', 'with', 'dots', 'symbol')

    def build(self):
        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.
        # Reference: original stroke graph and contour extremes.
        self.add_bezier('e0', (5, 40), ((6.627, 38.62), (7.991, 37.3), (9.036, 35.34)), ((9.264, 34.91), (9.491, 34.49), (9.709, 34.06)), ((9.764, 33.96), (9.818, 33.87), (9.864, 33.77)), ((9.727, 33.51), (7.855, 31.98), (7.464, 31.53)), ((5.636, 29.45), (4.009, 26.36), (4.009, 23.38)), ((4.009, 23.272), (4, 23.148999999999997), (4, 23.04)), ((4, 22.82), (4.009, 22.59), (4.009, 22.37)), ((4.009, 20.81), (4.564, 19.18), (5.218, 17.82)), ((8.327, 11.36), (16.282, 8.02), (22.655, 8.02)), ((22.923, 8.02), (23.195999999999998, 8), (23.464, 8)), ((24.055, 8), (24.645, 8.02), (25.236, 8.02)), ((31.673, 8.02), (39.755, 11.36), (42.827, 17.94)), ((43.482, 19.33), (44.0, 21.12), (44, 22.71)), ((44, 22.94), (43.991, 23.16), (43.991, 23.39)), ((43.991, 25.27), (43.336, 27.24), (42.464, 28.83)), ((38.609, 35.82), (30.218, 38.47), (23.191, 38.26)), ((21.364, 38.2), (19.464, 37.95), (17.691, 37.45)), ((17.3, 37.34), (15.327, 36.6), (15.1, 36.64)), ((14.8, 36.7), (13.318, 37.93), (12.882, 38.19)), ((11.127, 39.22), (9.009, 39.98), (7.009, 39.98)), ((6.782, 39.98), (6.555, 40), (6.318, 40)), ((5.855, 40), (5.473, 40), (5, 40)))
        self.add_line('e1', (13, 23), (13, 23))
        self.add_line('e2', (24, 23), (24, 23))
        self.add_line('e3', (35, 23), (35, 23))
        self.add_contour('c0', 'e0', closed=True)
