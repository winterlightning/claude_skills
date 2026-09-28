"""A front-facing figure stands upright with the feet together and arms resting down beside the torso. The body has rounded shoulders and a separate circular head centered above.
Construction: Bounds (8,6)-(40,42). Mirror rounded shoulders and resting arms; one vertical stroke denotes feet-together stance. Remove doubled body boundary.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '827a6183-d0a3-4c08-a449-f0bddf6114b0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountain-pose/20260927T153322Z-thuan-mac-1/reference/yoga mountain pose_827a6183-d0a3-4c08-a449-f0bddf6114b0.svg'
AUTHOR = "gpt-6"

class MountainPose(Solo48):
    icon_id = 'mountain-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('mountain', 'pose', 'yoga', 'exercise')

    def build(self):
        # Calm upright pose: head, shoulders, down arms, hips, and two legs.
        self.add_arc('head-a',(24,4),(24,14),radius_x=5,sweep=True)
        self.add_arc('head-b',(24,14),(24,4),radius_x=5,sweep=True)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('shoulders',(8,36),(8,28),(14,22),(24,22),(34,22),(40,28),(40,36))
        self.add_line('torso',(24,22),(24,32))
        self.add_line('hips',(18,32),(30,32))
        self.add_line('leg-left',(20,32),(20,44))
        self.add_line('leg-right',(28,32),(28,44))
        self.relate('connect','shoulders','torso')
        self.relate('connect','torso','hips')
        self.relate('connect','hips','leg-left','leg-right')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
