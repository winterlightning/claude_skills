'A figure lunges with one bent front knee and the rear leg extended diagonally left. Both arms reach vertically overhead beside the head, lengthening the upright torso.\nConstruction: Bounds (6,6)-(42,42). Upright reaching arms with long rear leg and bent front knee. Single arm/leg strokes replace overlapping paired outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7531c3ff-b529-46cd-ad18-210cb444c4fb'
SOURCE_PATH = 'pictographic-primitives/sports/yoga warrior pose_7531c3ff-b529-46cd-ad18-210cb444c4fb.svg'
AUTHOR = 'gpt-6'

class WarriorPoseRaisedArms(Solo48):
    icon_id = 'warrior-pose-raised-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('warrior', 'pose', 'raised', 'arms', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (14, 12), (20, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (20, 12), (14, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arm-torso', (31, 6), (31, 24), (27, 32), closed=False)
        self.add_polyline('legs', (6, 42), (27, 32), (40, 35), (42, 42), closed=False)
        self.relate("connect", 'arm-torso', 'legs')
