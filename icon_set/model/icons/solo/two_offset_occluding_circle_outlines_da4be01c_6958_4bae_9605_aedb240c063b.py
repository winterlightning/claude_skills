"""Two Overlapping Circles.

Symbol plan: Two equal circles offset diagonally; foreground outline masks the back arc through explicit shared intersection points. No useful Lucide circle-pair match.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da4be01c-6958-4bae-9605-aedb240c063b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/twin_da4be01c-6958-4bae-9605-aedb240c063b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-offset-occluding-circle-outlines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('two', 'overlapping', 'circles')

    def build(self):
        # Equal circles at (18,18) and (30,30), radius 12.
        self.add_arc('back',(18,30),(30,18),radius_x=12,large_arc=True)
        self.add_arc('front-long',(30,18),(18,30),radius_x=12,large_arc=True)
        self.add_arc('front-short',(18,30),(30,18),radius_x=12)
        self.add_contour('front','front-long','front-short',closed=True)
        self.relate('connect','back','front')
