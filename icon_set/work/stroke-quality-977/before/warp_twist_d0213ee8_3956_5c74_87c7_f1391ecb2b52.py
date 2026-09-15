"""Warp twist (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0213ee8-3956-5c74-87c7-f1391ecb2b52'
SOURCE_PATH = 'pictographic-primitives/design/warp twist_d0213ee8-3956-5c74-87c7-f1391ecb2b52.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WarpTwist(Solo48):
    icon_id = 'warp-twist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'twist', 'design')

    def build(self):
        self.add_line('e0', (26, 22), (22, 25))
        self.add_line('e1', (42, 6), (6, 6))
        self.add_line('e2', (6, 6), (6, 42))
        self.add_line('e3', (6, 42), (42, 42))
        self.add_line('e4', (42, 42), (42, 6))
        self.add_arc('e5', (28, 6), (26, 22), radius_x=14)
        self.add_arc('e6', (22, 25), (20, 42), radius_x=15, sweep=False)
        self.add_contour('c0', 'e5', 'e0', 'e6')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
