# Review candidate; original preserved.
"""A reclining figure raises the hips into a curved bridge with the head low on the right. A bent supporting leg drops underneath while another long limb extends diagonally toward the upper left.
Construction: Bounds (6,8)-(42,40). Raised diagonal leg, bent support and low head right preserve the one-legged bridge; remove doubled body contour.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ed6cb660-23da-5c6d-9d87-7413118cab56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bridge-pose/20260927T032022Z-thuan-mac-1/reference/yoga bridge pose_ed6cb660-23da-5c6d-9d87-7413118cab56.svg'
AUTHOR = "gpt-6"

class BridgePose(Solo48):
    icon_id = 'bridge-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('bridge', 'pose', 'yoga', 'exercise')

    def build(self):
        # A larger detached head and two differently bent supports recover the pose.
        self.add_arc('head-upper', (36, 28), (44, 28), radius_x=4)
        self.add_arc('head-lower', (44, 28), (36, 28), radius_x=4)
        self.add_contour('head', 'head-upper', 'head-lower', closed=True)
        self.add_line('raised-leg', (4, 8), (18, 19))
        self.add_line('torso', (18, 19), (28, 28))
        self.add_polyline('rear-support', (18, 19), (12, 26), (12, 40))
        self.add_polyline('front-support', (28, 28), (27, 36), (24, 40))
        self.relate('connect', 'raised-leg', 'torso')
        self.relate('connect', 'raised-leg', 'rear-support')
        self.relate('connect', 'torso', 'rear-support')
        self.relate('connect', 'torso', 'front-support')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='end')
