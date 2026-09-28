"""oval-check: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = 'pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class OvalCheck(Solo48):
    icon_id = 'oval-check'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('oval', 'check', 'state')

    def build(self):
        # HRECT_L (4,8)-(44,40); exact ellipse and interior mark with generous clearance.
        # Construction reference: Lucide circle-check: simple smooth envelope and two-segment check
        self.add_arc('upper',(4,24),(44,24),radius_x=20,radius_y=16)
        self.add_arc('lower',(44,24),(4,24),radius_x=20,radius_y=16)
        self.add_contour('outline','upper','lower',closed=True)
        self.add_polyline('check',(16,23),(22,29),(31,19))
