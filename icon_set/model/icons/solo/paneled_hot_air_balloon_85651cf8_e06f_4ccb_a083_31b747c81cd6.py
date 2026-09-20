'Hot Air Balloon with Basket.\n\nSymbol plan: Symmetric balloon envelope, one central seam, tapered throat and attached basket; reduce three panel bands to two wide panels.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85651cf8-e06f-4ccb-a083-31b747c81cd6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hot air balloon_85651cf8-e06f-4ccb-a083-31b747c81cd6.svg'
AUTHOR = 'gpt-6'

class PaneledHotAirBalloon(Solo48):
    icon_id = 'paneled-hot-air-balloon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('paneled', 'hot', 'air', 'balloon')

    def build(self):
        # Symmetric balloon envelope, one central seam, tapered throat and attached basket; reduce three panel bands to two wide panels.
        axis_x = 24
        p_8_9 = (8, 9)
        p_8_16 = (8, 16)
        p_8_22 = (8, 22)
        p_14_4 = (14, 4)
        p_17_27 = (17, 27)
        p_18_34 = (18, 34)
        p_18_44 = (18, 44)
        p_24_4 = (24, 4)
        p_24_25 = (24, 25)
        p_30_34 = (2 * axis_x - p_18_34[0], p_18_34[1])
        p_30_44 = (2 * axis_x - p_18_44[0], p_18_44[1])
        p_31_27 = (2 * axis_x - p_17_27[0], p_17_27[1])
        p_34_4 = (2 * axis_x - p_14_4[0], p_14_4[1])
        p_40_9 = (2 * axis_x - p_8_9[0], p_8_9[1])
        p_40_16 = (2 * axis_x - p_8_16[0], p_8_16[1])
        p_40_22 = (2 * axis_x - p_8_22[0], p_8_22[1])
        self.add_bezier('envelope-1', p_18_34, (p_17_27, p_8_22, p_8_16))
        self.add_bezier('envelope-2', p_8_16, (p_8_9, p_14_4, p_24_4))
        self.add_bezier('envelope-3', p_24_4, (p_34_4, p_40_9, p_40_16))
        self.add_bezier('envelope-4', p_40_16, (p_40_22, p_31_27, p_30_34))
        self.add_contour('envelope', 'envelope-1', 'envelope-2', 'envelope-3', 'envelope-4', closed=False)
        self.add_line('basket-1', p_18_34, p_18_44)
        self.add_line('basket-2', p_18_44, p_30_44)
        self.add_line('basket-3', p_30_44, p_30_34)
        self.add_line('basket-4', p_30_34, p_18_34)
        self.add_contour('basket', 'basket-1', 'basket-2', 'basket-3', 'basket-4', closed=False)
        self.relate("connect", 'envelope', 'basket')
        self.add_line('seam-1', p_24_4, p_24_25)
        self.add_contour('seam', 'seam-1', closed=False)
        self.relate("connect", 'seam', 'envelope')
