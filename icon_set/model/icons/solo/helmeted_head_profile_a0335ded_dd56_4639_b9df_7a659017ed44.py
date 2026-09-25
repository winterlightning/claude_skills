'Military Combat Helmet.\n\nSymbol plan: Domed protective helmet above a blank head profile; retain forward brim and lowered rear edge.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0335ded-dd56-4639-b9df-7a659017ed44'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/helmet safety_a0335ded-dd56-4639-b9df-7a659017ed44.svg'
AUTHOR = 'gpt-6'

class HelmetedHeadProfile(Solo48):
    icon_id = 'helmeted-head-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('helmeted', 'head', 'profile')

    def build(self):
        # Domed protective helmet above a blank head profile; retain forward brim and lowered rear edge.
        axis_x = 24
        p_4_24 = (4, 24)
        p_8_12 = (8, 12)
        p_8_20 = (8, 20)
        p_16_8 = (16, 8)
        p_17_32 = (17, 32)
        p_17_36 = (17, 36)
        p_21_40 = (21, 40)
        p_26_8 = (26, 8)
        p_29_24 = (29, 24)
        p_31_40 = (31, 40)
        p_36_28 = (36, 28)
        p_36_36 = (36, 36)
        p_38_8 = (38, 8)
        p_38_28 = (38, 28)
        p_44_16 = (44, 16)
        p_44_28 = (44, 28)
        self.add_line('helmet-1', p_4_24, p_8_20)
        self.add_bezier('helmet-2', p_8_20, (p_8_12, p_16_8, p_26_8))
        self.add_bezier('helmet-3', p_26_8, (p_38_8, p_44_16, p_44_28))
        self.add_line('helmet-4', p_44_28, p_36_28)
        self.add_line('helmet-5', p_36_28, p_29_24)
        self.add_line('helmet-6', p_29_24, p_4_24)
        self.add_contour('helmet', 'helmet-1', 'helmet-2', 'helmet-3', 'helmet-4', 'helmet-5', 'helmet-6', closed=True)
        self.add_line('head-1', p_17_32, p_17_36)
        self.add_arc('head-2', p_17_36, p_21_40, radius_x=4, radius_y=4, sweep=False)
        self.add_bezier('head-3', p_21_40, (p_31_40, p_36_36, p_38_28))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', closed=False)
        self.relate("connect", 'helmet', 'head')
