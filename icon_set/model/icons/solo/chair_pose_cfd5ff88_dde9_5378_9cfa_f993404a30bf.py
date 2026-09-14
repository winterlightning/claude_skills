'A narrow side-view figure bends both knees while raising the arms straight overhead. The torso stays lifted above the shallow seated bend, with the head beside the upper arms.\nConstruction: Bounds (8,6)-(40,42). Raised arm and two deliberate knee bends; remove doubled legs and small foot loop. Side view kept asymmetric.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfd5ff88-dde9-5378-9cfa-f993404a30bf'
SOURCE_PATH = 'pictographic-primitives/sports/yoga chair awkward pose_cfd5ff88-dde9-5378-9cfa-f993404a30bf.svg'
AUTHOR = 'gpt-6'

class ChairPose(Solo48):
    icon_id = 'chair-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('chair', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (8, 10), (14, 10), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (14, 10), (8, 10), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arm', (28, 6), (28, 20), (28, 27), closed=False)
        self.add_polyline('body', (28, 20), (17, 27), (32, 35), (26, 42), closed=False)
        self.relate("connect", 'arm', 'body')
        self.add_line('feet', (26, 42), (40, 42))
        self.relate("connect", 'body', 'feet')
