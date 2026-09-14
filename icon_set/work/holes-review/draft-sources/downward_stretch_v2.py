# Variant of downward-stretch; parent file remains unchanged.
"""A figure forms a high inverted V with the hips lifted and limbs sloping down to either side. A short curved head outline sits above the low extended forearms on the left.
Construction: Bounds (6,8)-(42,40). Inverted V with low left forearms and lowered head; preserve original direction, remove doubled contour.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3dea441-ee35-4695-9882-6fd0119f58d3'
SOURCE_PATH = 'pictographic-primitives/sports/yoga down stretch_f3dea441-ee35-4695-9882-6fd0119f58d3.svg'
AUTHOR = 'gpt-6'

class DownwardStretchVariant2(Solo48):
    icon_id = 'downward-stretch-v2'
    variant_of = 'downward-stretch'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('downward', 'stretch', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (6, 26), (11, 26), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (11, 26), (6, 26), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (6, 40), (14, 40), (30, 8), (42, 40), closed=False)
