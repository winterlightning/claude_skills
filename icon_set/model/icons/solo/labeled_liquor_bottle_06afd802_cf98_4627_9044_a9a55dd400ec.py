'Liquor Bottle with Label.\n\nSymbol plan: Capped liquor bottle with broad shoulders and blank rectangular label.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06afd802-cf98-4627-9044-a9a55dd400ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vodka_06afd802-cf98-4627-9044-a9a55dd400ec.svg'
AUTHOR = 'gpt-6'

class LabeledLiquorBottle(Solo48):
    icon_id = 'labeled-liquor-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('labeled', 'liquor', 'bottle')

    def build(self):
        # Capped liquor bottle with broad shoulders and blank rectangular label.
        axis_x = 24
        p_10_18 = (10, 18)
        p_10_24 = (10, 24)
        p_10_40 = (10, 40)
        p_14_44 = (14, 44)
        p_18_4 = (18, 4)
        p_18_14 = (18, 14)
        p_18_18 = (18, 18)
        p_19_26 = (19, 26)
        p_19_35 = (19, 35)
        p_29_26 = (2 * axis_x - p_19_26[0], p_19_26[1])
        p_29_35 = (2 * axis_x - p_19_35[0], p_19_35[1])
        p_30_4 = (2 * axis_x - p_18_4[0], p_18_4[1])
        p_30_14 = (2 * axis_x - p_18_14[0], p_18_14[1])
        p_30_18 = (2 * axis_x - p_18_18[0], p_18_18[1])
        p_34_44 = (2 * axis_x - p_14_44[0], p_14_44[1])
        p_38_18 = (2 * axis_x - p_10_18[0], p_10_18[1])
        p_38_24 = (2 * axis_x - p_10_24[0], p_10_24[1])
        p_38_40 = (2 * axis_x - p_10_40[0], p_10_40[1])
        self.add_line('bottle-1', p_18_4, p_30_4)
        self.add_line('bottle-2', p_30_4, p_30_14)
        self.add_bezier('bottle-3', p_30_14, (p_30_18, p_38_18, p_38_24))
        self.add_line('bottle-4', p_38_24, p_38_40)
        self.add_arc('bottle-5', p_38_40, p_34_44, radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottle-6', p_34_44, p_14_44)
        self.add_arc('bottle-7', p_14_44, p_10_40, radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottle-8', p_10_40, p_10_24)
        self.add_bezier('bottle-9', p_10_24, (p_10_18, p_18_18, p_18_14))
        self.add_line('bottle-10', p_18_14, p_18_4)
        self.add_contour('bottle', 'bottle-1', 'bottle-2', 'bottle-3', 'bottle-4', 'bottle-5', 'bottle-6', 'bottle-7', 'bottle-8', 'bottle-9', 'bottle-10', closed=True)
        self.add_line('label-1', p_19_26, p_29_26)
        self.add_line('label-2', p_29_26, p_29_35)
        self.add_line('label-3', p_29_35, p_19_35)
        self.add_line('label-4', p_19_35, p_19_26)
        self.add_contour('label', 'label-1', 'label-2', 'label-3', 'label-4', closed=True)
