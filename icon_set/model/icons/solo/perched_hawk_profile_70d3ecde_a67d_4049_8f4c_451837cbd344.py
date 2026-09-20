'Perched Hawk Profile.\n\nSymbol plan: Perched hawk with hooked beak and a single folded-wing edge shared with its tail silhouette. Omit the crowded nested wing loop.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: bird.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70d3ecde-a67d-4049-8f4c-451837cbd344'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hawk_70d3ecde-a67d-4049-8f4c-451837cbd344.svg'
AUTHOR = 'gpt-6'

class PerchedHawkProfile(Solo48):
    icon_id = 'perched-hawk-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('perched', 'hawk', 'profile')

    def build(self):
        # Perched hawk with hooked beak and a single folded-wing edge shared with its tail silhouette. Omit the crowded nested wing loop.
        axis_x = 24
        p_8_38 = (8, 38)
        p_13_28 = (13, 28)
        p_22_34 = (22, 34)
        p_23_7 = (23, 7)
        p_23_13 = (23, 13)
        p_23_22 = (23, 22)
        p_27_4 = (27, 4)
        p_28_44 = (28, 44)
        p_30_34 = (30, 34)
        p_32_4 = (32, 4)
        p_34_12 = (34, 12)
        p_34_25 = (34, 25)
        p_36_44 = (36, 44)
        p_37_4 = (37, 4)
        p_40_8 = (40, 8)
        p_40_14 = (40, 14)
        self.add_bezier('outline-1', p_8_38, (p_13_28, p_23_22, p_23_13))
        self.add_bezier('outline-2', p_23_13, (p_23_7, p_27_4, p_32_4))
        self.add_bezier('outline-3', p_32_4, (p_37_4, p_40_8, p_40_14))
        self.add_line('outline-4', p_40_14, p_34_12)
        self.add_bezier('outline-5', p_34_12, (p_34_25, p_30_34, p_22_34))
        self.add_line('outline-6', p_22_34, p_8_38)
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
        self.add_line('leg-1', p_22_34, p_28_44)
        self.add_line('leg-2', p_28_44, p_36_44)
        self.add_contour('leg', 'leg-1', 'leg-2', closed=False)
        self.relate("connect", 'leg', 'outline')
