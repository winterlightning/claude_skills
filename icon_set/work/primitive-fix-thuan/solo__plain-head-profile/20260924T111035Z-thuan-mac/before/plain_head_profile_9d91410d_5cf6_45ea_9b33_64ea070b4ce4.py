'Human Head Profile View.\n\nSymbol plan: Right-facing head with nose and chin; omit fine lip serrations which close at 4px stroke.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d91410d-5cf6-45ea-9b33-64ea070b4ce4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/head side_9d91410d-5cf6-45ea-9b33-64ea070b4ce4.svg'
AUTHOR = 'gpt-6'

class PlainHeadProfile(Solo48):
    icon_id = 'plain-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('plain', 'head', 'profile')

    def build(self):
        # Right-facing head with nose and chin; omit fine lip serrations which close at 4px stroke.
        axis_x = 24
        p_8_9 = (8, 9)
        p_8_19 = (8, 19)
        p_8_31 = (8, 31)
        p_13_4 = (13, 4)
        p_14_44 = (14, 44)
        p_17_34 = (17, 34)
        p_24_4 = (24, 4)
        p_25_44 = (25, 44)
        p_26_36 = (26, 36)
        p_31_36 = (31, 36)
        p_34_4 = (34, 4)
        p_34_27 = (34, 27)
        p_35_19 = (35, 19)
        p_35_32 = (35, 32)
        p_36_38 = (36, 38)
        p_37_11 = (37, 11)
        p_40_25 = (40, 25)
        self.add_bezier('profile-1', p_14_44, (p_17_34, p_8_31, p_8_19))
        self.add_bezier('profile-2', p_8_19, (p_8_9, p_13_4, p_24_4))
        self.add_bezier('profile-3', p_24_4, (p_34_4, p_37_11, p_35_19))
        self.add_line('profile-4', p_35_19, p_40_25)
        self.add_line('profile-5', p_40_25, p_34_27)
        self.add_line('profile-6', p_34_27, p_35_32)
        self.add_bezier('profile-7', p_35_32, (p_36_38, p_31_36, p_26_36))
        self.add_line('profile-8', p_26_36, p_25_44)
        self.add_contour('profile', 'profile-1', 'profile-2', 'profile-3', 'profile-4', 'profile-5', 'profile-6', 'profile-7', 'profile-8', closed=False)
