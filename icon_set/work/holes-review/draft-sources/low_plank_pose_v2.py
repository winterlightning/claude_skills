# Variant of low-plank-pose; parent file remains unchanged.
"""A low figure holds the body nearly straight on a shallow diagonal, with the head at the right. A bent arm supports the shoulder while the long legs extend back to the left.
Construction: Bounds (6,8)-(42,40). Shallow body diagonal with bent supporting forearm; right-facing head. Remove second outline of the legs.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9439df77-0cdb-5ac3-878e-3030ec5b7a19'
SOURCE_PATH = 'pictographic-primitives/sports/yoga low plank pose_9439df77-0cdb-5ac3-878e-3030ec5b7a19.svg'
AUTHOR = 'gpt-6'

class LowPlankPoseVariant2(Solo48):
    icon_id = 'low-plank-pose-v2'
    variant_of = 'low-plank-pose'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('low', 'plank', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (38, 11), (42, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (42, 11), (38, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (6, 40), (29, 17), (29, 31), closed=False)
        self.add_polyline('forearm', (29, 31), (24, 40), closed=False)
        self.relate('connect', 'body', 'forearm')
