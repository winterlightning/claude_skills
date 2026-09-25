'Protective Medical Glove.\n\nSymbol plan: Four rounded fingers and broad glove palm; a single projecting thumb stroke replaces its crowded outline. Finger divisions use equal eight-unit spacing.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6288b5a8-887b-4031-b7cf-6d2c2cf7edf6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/latex_6288b5a8-887b-4031-b7cf-6d2c2cf7edf6.svg'
AUTHOR = 'gpt-6'

class LatexGlove(Solo48):
    icon_id = 'latex-glove'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('latex', 'glove')

    def build(self):
        # Four rounded fingers and broad glove palm; a single projecting thumb stroke replaces its crowded outline. Finger divisions use equal eight-unit spacing.
        axis_x = 24
        p_4_24 = (4, 24)
        p_12_16 = (12, 16)
        p_12_28 = (12, 28)
        p_12_32 = (12, 32)
        p_14_36 = (14, 36)
        p_18_40 = (18, 40)
        p_20_12 = (20, 12)
        p_20_16 = (20, 16)
        p_20_26 = (20, 26)
        p_28_12 = (2 * axis_x - p_20_12[0], p_20_12[1])
        p_28_14 = (28, 14)
        p_28_26 = (2 * axis_x - p_20_26[0], p_20_26[1])
        p_36_14 = (36, 14)
        p_36_18 = (36, 18)
        p_36_26 = (36, 26)
        p_38_40 = (38, 40)
        p_40_36 = (40, 36)
        p_44_18 = (44, 18)
        p_44_30 = (44, 30)
        p_44_35 = (44, 35)
        self.add_line('glove-1', p_12_28, p_12_16)
        self.add_arc('glove-2', p_12_16, p_20_16, radius_x=4, radius_y=4, sweep=True)
        self.add_line('glove-3', p_20_16, p_20_12)
        self.add_arc('glove-4', p_20_12, p_28_12, radius_x=4, radius_y=4, sweep=True)
        self.add_line('glove-5', p_28_12, p_28_14)
        self.add_arc('glove-6', p_28_14, p_36_14, radius_x=4, radius_y=4, sweep=True)
        self.add_line('glove-7', p_36_14, p_36_18)
        self.add_arc('glove-8', p_36_18, p_44_18, radius_x=4, radius_y=4, sweep=True)
        self.add_line('glove-9', p_44_18, p_44_30)
        self.add_bezier('glove-10', p_44_30, (p_44_35, p_40_36, p_38_40))
        self.add_line('glove-11', p_38_40, p_18_40)
        self.add_bezier('glove-12', p_18_40, (p_14_36, p_12_32, p_12_28))
        self.add_contour('glove', 'glove-1', 'glove-2', 'glove-3', 'glove-4', 'glove-5', 'glove-6', 'glove-7', 'glove-8', 'glove-9', 'glove-10', 'glove-11', 'glove-12', closed=True)
        self.add_line('thumb-1', p_4_24, p_12_28)
        self.add_contour('thumb', 'thumb-1', closed=False)
        self.relate("connect", 'thumb', 'glove')
        self.add_line('finger20-1', p_20_16, p_20_26)
        self.add_contour('finger20', 'finger20-1', closed=False)
        self.relate("connect", 'glove', 'finger20')
        self.add_line('finger28-1', p_28_14, p_28_26)
        self.add_contour('finger28', 'finger28-1', closed=False)
        self.relate("connect", 'glove', 'finger28')
        self.add_line('finger36-1', p_36_18, p_36_26)
        self.add_contour('finger36', 'finger36-1', closed=False)
        self.relate("connect", 'glove', 'finger36')
