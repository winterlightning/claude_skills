'A figure stands in a broad lunge with one knee bent and the other leg stretched diagonally outward. Both arms extend horizontally from the shoulders beneath the centered circular head.\nConstruction: Bounds (6,6)-(42,42). Horizontal shoulder span above a left bent knee and right extended leg; direction distinguishes this lunge from shoulder stretch.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'facfd6f9-4a93-42ef-ae5f-7f7c17afd7a6'
SOURCE_PATH = 'pictographic-primitives/sports/yoga warrior pose_facfd6f9-4a93-42ef-ae5f-7f7c17afd7a6.svg'
AUTHOR = 'gpt-6'

class WarriorPoseExtendedArms(Solo48):
    icon_id = 'warrior-pose-extended-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('warrior', 'pose', 'extended', 'arms', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (6, 21), (24, 21), (42, 21), closed=False)
        self.add_line('body', (24, 21), (24, 31))
        self.relate("connect", 'body', 'arms')
        self.add_polyline('legs', (10, 42), (10, 36), (24, 31), (40, 42), closed=False)
        self.relate("connect", 'body', 'legs')
