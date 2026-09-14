'A figure lifts the hips into a broad inverted V with straight legs on the left and extended arms on the right. The round head hangs beneath the sloping torso near the arms.\nConstruction: Bounds (6,8)-(42,40). Broad inverted V, head below right slope; distinguish direction from the left-facing stretch. Remove double leg/arm outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fe7de29-69dc-4808-9579-295702797c76'
SOURCE_PATH = 'pictographic-primitives/sports/yoga downward facing dog pose_6fe7de29-69dc-4808-9579-295702797c76.svg'
AUTHOR = 'gpt-6'

class DownwardFacingDogPose(Solo48):
    icon_id = 'downward-facing-dog-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('downward', 'facing', 'dog', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 37), (27, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 37), (21, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (4, 40), (14, 8), (44, 40), closed=False)
