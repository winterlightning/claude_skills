'A standing figure folds deeply at the hips into a tall rounded arch. Long arms descend beside the legs, and the circular head hangs outside the lower-right side of the folded torso.\nConstruction: Bounds (8,6)-(40,42). Tall rounded fold with long leg and descending arm; head hangs to the right. Remove parallel limb contours.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55834a1a-9348-5505-95a8-8fdda98bb904'
SOURCE_PATH = 'pictographic-primitives/sports/yoga standing forward fold pose_55834a1a-9348-5505-95a8-8fdda98bb904.svg'
AUTHOR = 'gpt-6'

class StandingForwardFold(Solo48):
    icon_id = 'standing-forward-fold'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('standing', 'forward', 'fold', 'yoga', 'exercise')

    def build(self):
        self.add_line('leg', (8, 42), (8, 16))
        self.add_arc('hip', (8, 16), (32, 16), radius_x=12, radius_y=12, sweep=True)
        self.add_line('torso-arm', (32, 16), (20, 42))
        self.add_contour('body', 'leg', 'hip', 'torso-arm', closed=False)
        self.add_arc('head-top', (34, 33), (40, 33), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (40, 33), (34, 33), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
