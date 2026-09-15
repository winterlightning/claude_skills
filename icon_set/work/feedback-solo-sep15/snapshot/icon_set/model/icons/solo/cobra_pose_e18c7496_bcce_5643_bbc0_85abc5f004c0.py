'A prone figure stretches the legs left along the ground while lifting the chest and head on the right. A straight supporting arm descends below the shoulder beside the upward-curving torso.\nConstruction: Bounds (6,8)-(42,40). Long ground-level legs rise into lifted chest, braced by straight arm. One continuous back curve replaces thick outlined body.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e18c7496-bcce-5643-bbc0-85abc5f004c0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga cobra pose_e18c7496-bcce-5643-bbc0-85abc5f004c0.svg'
AUTHOR = 'gpt-6'

class CobraPose(Solo48):
    icon_id = 'cobra-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('cobra', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (31, 11), (37, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (37, 11), (31, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('legs', (4, 40), (18, 36))
        self.add_arc('chest', (18, 36), (33, 23), radius_x=18, radius_y=18, sweep=False)
        self.add_contour('body', 'legs', 'chest', closed=False)
        self.add_line('arm', (33, 23), (44, 40))
        self.relate("connect", 'arm', 'body')
