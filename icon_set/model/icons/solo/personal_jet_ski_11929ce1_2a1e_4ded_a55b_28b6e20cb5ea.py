'Personal Watercraft Vehicle.\n\nSymbol plan: Jet-ski silhouette with raised seat, upswept bow and steering grip. Omit the long parallel internal deck seam.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11929ce1-2a1e-4ded-a55b-28b6e20cb5ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jet ski_11929ce1-2a1e-4ded-a55b-28b6e20cb5ea.svg'
AUTHOR = 'gpt-6'

class PersonalJetSki(Solo48):
    icon_id = 'personal-jet-ski'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('personal', 'jet', 'ski')

    def build(self):
        # Jet-ski silhouette with raised seat, upswept bow and steering grip. Omit the long parallel internal deck seam.
        axis_x = 24
        p_4_29 = (4, 29)
        p_4_37 = (4, 37)
        p_8_40 = (8, 40)
        p_14_40 = (14, 40)
        p_16_21 = (16, 21)
        p_17_8 = (17, 8)
        p_23_26 = (23, 26)
        p_25_8 = (25, 8)
        p_26_15 = (26, 15)
        p_27_40 = (27, 40)
        p_31_17 = (31, 17)
        p_35_40 = (35, 40)
        p_38_19 = (38, 19)
        p_40_37 = (40, 37)
        p_42_25 = (42, 25)
        p_44_29 = (2 * axis_x - p_4_29[0], p_4_29[1])
        self.add_line('hull-1', p_4_29, p_16_21)
        self.add_bezier('hull-2', p_16_21, (p_23_26, p_26_15, p_31_17))
        self.add_bezier('hull-3', p_31_17, (p_38_19, p_42_25, p_44_29))
        self.add_bezier('hull-4', p_44_29, (p_40_37, p_35_40, p_27_40))
        self.add_line('hull-5', p_27_40, p_14_40)
        self.add_bezier('hull-6', p_14_40, (p_8_40, p_4_37, p_4_29))
        self.add_contour('hull', 'hull-1', 'hull-2', 'hull-3', 'hull-4', 'hull-5', 'hull-6', closed=True)
        self.add_line('steering-1', p_31_17, p_25_8)
        self.add_line('steering-2', p_25_8, p_17_8)
        self.add_contour('steering', 'steering-1', 'steering-2', closed=False)
        self.relate("connect", 'steering', 'hull')
