"""eye-1-state: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe0ffe1-6a10-4f5e-96f8-3d6033f13623'
SOURCE_PATH = 'pictographic-primitives/state/eye 1_4fe0ffe1-6a10-4f5e-96f8-3d6033f13623.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Eye1State(Solo48):
    icon_id = 'eye-1-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('eye', 'state')

    def build(self):
        # Plan: HRECT_L; four mirrored curves and balanced lens negative space.
        # Reference: Geometric lens; no pupil added to outline-only source.
        self.add_bezier('upper',(4,24),((9,15),(15,8),(24,8)),((33,8),(39,15),(44,24)))
        self.add_bezier('lower',(44,24),((39,33),(33,40),(24,40)),((15,40),(9,33),(4,24)))
        self.add_contour('outline','upper','lower',closed=True)

        self.add_dot('pupil',(24,24))
