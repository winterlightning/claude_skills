'A figure sits upright with the legs crossed broadly in front. The arms extend down along the rounded torso, while a plain circular head sits centered above the shoulders.\nConstruction: Bounds (6,6)-(42,42). Shared axis with resting arms and broad crossed legs; simplify rounded torso outline into connected limb strokes. Equivalent source compositions share the same construction.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da87e4f0-75c3-43bf-bec0-675953355d74'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditation pose_da87e4f0-75c3-43bf-bec0-675953355d74.svg'
AUTHOR = 'gpt-6'

class SeatedMeditationBroadCross(Solo48):
    icon_id = 'seated-meditation-broad-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('seated', 'meditation', 'broad', 'cross', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (9, 30), (12, 21), (24, 21), (36, 21), (39, 30), closed=False)
        self.add_line('torso', (24, 21), (24, 38))
        self.relate("connect", 'arms', 'torso')
        self.add_polyline('leg-l', (6, 34), (24, 38), (42, 42), closed=False)
        self.add_polyline('leg-r', (42, 34), (24, 38), (6, 42), closed=False)
        self.relate("connect", 'leg-l', 'leg-r')
        self.relate("connect", 'torso', 'leg-l')
        self.relate("connect", 'torso', 'leg-r')
