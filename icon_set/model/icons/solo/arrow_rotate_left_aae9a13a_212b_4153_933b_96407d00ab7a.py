"""Arrow rotate left (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aae9a13a-212b-4153-933b-96407d00ab7a'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow rotate left_aae9a13a-212b-4153-933b-96407d00ab7a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ArrowRotateLeft(Solo48):
    icon_id = 'arrow-rotate-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('arrow', 'rotate', 'left', 'symbol')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (15, 6), (6, 15))
        self.add_line('e1', (15, 23), (6, 15))
        self.add_line('e2', (42, 42), (42, 15))
        self.add_line('e3', (42, 15), (6, 15))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e3', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
