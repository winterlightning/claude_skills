# Variant of mountain-pose-raised-arms; parent file remains unchanged.
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
        self.add_arc('head-top', (21, 10), (27, 10), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 10), (21, 10), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (8, 6), (8, 19), (24, 24), (40, 19), (40, 6), closed=False)
        self.add_line('body', (24, 24), (24, 42))
        self.relate('connect', 'arms', 'body')
