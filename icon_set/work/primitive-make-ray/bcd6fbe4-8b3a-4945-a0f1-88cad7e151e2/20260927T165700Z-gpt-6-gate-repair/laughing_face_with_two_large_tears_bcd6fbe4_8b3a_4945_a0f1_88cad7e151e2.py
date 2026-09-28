'Laughing Face with Tears of Joy.\n\nSymbol plan: Laughing face with two tears shown as outward cheek trails; omit closed tear outlines to prevent trapped pockets.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bcd6fbe4-8b3a-4945-a0f1-88cad7e151e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laughing-face-with-two-large-tears/20260927T164305Z-thuan-mac-1/reference/face grin squint tears_bcd6fbe4-8b3a-4945-a0f1-88cad7e151e2.svg'
AUTHOR = "gpt-6"

class LaughingFaceWithTwoLargeTears(Solo48):
    icon_id = 'laughing-face-with-two-large-tears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('laughing', 'face', 'with', 'two', 'large', 'tears')

    def build(self):
        # Laughing face with two tears shown as outward cheek trails; omit closed tear outlines to prevent trapped pockets.
        axis_x = 24
        p_6_24 = (6, 24)
        p_6_42 = (6, 42)
        p_9_34 = (9, 34)
        p_15_20 = (15, 20)
        p_17_18 = (17, 18)
        p_18_18 = (18, 18)
        p_19_30 = (19, 30)
        p_20_20 = (20, 20)
        p_22_34 = (22, 34)
        p_26_34 = (2 * axis_x - p_22_34[0], p_22_34[1])
        p_28_20 = (2 * axis_x - p_20_20[0], p_20_20[1])
        p_29_30 = (2 * axis_x - p_19_30[0], p_19_30[1])
        p_30_18 = (2 * axis_x - p_18_18[0], p_18_18[1])
        p_31_18 = (2 * axis_x - p_17_18[0], p_17_18[1])
        p_33_20 = (2 * axis_x - p_15_20[0], p_15_20[1])
        p_39_34 = (2 * axis_x - p_9_34[0], p_9_34[1])
        p_42_24 = (2 * axis_x - p_6_24[0], p_6_24[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_arc('face-1', p_6_24, p_42_24, radius_x=18, radius_y=18, sweep=True)
        self.add_arc('face-2', p_42_24, p_6_24, radius_x=18, radius_y=18, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', closed=True)
        # Open curved tear trails keep the drops legible without tiny trapped holes.
        self.add_bezier('left-tear-curve', p_9_34, ((8, 37), (6, 39), p_6_42))
        self.add_contour('left-tear', 'left-tear-curve', closed=False)
        self.add_bezier('right-tear-curve', p_39_34, ((40, 37), (42, 39), p_42_42))
        self.add_contour('right-tear', 'right-tear-curve', closed=False)
        self.relate("connect", 'face', 'left-tear')
        self.relate("connect", 'face', 'right-tear')
        # A broad open laugh replaces the tiny ordinary smile.
        self.add_bezier('smile-1', (15, 28), ((18, 35), (30, 35), (33, 28)))
        self.add_contour('smile', 'smile-1', closed=False)
        self.add_bezier('eye-left-1', p_15_20, (p_17_18, p_18_18, p_20_20))
        self.add_contour('eye-left', 'eye-left-1', closed=False)
        self.add_bezier('eye-right-1', p_28_20, (p_30_18, p_31_18, p_33_20))
        self.add_contour('eye-right', 'eye-right-1', closed=False)
