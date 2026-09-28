"""dew: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09205fdc-98c2-4833-b1f6-9a17e483ac53'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/dew_09205fdc-98c2-4833-b1f6-9a17e483ac53.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Dew(Solo48):
    icon_id = 'dew'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dew', '_uncategorized')

    def build(self):
        # Plan: VRECT_L; mirrored shoulders meet a circular bowl with vertical tangents.
        # Reference: Lucide droplet: a coherent pointed crest and round bowl.
        axis = 24
        self.add_bezier('left',(axis,4),((19,11),(8,22),(8,28)))
        self.add_arc('bowl',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_bezier('right',(40,28),((40,22),(29,11),(axis,4)))
        self.add_contour('outline','left','bowl','right',closed=True)
