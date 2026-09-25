"""u-turn-right: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd89078-9ea5-43e7-8b53-fc1e7797e607'
SOURCE_PATH = 'pictographic-primitives/transportation/u turn right_3cd89078-9ea5-43e7-8b53-fc1e7797e607.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class UTurnRight(Solo48):
    icon_id = 'u-turn-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('u', 'turn', 'right', 'transportation')

    def build(self):
        # SQUARE (6,6)-(42,42); one semicircle owns both vertical tangents.
        # Construction reference: Lucide undo-2: circle-to-line tangency
        self.add_line('left',(6,42),(6,20))
        self.add_arc('turn',(6,20),(34,20),radius_x=14)
        self.add_line('right',(34,20),(34,34))
        self.add_contour('run','left','turn','right')
        self.add_polyline('head',(26,26),(34,34),(42,26))
        self.relate('connect','run','head')
