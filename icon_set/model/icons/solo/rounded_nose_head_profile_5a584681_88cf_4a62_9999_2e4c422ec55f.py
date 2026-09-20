'Human Head Profile.\n\nSymbol plan: Open neck beneath rounded cranium and right-facing nose; simplified smooth facial contour.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a584681-88cf-4a62-9999-2e4c422ec55f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tenor_5a584681-88cf-4a62-9999-2e4c422ec55f.svg'
AUTHOR = 'gpt-6'

class RoundedNoseHeadProfile(Solo48):
    icon_id = 'rounded-nose-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('rounded', 'nose', 'head', 'profile')

    def build(self):
        # Open neck beneath rounded cranium and right-facing nose; simplified smooth facial contour.
        axis_x = 24
        p_8_9 = (8, 9)
        p_8_18 = (8, 18)
        p_8_26 = (8, 26)
        p_13_4 = (13, 4)
        p_15_28 = (15, 28)
        p_15_34 = (15, 34)
        p_15_44 = (15, 44)
        p_23_4 = (23, 4)
        p_27_36 = (27, 36)
        p_27_44 = (27, 44)
        p_31_36 = (31, 36)
        p_33_4 = (33, 4)
        p_34_26 = (34, 26)
        p_34_32 = (34, 32)
        p_34_36 = (34, 36)
        p_36_11 = (36, 11)
        p_36_18 = (36, 18)
        p_40_24 = (40, 24)
        self.add_line('profile-1', p_15_44, p_15_34)
        self.add_bezier('profile-2', p_15_34, (p_15_28, p_8_26, p_8_18))
        self.add_bezier('profile-3', p_8_18, (p_8_9, p_13_4, p_23_4))
        self.add_bezier('profile-4', p_23_4, (p_33_4, p_36_11, p_36_18))
        self.add_line('profile-5', p_36_18, p_40_24)
        self.add_line('profile-6', p_40_24, p_34_26)
        self.add_line('profile-7', p_34_26, p_34_32)
        self.add_bezier('profile-8', p_34_32, (p_34_36, p_31_36, p_27_36))
        self.add_line('profile-9', p_27_36, p_27_44)
        self.add_contour('profile', 'profile-1', 'profile-2', 'profile-3', 'profile-4', 'profile-5', 'profile-6', 'profile-7', 'profile-8', 'profile-9', closed=False)
