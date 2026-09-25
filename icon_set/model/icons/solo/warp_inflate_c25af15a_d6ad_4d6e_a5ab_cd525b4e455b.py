"""warp-inflate: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c25af15a-d6ad-4d6e-a5ab-cd525b4e455b'
SOURCE_PATH = 'pictographic-primitives/design/warp inflate_c25af15a-d6ad-4d6e-a5ab-cd525b4e455b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class WarpInflate(Solo48):
    icon_id = 'warp-inflate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('warp', 'inflate', 'design')

    def build(self):
        # HRECT_L (4,8)-(44,40); one exact ellipse with shared radii.
        # Construction reference: Lucide circle-check: coherent rounded outline
        self.add_arc('upper', (4,24), (44,24), radius_x=20, radius_y=16)
        self.add_arc('lower', (44,24), (4,24), radius_x=20, radius_y=16)
        self.add_contour('outline','upper','lower',closed=True)
