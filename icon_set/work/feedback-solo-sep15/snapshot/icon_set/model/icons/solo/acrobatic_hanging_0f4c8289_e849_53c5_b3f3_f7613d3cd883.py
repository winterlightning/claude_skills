"""acrobatic-hanging: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f4c8289-e849-53c5-b3f3-f7613d3cd883'
SOURCE_PATH = 'pictographic-primitives/sports/acrobatic hanging_0f4c8289-e849-53c5-b3f3-f7613d3cd883.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AcrobaticHanging(Solo48):
    icon_id = 'acrobatic-hanging'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('acrobatic', 'hanging', 'sports')

    def build(self):
        # Plan: VRECT_L; split the oval at its exact rope attachment, eliminating the interior tip.
        # Reference: Geometric ellipse; no useful Lucide subject match.
        self.add_line('rope',(24,4),(24,14))
        self.add_arc('ring-upper-left',(8,29),(24,14),radius_x=16,radius_y=15)
        self.add_arc('ring-upper-right',(24,14),(40,29),radius_x=16,radius_y=15)
        self.add_arc('ring-lower',(40,29),(8,29),radius_x=16,radius_y=15)
        self.add_contour('ring','ring-upper-left','ring-upper-right','ring-lower',closed=True)
        self.relate('connect','rope','ring')
