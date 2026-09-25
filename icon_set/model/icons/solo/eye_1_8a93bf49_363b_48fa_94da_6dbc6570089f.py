"""eye-1-container: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a93bf49-363b-48fa-94da-6dbc6570089f'
SOURCE_PATH = 'pictographic-primitives/container/eye 1_8a93bf49-363b-48fa-94da-6dbc6570089f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Eye1Container(Solo48):
    icon_id = 'eye-1-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('eye', 'container')

    def build(self):
        # Plan: HRECT_L; four mirrored curves and balanced lens negative space.
        # Reference: Geometric lens; no pupil added to outline-only source.
        self.add_bezier('upper',(4,24),((9,15),(15,8),(24,8)),((33,8),(39,15),(44,24)))
        self.add_bezier('lower',(44,24),((39,33),(33,40),(24,40)),((15,40),(9,33),(4,24)))
        self.add_contour('outline','upper','lower',closed=True)
