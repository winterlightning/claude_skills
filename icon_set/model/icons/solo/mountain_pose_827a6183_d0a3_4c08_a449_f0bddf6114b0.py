"""A front-facing figure stands upright with the feet together and arms resting down beside the torso. The body has rounded shoulders and a separate circular head centered above.
Construction: Bounds (8,6)-(40,42). Mirror rounded shoulders and resting arms; one vertical stroke denotes feet-together stance. Remove doubled body boundary.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '827a6183-d0a3-4c08-a449-f0bddf6114b0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga mountain pose_827a6183-d0a3-4c08-a449-f0bddf6114b0.svg'
AUTHOR = 'gpt-6'

class MountainPose(Solo48):
    icon_id = 'mountain-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('mountain', 'pose', 'yoga', 'exercise')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('head-top', (21, 7), (27, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 7), (21, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm-l', (8, 34), (8, 25))
        self.add_arc('shoulder-l', (8, 25), (24, 18), radius_x=16, radius_y=7, sweep=True)
        self.add_arc('shoulder-r', (24, 18), (40, 25), radius_x=16, radius_y=7, sweep=True)
        self.add_line('arm-r', (40, 25), (40, 34))
        self.add_contour('arms', 'arm-l', 'shoulder-l', 'shoulder-r', 'arm-r', closed=False)
        self.add_line('body', (24, 18), (24, 44))
        self.relate('connect', 'arms', 'body')
