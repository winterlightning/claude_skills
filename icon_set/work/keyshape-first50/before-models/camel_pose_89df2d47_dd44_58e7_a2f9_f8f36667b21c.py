'A kneeling figure arches the torso backward above folded lower legs. One long arm reaches down toward the heels, and the round head sits above the curved chest on the right.\nConstruction: Bounds (8,6)-(40,42). Broad back arch above kneeling shin, long arm reaching heel. Remove parallel torso boundary; keep asymmetry.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89df2d47-dd44-58e7-a2f9-f8f36667b21c'
SOURCE_PATH = 'pictographic-primitives/sports/yoga camel pose_89df2d47-dd44-58e7-a2f9-f8f36667b21c.svg'
AUTHOR = 'gpt-6'

class CamelPose(Solo48):
    icon_id = 'camel-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('camel', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (34, 7), (40, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (40, 7), (34, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('arched-back', (30, 19), (8, 41), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('knee', (8, 41), (11, 42), radius_x=3, radius_y=3, sweep=False)
        self.add_line('shin', (11, 42), (22, 42))
        self.add_contour('body', 'arched-back', 'knee', 'shin', closed=False)
        self.add_line('arm', (30, 19), (30, 42))
        self.relate("connect", 'body', 'arm')
