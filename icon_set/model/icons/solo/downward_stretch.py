# Review candidate; original preserved.
"""A figure forms a high inverted V with the hips lifted and limbs sloping down to either side. A short curved head outline sits above the low extended forearms on the left.
Construction: Bounds (6,8)-(42,40). Inverted V with low left forearms and lowered head; preserve original direction, remove doubled contour.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3dea441-ee35-4695-9882-6fd0119f58d3'
SOURCE_PATH = 'pictographic-primitives/sports/yoga down stretch_f3dea441-ee35-4695-9882-6fd0119f58d3.svg'
AUTHOR = 'gpt-6'

class DownwardStretch(Solo48):
    icon_id = 'downward-stretch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('downward', 'stretch', 'yoga', 'exercise')

    def build(self):
        """Opening repair: Replaced the flattened head lens with a genuine circular head; retained the pose."""
        self.add_arc('head-top', (5, 26), (11, 26), sweep=True, radius_x=3, radius_y=3)
        self.add_arc('head-bottom', (11, 26), (5, 26), sweep=True, radius_x=3, radius_y=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (4, 40), (14, 40), (30, 8), (44, 40), closed=False)
