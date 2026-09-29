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
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('camel', 'pose', 'yoga', 'exercise')

    def build(self):
        # Human reference: human_ref/full_body_ref.png, kneeling pose.
        # Head center (34,10), radius 6; body top (34,24): ink gap exactly 4.
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_arc('head-top', (28, 10), (40, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('head-bottom', (40, 10), (28, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('arched-back', (34, 24), (8, 41), radius_x=26, radius_y=17, sweep=False)
        self.add_arc('knee', (8, 41), (11, 44), radius_x=3, radius_y=3, sweep=False)
        self.add_line('shin', (11, 44), (22, 44))
        self.add_contour('body', 'arched-back', 'knee', 'shin', closed=False)
        self.add_line('arm', (34, 24), (34, 44))
        self.relate("connect", 'body', 'arm')
