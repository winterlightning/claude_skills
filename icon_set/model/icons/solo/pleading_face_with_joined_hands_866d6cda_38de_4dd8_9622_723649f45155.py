'Praying Face with Hands Together.\n\nSymbol plan: Pleading face with closed eyes and two joined palms. Enlarge the palms and remove their crowded center crease and small brows.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '866d6cda-38de-4dd8-9622-723649f45155'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face pleading_866d6cda-38de-4dd8-9622-723649f45155.svg'
AUTHOR = 'gpt-6'

class PleadingFaceWithJoinedHands(Solo48):
    icon_id = 'pleading-face-with-joined-hands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pleading', 'face', 'with', 'joined', 'hands')

    def build(self):
        # Pleading face with closed eyes and two joined palms. Enlarge the palms and remove their crowded center crease and small brows.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_26 = (8, 26)
        p_10_31 = (10, 31)
        p_12_44 = (12, 44)
        p_14_34 = (14, 34)
        p_17_37 = (17, 37)
        p_18_17 = (18, 17)
        p_24_25 = (24, 25)
        p_30_17 = (2 * axis_x - p_18_17[0], p_18_17[1])
        p_31_37 = (2 * axis_x - p_17_37[0], p_17_37[1])
        p_34_34 = (2 * axis_x - p_14_34[0], p_14_34[1])
        p_36_44 = (2 * axis_x - p_12_44[0], p_12_44[1])
        p_38_31 = (2 * axis_x - p_10_31[0], p_10_31[1])
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_40_26 = (2 * axis_x - p_8_26[0], p_8_26[1])
        self.add_bezier('face-1', p_14_34, (p_10_31, p_8_26, p_8_20))
        self.add_arc('face-2', p_8_20, p_40_20, radius_x=16, radius_y=16, sweep=True)
        self.add_bezier('face-3', p_40_20, (p_40_26, p_38_31, p_34_34))
        self.add_contour('face', 'face-1', 'face-2', 'face-3', closed=False)
        self.add_line('hands-1', p_12_44, p_17_37)
        self.add_line('hands-2', p_17_37, p_24_25)
        self.add_line('hands-3', p_24_25, p_31_37)
        self.add_line('hands-4', p_31_37, p_36_44)
        self.add_contour('hands', 'hands-1', 'hands-2', 'hands-3', 'hands-4', closed=False)
        self.relate("connect", 'hands', 'face')
        self.add_line('eye-left-1', p_18_17, p_18_17)
        self.add_contour('eye-left', 'eye-left-1', closed=False)
        self.add_line('eye-right-1', p_30_17, p_30_17)
        self.add_contour('eye-right', 'eye-right-1', closed=False)
