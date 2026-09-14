"""A wide-legged figure bends the torso sideways, reaching one arm down between the legs. The other arm rises diagonally overhead, with the circular head beside the tilted upper body.
Construction: Bounds (8,6)-(40,42). One arm reaches up and another down beside tilted torso; wide stance retains unequal knees. Remove doubled limbs.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6536663-b340-5128-bbbb-fbd254093c96'
SOURCE_PATH = 'pictographic-primitives/sports/yoga twisting triangle pose_c6536663-b340-5128-bbbb-fbd254093c96.svg'
AUTHOR = 'gpt-6'

class TwistingTrianglePoseVariant2(Solo48):
    icon_id = 'twisting-triangle-pose-v2'
    variant_of = 'twisting-triangle-pose'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('twisting', 'triangle', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (8, 15), (14, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (14, 15), (8, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('torso', (26, 4), (22, 10), (22, 25), (28, 32), closed=False)
        self.add_polyline('legs', (8, 44), (22, 25), (33, 28), (40, 44), closed=False)
        self.relate('connect', 'torso', 'legs')
        self.add_line('low-arm', (22, 25), (17, 44))
        self.relate('connect', 'low-arm', 'torso')
        self.relate('connect', 'low-arm', 'legs')
