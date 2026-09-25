'Human Leg in Sitting Position.\n\nSymbol plan: Bent leg with a broad knee and left-projecting foot; smooth contour, no tiny internal knee crease.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87d9a32d-418e-48eb-9d3b-c61d18048ab3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/limb_87d9a32d-418e-48eb-9d3b-c61d18048ab3.svg'
AUTHOR = 'gpt-6'

class BentLeg(Solo48):
    icon_id = 'bent-leg'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bent', 'leg')

    def build(self):
        # Bent leg with a broad knee and left-projecting foot; smooth contour, no tiny internal knee crease.
        axis_x = 24
        p_8_39 = (8, 39)
        p_8_42 = (8, 42)
        p_8_44 = (8, 44)
        p_12_25 = (12, 25)
        p_13_19 = (13, 19)
        p_14_34 = (14, 34)
        p_14_39 = (14, 39)
        p_15_44 = (15, 44)
        p_22_28 = (22, 28)
        p_22_44 = (22, 44)
        p_25_4 = (25, 4)
        p_25_17 = (25, 17)
        p_25_22 = (25, 22)
        p_30_28 = (30, 28)
        p_40_4 = (40, 4)
        p_40_18 = (40, 18)
        p_40_24 = (40, 24)
        p_40_28 = (40, 28)
        self.add_line('leg-1', p_25_4, p_25_17)
        self.add_bezier('leg-2', p_25_17, (p_25_22, p_13_19, p_12_25))
        self.add_line('leg-3', p_12_25, p_14_34)
        self.add_bezier('leg-4', p_14_34, (p_14_39, p_8_39, p_8_42))
        self.add_bezier('leg-5', p_8_42, (p_8_44, p_15_44, p_22_44))
        self.add_line('leg-6', p_22_44, p_22_28)
        self.add_line('leg-7', p_22_28, p_30_28)
        self.add_bezier('leg-8', p_30_28, (p_40_28, p_40_24, p_40_18))
        self.add_line('leg-9', p_40_18, p_40_4)
        self.add_contour('leg', 'leg-1', 'leg-2', 'leg-3', 'leg-4', 'leg-5', 'leg-6', 'leg-7', 'leg-8', 'leg-9', closed=False)
