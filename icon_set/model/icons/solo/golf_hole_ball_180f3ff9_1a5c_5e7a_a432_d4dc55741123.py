"""Golf hole ball (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '180f3ff9-1a5c-5e7a-a432-d4dc55741123'
SOURCE_PATH = 'pictographic-primitives/sports/golf hole ball_180f3ff9-1a5c-5e7a-a432-d4dc55741123.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GolfHoleBall(Solo48):
    icon_id = 'golf-hole-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('golf', 'hole', 'ball', 'sports')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_arc('e0-top', (22, 13), (36, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (36, 13), (22, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_bezier('e1', (40, 39), ((35.737, 41.201), (30.488, 41.984), (25.685, 41.984)), ((25.227, 41.984), (24.761, 42), (24.295, 42)), ((23.746, 42), (23.223, 41.984), (22.699, 41.984)), ((18.281, 41.984), (13.568, 41.182), (9.6, 39.218)), ((7.997, 38.421), (6, 37.037), (6, 35.043)), ((6, 31.781), (10.835, 30.071), (13.29, 29.359)), ((19.885, 27.436), (29.097, 27.436), (35.618, 29.645)), ((37.942, 30.431), (41.984, 31.945), (41.984, 34.923)), ((41.992, 35.054), (41.992, 35.176), (42, 35.307)), ((41.992, 36.911), (41.006, 38.272), (40, 39)))
        self.add_contour('c0', 'e1', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
