"""oval: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a24b950-1725-4da0-b49d-dcbe11225bd1'
SOURCE_PATH = 'pictographic-primitives/design/oval_1a24b950-1725-4da0-b49d-dcbe11225bd1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Oval(Solo48):
    icon_id = 'oval'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('oval', 'design')

    def build(self):
        # HRECT_L (4,8)-(44,40); one exact ellipse with shared radii.
        # Construction reference: Lucide circle-check: coherent rounded outline
        self.add_arc('upper', (4,24), (44,24), radius_x=20, radius_y=16)
        self.add_arc('lower', (44,24), (4,24), radius_x=20, radius_y=16)
        self.add_contour('outline','upper','lower',closed=True)
