# Review candidate; original preserved.
"""A reclining figure raises the hips into a curved bridge with the head low on the right. A bent supporting leg drops underneath while another long limb extends diagonally toward the upper left.
Construction: Bounds (6,8)-(42,40). Raised diagonal leg, bent support and low head right preserve the one-legged bridge; remove doubled body contour.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed6cb660-23da-5c6d-9d87-7413118cab56'
SOURCE_PATH = 'pictographic-primitives/sports/yoga bridge pose_ed6cb660-23da-5c6d-9d87-7413118cab56.svg'
AUTHOR = 'gpt-6'

class BridgePoseVariant2(Solo48):
    icon_id = 'bridge-pose-v2'
    variant_of = 'bridge-pose'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('bridge', 'pose', 'yoga', 'exercise')

    def build(self):
        """Opening repair: Replaced the flattened head lens with a genuine circular head; retained the pose."""
        self.add_arc('head-top', (38, 30), (44, 30), sweep=True, radius_x=3, radius_y=3)
        self.add_arc('head-bottom', (44, 30), (38, 30), sweep=True, radius_x=3, radius_y=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('raised-leg', (4, 8), (18, 19), (29, 29), closed=False)
        self.add_polyline('support-leg', (18, 19), (12, 26), (12, 40), closed=False)
        self.relate('connect', 'raised-leg', 'support-leg')
        self.add_polyline('back', (29, 29), (31, 37), (24, 40), closed=False)
        self.relate('connect', 'raised-leg', 'back')
