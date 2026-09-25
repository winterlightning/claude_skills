'Hound Dog Head Profile.\n\nSymbol plan: Right-facing hound with hanging ear and broad muzzle; omit eyes absent in the reference.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: dog.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44555db3-5831-46c6-921d-f98ff556cf14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hound_44555db3-5831-46c6-921d-f98ff556cf14.svg'
AUTHOR = 'gpt-6'

class DroopEaredHoundHead(Solo48):
    icon_id = 'droop-eared-hound-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('droop', 'eared', 'hound', 'head')

    def build(self):
        # Right-facing hound with hanging ear and broad muzzle; omit eyes absent in the reference.
        axis_x = 24
        p_5_27 = (5, 27)
        p_6_42 = (6, 42)
        p_8_21 = (8, 21)
        p_10_30 = (10, 30)
        p_12_14 = (12, 14)
        p_13_35 = (13, 35)
        p_15_8 = (15, 8)
        p_18_6 = (18, 6)
        p_18_14 = (18, 14)
        p_19_29 = (19, 29)
        p_19_37 = (19, 37)
        p_22_6 = (22, 6)
        p_27_6 = (27, 6)
        p_28_31 = (28, 31)
        p_28_34 = (28, 34)
        p_28_42 = (28, 42)
        p_29_8 = (29, 8)
        p_31_13 = (31, 13)
        p_32_31 = (32, 31)
        p_33_19 = (33, 19)
        p_36_31 = (36, 31)
        p_38_18 = (38, 18)
        p_39_31 = (39, 31)
        p_42_21 = (42, 21)
        p_42_28 = (42, 28)
        self.add_line('head-1', p_6_42, p_10_30)
        self.add_bezier('head-2', p_10_30, (p_5_27, p_8_21, p_12_14))
        self.add_bezier('head-3', p_12_14, (p_15_8, p_18_6, p_22_6))
        self.add_bezier('head-4', p_22_6, (p_27_6, p_29_8, p_31_13))
        self.add_bezier('head-5', p_31_13, (p_33_19, p_38_18, p_42_21))
        self.add_bezier('head-6', p_42_21, (p_42_28, p_39_31, p_36_31))
        self.add_line('head-7', p_36_31, p_32_31)
        self.add_bezier('head-8', p_32_31, (p_28_31, p_28_34, p_28_42))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', closed=False)
        self.add_line('ear-1', p_18_14, p_19_29)
        self.add_bezier('ear-2', p_19_29, (p_19_37, p_13_35, p_10_30))
        self.add_contour('ear', 'ear-1', 'ear-2', closed=False)
        self.relate("connect", 'head', 'ear')
