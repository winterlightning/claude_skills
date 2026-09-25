"""Aspect ratio (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ba9bd95-6bcb-4cc5-b8ab-8562a1e8bdce'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/aspect ratio_0ba9bd95-6bcb-4cc5-b8ab-8562a1e8bdce.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AspectRatio(Solo48):
    icon_id = 'aspect-ratio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('aspect', 'ratio', '_uncategorized_04')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 25), (23, 25))
        self.add_line('e1', (23, 25), (23, 42))
        self.add_line('e2', (6, 25), (6, 42))
        self.add_line('e3', (6, 42), (23, 42))
        self.add_line('e4', (6, 25), (6, 16))
        self.add_line('e5', (23, 42), (32, 42))
        self.add_line('e6', (6, 16), (32, 16))
        self.add_line('e7', (32, 16), (32, 42))
        self.add_line('e8', (6, 16), (6, 6))
        self.add_line('e9', (6, 6), (42, 6))
        self.add_line('e10', (42, 6), (42, 42))
        self.add_line('e11', (42, 42), (32, 42))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.add_contour('c4', 'e6', 'e7', closed=False)
        self.add_contour('c5', 'e8', 'e9', 'e10', 'e11', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
