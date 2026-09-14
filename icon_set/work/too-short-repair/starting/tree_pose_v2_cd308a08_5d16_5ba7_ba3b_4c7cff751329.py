# Variant of tree-pose; parent file remains unchanged.
"""A figure balances on one straight leg while the opposite foot rests against its inner side, forming a triangular knee opening. Both arms curve overhead around the circular head.
Construction: Bounds (8,6)-(40,42). Mirror overhead arms, but retain the single folded knee and straight supporting leg. Triangle of bent knee remains open.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd308a08-5d16-5ba7-ba3b-4c7cff751329'
SOURCE_PATH = 'pictographic-primitives/sports/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg'
AUTHOR = 'gpt-6'

class TreePoseVariant2(Solo48):
    icon_id = 'tree-pose-v2'
    variant_of = 'tree-pose'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tree', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 12), (27, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 12), (21, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm-l', (8, 6), (8, 8))
        self.add_arc('shoulder-l', (8, 8), (24, 24), radius_x=16, radius_y=16, sweep=False)
        self.add_arc('shoulder-r', (24, 24), (40, 8), radius_x=16, radius_y=16, sweep=False)
        self.add_line('arm-r', (40, 8), (40, 6))
        self.add_contour('arms', 'arm-l', 'shoulder-l', 'shoulder-r', 'arm-r', closed=False)
        self.add_polyline('body', (24, 24), (24, 29), (24, 42), (24, 42), closed=False)
        self.relate('connect', 'arms', 'body')
        self.add_polyline('bent-leg', (24, 29), (38, 36), (24, 42), closed=False)
        self.relate('connect', 'body', 'bent-leg')
