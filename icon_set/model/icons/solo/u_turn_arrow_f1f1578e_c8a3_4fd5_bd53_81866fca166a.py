"""u-turn-arrow: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1f1578e-c8a3-4fd5-bd53-81866fca166a'
SOURCE_PATH = 'pictographic-primitives/symbol/u turn arrow_f1f1578e-c8a3-4fd5-bd53-81866fca166a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UTurnArrow(Solo48):
    icon_id = 'u-turn-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('u', 'turn', 'arrow', 'symbol')

    def build(self):
        # Plan: VRECT_L; one semicircle joins parallel legs; equal arrowhead arms.
        # Reference: Lucide undo-2: tangent circle-to-line construction.
        self.add_line('left',(8,44),(8,16))
        self.add_arc('turn',(8,16),(32,16),radius_x=12)
        self.add_line('right',(32,16),(32,38))
        self.add_contour('run','left','turn','right')
        self.add_polyline('head',(24,30),(32,38),(40,30))
        self.relate('connect','run','head')
