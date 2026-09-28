'A standing figure stretches both arms horizontally at shoulder height. The legs spread into a wide stance with one knee bent, beneath a straight torso and centered circular head.\nConstruction: Bounds (6,6)-(42,42). Level arms, centered torso, one bent knee; preserve asymmetric stance and remove outlined hands.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e61808a5-f322-4582-85a4-6abce115f0c6'
SOURCE_PATH = 'pictographic-primitives/sports/yoga shoulder stretch_e61808a5-f322-4582-85a4-6abce115f0c6.svg'
AUTHOR = 'gpt-6'

class WideStanceShoulderStretch(Solo48):
    icon_id = 'wide-stance-shoulder-stretch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('wide', 'stance', 'shoulder', 'stretch', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (6, 21), (24, 21), (42, 21), closed=False)
        self.add_line('torso', (24, 21), (24, 31))
        self.relate("connect", 'arms', 'torso')
        self.add_polyline('legs', (6, 42), (24, 31), (36, 34), (36, 42), closed=False)
        self.relate("connect", 'torso', 'legs')
