'A figure balances on one vertical leg while the torso, arms, and raised rear leg form a long horizontal span. The lowered head peeks beneath the left side of the outstretched body.\nConstruction: Bounds (6,8)-(42,40). Horizontal torso and rear leg with one vertical supporting leg; lowered head left. Remove duplicated limb outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8425ffa-e3c5-5bfe-8ef8-8629d46590cf'
SOURCE_PATH = 'pictographic-primitives/sports/yoga balancing stick pose_b8425ffa-e3c5-5bfe-8ef8-8629d46590cf.svg'
AUTHOR = 'gpt-6'

class BalancingStickPose(Solo48):
    icon_id = 'balancing-stick-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('balancing', 'stick', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (9, 22), (15, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (15, 22), (9, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('balance', (6, 8), (28, 12), (42, 8), closed=False)
        self.add_line('support', (28, 12), (28, 40))
        self.relate("connect", 'balance', 'support')
