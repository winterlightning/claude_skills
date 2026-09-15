"""ladle: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd806eb05-a137-506d-b702-2b48eedabd62'
SOURCE_PATH = 'pictographic-primitives/food/ladle_d806eb05-a137-506d-b702-2b48eedabd62.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Ladle(Solo48):
    icon_id = 'ladle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ladle', 'food')

    def build(self):
        # Plan: VRECT_L; one clean hook and elliptical bowl, straight handle and exact rim attachment.
        # Reference: Geometric ellipse and circular hook.
        self.add_arc('hook',(30,9),(40,9),radius_x=5)
        self.add_line('handle',(26,33),(30,9))
        self.add_arc('bowl',(8,33),(26,33),radius_x=9,radius_y=11,sweep=False)
        self.add_line('rim',(26,33),(8,33))
        self.add_contour('cup','bowl','rim',closed=True)
        self.add_contour('handle-run','handle','hook')
        self.relate('connect','cup','handle-run')
