"""A narrow standing figure extends the arms straight upward beside the head. The long torso and joined legs form one continuous upright silhouette with a softly rounded bottom.
Construction: Bounds (8,6)-(40,42). Standing with joined legs and two raised arms; use front-facing paired arms to keep openings clear. Remove doubled leg outlines.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd04c0f4f-bbd7-5070-aebb-a2e4f24da238'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountain-pose-raised-arms/20260927T153322Z-thuan-mac-1/reference/yoga mountain arms up pose_d04c0f4f-bbd7-5070-aebb-a2e4f24da238.svg'
AUTHOR = 'gpt-6'

class MountainPoseRaisedArms(Solo48):
    icon_id = 'mountain-pose-raised-arms'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('mountain', 'pose', 'raised', 'arms', 'yoga', 'exercise')

    def build(self):
        # Side-standing mountain pose with the right arm raised beside the head.
        self.add_arc('head-a',(10,14),(22,14),radius_x=6,sweep=True)
        self.add_arc('head-b',(22,14),(10,14),radius_x=6,sweep=True)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('body',(16,28),(8,32),(12,44),(32,44),(28,28))
        self.add_polyline('raised-arm',(28,28),(40,20),(40,4))
        self.relate('connect','body','raised-arm')
