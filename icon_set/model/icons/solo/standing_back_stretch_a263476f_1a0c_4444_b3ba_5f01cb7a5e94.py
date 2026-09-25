"""A balancing figure bends the torso forward with one arm extending horizontally to the right. One knee folds high beside the body while the supporting leg drops straight downward.
Construction: Bounds (8,6)-(40,42). Retain right-reaching arm, high bent knee and supporting leg; omit secondary limb outlines. Asymmetric balance pose.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a263476f-1a0c-4444-b3ba-5f01cb7a5e94'
SOURCE_PATH = 'pictographic-primitives/sports/yoga back stretch_a263476f-1a0c-4444-b3ba-5f01cb7a5e94.svg'
AUTHOR = 'gpt-6'

class StandingBackStretch(Solo48):
    icon_id = 'standing-back-stretch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('standing', 'back', 'stretch', 'yoga', 'exercise')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('head-top', (8, 7), (14, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (14, 7), (8, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('back', (22, 7), (28, 23), (23, 30), (23, 44), closed=False)
        self.add_polyline('arm', (28, 23), (29, 11), (40, 11), closed=False)
        self.relate('connect', 'back', 'arm')
        self.add_polyline('raised-knee', (23, 30), (38, 30), (38, 20), closed=False)
        self.relate('connect', 'back', 'raised-knee')
