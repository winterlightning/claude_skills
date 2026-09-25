"""u-turn-left: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a392fc8f-838e-40fb-a666-e78597be5c78'
SOURCE_PATH = 'pictographic-primitives/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UTurnLeft(Solo48):
    icon_id = 'u-turn-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('u', 'turn', 'left', 'transportation')

    def build(self):
        # Plan: SQUARE; one circular turn with vertical tangents and equal arrowhead arms.
        # Reference: Lucide undo-2: continuous bend and clean head.
        self.add_line('right',(42,42),(42,20))
        self.add_arc('turn',(42,20),(14,20),radius_x=14,sweep=False)
        self.add_line('left',(14,20),(14,34))
        self.add_contour('run','right','turn','left')
        self.add_polyline('head',(6,26),(14,34),(22,26))
        self.relate('connect','run','head')
