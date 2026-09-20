'Human Neck and Throat.\n\nSymbol plan: Cropped jaw, neck and sloping shoulders, with a central throat mark. Continuous neck is anatomically attached, not a detached stick head.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fc42246-18fd-4400-9169-26a01f5ca3d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/throat_2fc42246-18fd-4400-9169-26a01f5ca3d7.svg'
AUTHOR = 'gpt-6'

class FrontNeckThroatDetail(Solo48):
    icon_id = 'front-neck-throat-detail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('front', 'neck', 'throat', 'detail')

    def build(self):
        # Cropped jaw, neck and sloping shoulders, with a central throat mark. Continuous neck is anatomically attached, not a detached stick head.
        axis_x = 24
        p_6_33 = (6, 33)
        p_6_38 = (6, 38)
        p_6_42 = (6, 42)
        p_12_6 = (12, 6)
        p_12_12 = (12, 12)
        p_12_14 = (12, 14)
        p_12_28 = (12, 28)
        p_12_34 = (12, 34)
        p_14_17 = (14, 17)
        p_21_29 = (21, 29)
        p_24_17 = (24, 17)
        p_27_29 = (2 * axis_x - p_21_29[0], p_21_29[1])
        p_34_17 = (2 * axis_x - p_14_17[0], p_14_17[1])
        p_36_6 = (2 * axis_x - p_12_6[0], p_12_6[1])
        p_36_12 = (2 * axis_x - p_12_12[0], p_12_12[1])
        p_36_14 = (2 * axis_x - p_12_14[0], p_12_14[1])
        p_36_28 = (2 * axis_x - p_12_28[0], p_12_28[1])
        p_36_34 = (2 * axis_x - p_12_34[0], p_12_34[1])
        p_42_33 = (2 * axis_x - p_6_33[0], p_6_33[1])
        p_42_38 = (2 * axis_x - p_6_38[0], p_6_38[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('body-1', p_6_42, p_6_38)
        self.add_bezier('body-2', p_6_38, (p_6_33, p_12_34, p_12_28))
        self.add_line('body-3', p_12_28, p_12_14)
        self.add_line('body-4', p_12_14, p_12_6)
        self.add_bezier('body-5', p_12_6, (p_12_12, p_14_17, p_24_17))
        self.add_bezier('body-6', p_24_17, (p_34_17, p_36_12, p_36_6))
        self.add_line('body-7', p_36_6, p_36_14)
        self.add_line('body-8', p_36_14, p_36_28)
        self.add_bezier('body-9', p_36_28, (p_36_34, p_42_33, p_42_38))
        self.add_line('body-10', p_42_38, p_42_42)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', closed=False)
        self.add_arc('throat-1', p_21_29, p_27_29, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('throat-2', p_27_29, p_21_29, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('throat', 'throat-1', 'throat-2', closed=True)
