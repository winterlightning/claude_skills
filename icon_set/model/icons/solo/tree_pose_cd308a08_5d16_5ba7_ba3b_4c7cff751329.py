"""A figure balances on one straight leg while the opposite foot rests against its inner side, forming a triangular knee opening. Both arms curve overhead around the circular head.
Construction: Bounds (8,6)-(40,42). Mirror overhead arms, but retain the single folded knee and straight supporting leg. Triangle of bent knee remains open.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd308a08-5d16-5ba7-ba3b-4c7cff751329'
SOURCE_PATH = 'pictographic-primitives/sports/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg'
AUTHOR = 'gpt-6'

class TreePose(Solo48):
    icon_id = 'tree-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tree', 'pose', 'yoga', 'exercise')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
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
        self.add_polyline('body', (24, 24), (24, 29), (24, 44), closed=False)
        self.relate('connect', 'arms', 'body')
        self.add_polyline('bent-leg', (24, 29), (38, 36), (24, 44), closed=False)
        self.relate('connect', 'body', 'bent-leg')
