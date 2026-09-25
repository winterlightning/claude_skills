'A folded figure stretches a long limb horizontally to the left above its lowered round head. The torso bends sharply down at the right and ends in a short outward-curving support.\nConstruction: Bounds (6,8)-(42,40). Long folded leg above head and low shoulder support; preserve the asymmetric fold, simplify paired limb outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e73cd4c7-5003-4fa0-b716-19121f8fa738'
SOURCE_PATH = 'pictographic-primitives/sports/yoga back stretch_e73cd4c7-5003-4fa0-b716-19121f8fa738.svg'
AUTHOR = 'gpt-6'

class PlowBackStretch(Solo48):
    icon_id = 'plow-back-stretch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('plow', 'back', 'stretch', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (18, 37), (24, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (24, 37), (18, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('raised-leg', (4, 15), (30, 8))
        self.add_arc('hip', (30, 8), (36, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('back', (36, 14), (34, 34))
        self.add_arc('shoulder', (34, 34), (40, 40), radius_x=6, radius_y=6, sweep=False)
        self.add_line('arm', (40, 40), (44, 40))
        self.add_contour('body', 'raised-leg', 'hip', 'back', 'shoulder', 'arm', closed=False)
