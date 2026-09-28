'Praying Face with Hands Together.\n\nSymbol plan: Pleading face with closed eyes and two joined palms. Enlarge the palms and show curved closed eyes while omitting crowded brows and center crease.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nHuman references: human_ref/user.svg and full_body_ref.png; no useful Lucide subject match.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '866d6cda-38de-4dd8-9622-723649f45155'
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pleading-face-with-joined-hands/20260927T170245Z-thuan-mac-1/reference/face pleading_866d6cda-38de-4dd8-9622-723649f45155.svg"
AUTHOR = 'gpt-6'

class PleadingFaceWithJoinedHands(Solo48):
    icon_id = 'pleading-face-with-joined-hands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pleading', 'face', 'with', 'joined', 'hands')

    def build(self):
        # Pleading face with closed eyes and two joined palms. Enlarge the palms and show curved closed eyes while omitting crowded brows and center crease.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_26 = (8, 26)
        p_10_31 = (10, 31)
        p_12_44 = (12, 44)
        p_14_34 = (14, 34)
        p_17_37 = (17, 37)
        p_18_17 = (18, 17)
        p_24_25 = (24, 29)
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
        self.add_arc('eye-left', (17,19), (19,19), radius_x=2, sweep=False)
        self.add_arc('eye-right', (29,19), (31,19), radius_x=2, sweep=False)
