'A figure lifts the hips into a broad inverted V with straight legs on the left and extended arms on the right. The round head hangs beneath the sloping torso near the arms.\nConstruction: Bounds (6,8)-(42,40). Broad inverted V, head below right slope; distinguish direction from the left-facing stretch. Remove double leg/arm outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6fe7de29-69dc-4808-9579-295702797c76'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__downward-facing-dog-pose/20260927T135945Z-thuan-mac-1/reference/yoga downward facing dog pose_6fe7de29-69dc-4808-9579-295702797c76.svg'
AUTHOR = 'gpt-6'

class DownwardFacingDogPose(Solo48):
    icon_id = 'downward-facing-dog-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('downward', 'facing', 'dog', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (22, 36), (30, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-bottom', (30, 36), (22, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (4, 40), (14, 8), (34, 26), (44, 40), closed=False)
        self.add_line('neck', (34, 26), (26, 32))
        self.relate('connect', 'body', 'neck')
        self.relate('connect', 'head', 'neck')
        self.mark_human_figure('person', head='head', torso='body-2', torso_junction='end')
