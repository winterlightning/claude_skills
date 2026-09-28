'A figure lunges with one bent front knee and the rear leg extended diagonally left. Both arms reach vertically overhead beside the head, lengthening the upright torso.\nConstruction: Bounds (6,6)-(42,42). Upright reaching arms with long rear leg and bent front knee. Single arm/leg strokes replace overlapping paired outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7531c3ff-b529-46cd-ad18-210cb444c4fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__warrior-pose-raised-arms/20260927T160114Z-thuan-mac-1/reference/yoga warrior pose_7531c3ff-b529-46cd-ad18-210cb444c4fb.svg'
AUTHOR = "gpt-6"

class WarriorPoseRaisedArms(Solo48):
    icon_id = 'warrior-pose-raised-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('warrior', 'pose', 'raised', 'arms', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (17, 12), (23, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (23, 12), (17, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arm-torso', (31, 6), (31, 24), (27, 32), closed=False)
        self.add_polyline('legs', (6, 42), (27, 32), (40, 35), (42, 42), closed=False)
        self.relate("connect", 'arm-torso', 'legs')
