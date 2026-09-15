"""A narrow side-view figure bends both knees while raising the arms straight overhead. The torso stays lifted above the shallow seated bend, with the head beside the upper arms.
Construction: Bounds (8,6)-(40,42). Raised arm and two deliberate knee bends; remove doubled legs and small foot loop. Side view kept asymmetric.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cfd5ff88-dde9-5378-9cfa-f993404a30bf'
SOURCE_PATH = 'pictographic-primitives/sports/yoga chair awkward pose_cfd5ff88-dde9-5378-9cfa-f993404a30bf.svg'
AUTHOR = 'gpt-6'

class ChairPose(Solo48):
    icon_id = 'chair-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('chair', 'pose', 'yoga', 'exercise')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        # Human reference: circular head, raised arm, bent hips/knees; exact side gap 8.
        self.add_arc('head-top', (8, 14), (14, 14), radius_x=3)
        self.add_arc('head-bottom', (14, 14), (8, 14), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm', (22, 4), (22, 22))
        self.add_polyline('body', (22, 22), (30, 30), (17, 30), (24, 44))
        self.add_line('feet', (24, 44), (40, 44))
        self.relate('connect', 'arm', 'body')
        self.relate('connect', 'body', 'feet')
