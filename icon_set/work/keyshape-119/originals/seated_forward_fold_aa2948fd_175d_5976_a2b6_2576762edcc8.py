'A low seated figure folds the rounded back over the legs and stretches both arms forward along the ground to the left. The lowered circular head sits just above the extended arms.\nConstruction: Bounds (6,8)-(42,40). Rounded folded back over outstretched legs, lowered head left; remove doubled limbs.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa2948fd-175d-5976-a2b6-2576762edcc8'
SOURCE_PATH = 'pictographic-primitives/sports/yoga seated forward fold pose_aa2948fd-175d-5976-a2b6-2576762edcc8.svg'
AUTHOR = 'gpt-6'

class SeatedForwardFold(Solo48):
    icon_id = 'seated-forward-fold'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('seated', 'forward', 'fold', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (8, 27), (14, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (14, 27), (8, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('back-top', (24, 8), (42, 28), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('back-bottom', (42, 28), (32, 40), radius_x=12, radius_y=12, sweep=True)
        self.add_line('legs-1', (32, 40), (6, 40))
        self.add_contour('body', 'back-top', 'back-bottom', 'legs-1', closed=False)
        self.add_line('reaching-arm', (24, 8), (24, 28))
        self.relate("connect", 'body', 'reaching-arm')
