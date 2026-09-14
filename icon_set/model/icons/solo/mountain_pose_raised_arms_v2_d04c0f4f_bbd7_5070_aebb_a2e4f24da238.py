"""A narrow standing figure extends the arms straight upward beside the head. The long torso and joined legs form one continuous upright silhouette with a softly rounded bottom.
Construction: Bounds (8,6)-(40,42). Standing with joined legs and two raised arms; use front-facing paired arms to keep openings clear. Remove doubled leg outlines.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd04c0f4f-bbd7-5070-aebb-a2e4f24da238'
SOURCE_PATH = 'pictographic-primitives/sports/yoga mountain arms up pose_d04c0f4f-bbd7-5070-aebb-a2e4f24da238.svg'
AUTHOR = 'gpt-6'

class MountainPoseRaisedArmsVariant2(Solo48):
    icon_id = 'mountain-pose-raised-arms-v2'
    variant_of = 'mountain-pose-raised-arms'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('mountain', 'pose', 'raised', 'arms', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 13), (27, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 13), (21, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        # Separate the rounded side arms from the flat shoulder span so the exact gap is certifiable.
        self.add_line('arm-l', (8, 4), (8, 16))
        self.add_arc('shoulder-l', (8, 16), (16, 24), radius_x=8, sweep=False)
        self.add_contour('left-arm', 'arm-l', 'shoulder-l')
        self.add_line('arms', (16, 24), (24, 24))
        self.add_line('arms-right', (24, 24), (32, 24))
        self.add_arc('shoulder-r', (32, 24), (40, 16), radius_x=8, sweep=False)
        self.add_line('arm-r', (40, 16), (40, 4))
        self.add_contour('right-arm', 'shoulder-r', 'arm-r')
        self.relate('connect', 'left-arm', 'arms')
        self.relate('connect', 'arms', 'arms-right')
        self.relate('connect', 'arms-right', 'right-arm')
        self.add_line('body', (24, 24), (24, 44))
        self.relate('connect', 'arms', 'body')
