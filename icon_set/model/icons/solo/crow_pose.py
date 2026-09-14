# Review candidate; original preserved.
"""A compact figure balances forward with a long arm extending down beneath the shoulder. The round head projects left while bent knees tuck toward the body at the upper right.
Construction: Bounds (6,8)-(42,40). Compact tucked knee above a supporting arm, head projecting left. Remove parallel limb outlines.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a2b64ee-6a30-5094-9ab6-83d78d52dace'
SOURCE_PATH = 'pictographic-primitives/sports/yoga crow pose_9a2b64ee-6a30-5094-9ab6-83d78d52dace.svg'
AUTHOR = 'gpt-6'

class CrowPose(Solo48):
    icon_id = 'crow-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('crow', 'pose', 'yoga', 'exercise')

    def build(self):
        """Opening repair: Replaced the flattened head lens with a genuine circular head; retained the pose."""
        self.add_arc('head-top', (5, 23), (11, 23), sweep=True, radius_x=3, radius_y=3)
        self.add_arc('head-bottom', (11, 23), (5, 23), sweep=True, radius_x=3, radius_y=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('support', (20, 40), (20, 22))
        self.add_arc('back', (20, 22), (34, 8), radius_x=14)
        self.add_contour('body', 'support', 'back')
        self.add_arc('knee', (34, 8), (42, 16), radius_x=8)
        self.add_line('knee-drop', (42, 16), (42, 20))
        self.relate('connect', 'knee', 'knee-drop')
        self.add_polyline('shin', (42, 20), (35, 26), (42, 32), closed=False)
        self.relate('connect', 'body', 'knee')
        self.relate('connect', 'knee-drop', 'shin')
