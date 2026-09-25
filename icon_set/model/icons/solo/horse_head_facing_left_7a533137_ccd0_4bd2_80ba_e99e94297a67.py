'Horse Head Profile.\n\nSymbol plan: Long left-facing muzzle, one pointed ear, curved mane and open neck; omit the short jaw crease to keep the muzzle open.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a533137-ccd0-4bd2-80ba-e99e94297a67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/filly_7a533137-ccd0-4bd2-80ba-e99e94297a67.svg'
AUTHOR = 'gpt-6'

class HorseHeadFacingLeft(Solo48):
    icon_id = 'horse-head-facing-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('horse', 'head', 'facing', 'left')

    def build(self):
        # Long left-facing muzzle, one pointed ear, curved mane and open neck; omit the short jaw crease to keep the muzzle open.
        axis_x = 24
        p_8_26 = (8, 26)
        p_8_29 = (8, 29)
        p_8_34 = (8, 34)
        p_9_24 = (9, 24)
        p_11_21 = (11, 21)
        p_12_35 = (12, 35)
        p_16_30 = (16, 30)
        p_18_4 = (18, 4)
        p_18_11 = (18, 11)
        p_20_28 = (20, 28)
        p_20_44 = (20, 44)
        p_24_27 = (24, 27)
        p_25_10 = (25, 10)
        p_26_22 = (26, 22)
        p_27_35 = (27, 35)
        p_29_27 = (29, 27)
        p_35_11 = (35, 11)
        p_40_21 = (40, 21)
        p_40_32 = (40, 32)
        p_40_44 = (40, 44)
        self.add_bezier('horse-1', p_20_44, (p_27_35, p_29_27, p_26_22))
        self.add_bezier('horse-2', p_26_22, (p_24_27, p_20_28, p_16_30))
        self.add_bezier('horse-3', p_16_30, (p_12_35, p_8_34, p_8_29))
        self.add_bezier('horse-4', p_8_29, (p_8_26, p_9_24, p_11_21))
        self.add_line('horse-5', p_11_21, p_18_11)
        self.add_line('horse-6', p_18_11, p_18_4)
        self.add_line('horse-7', p_18_4, p_25_10)
        self.add_bezier('horse-8', p_25_10, (p_35_11, p_40_21, p_40_32))
        self.add_line('horse-9', p_40_32, p_40_44)
        self.add_contour('horse', 'horse-1', 'horse-2', 'horse-3', 'horse-4', 'horse-5', 'horse-6', 'horse-7', 'horse-8', 'horse-9', closed=False)
