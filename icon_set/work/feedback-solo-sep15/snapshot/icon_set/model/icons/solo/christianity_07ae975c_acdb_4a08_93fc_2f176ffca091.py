"""Christianity (religion), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07ae975c-acdb-4a08-93fc-2f176ffca091'
SOURCE_PATH = 'pictographic-primitives/religion/christianity_07ae975c-acdb-4a08-93fc-2f176ffca091.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Christianity(Solo48):
    icon_id = 'christianity'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('christianity', 'religion')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (41, 19), (38, 24))
        self.add_bezier('e1', (44, 8), ((43.491, 10.92), (42.418, 16.92), (41, 19)))
        self.add_bezier('e2', (44, 40), ((43.991, 39.24), (43.7, 38.387), (43.555, 37.733)), ((42.391, 32.52), (40.427, 28.067), (38, 24)))
        self.add_bezier('e3', (38, 24), ((36.173, 21.253), (33.873, 18.52), (31.655, 16.44)), ((25.1, 10.28), (17.782, 10.12), (11.018, 15.88)), ((9.073, 17.547), (7.309, 19.627), (5.645, 21.84)), ((5.291, 22.307), (4, 23.96), (4, 24.16)), ((4, 24.378), (5.133, 25.781), (5.482, 26.267)), ((7.173, 28.573), (8.882, 30.76), (10.873, 32.493)), ((17.3, 38.107), (24.482, 38.147), (30.909, 32.493)), ((33.473, 30.24), (35.9, 27.08), (38, 24)))
        self.add_contour('c0', 'e1', 'e0', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=True)
        self.relate('connect', 'c1', 'c2')
