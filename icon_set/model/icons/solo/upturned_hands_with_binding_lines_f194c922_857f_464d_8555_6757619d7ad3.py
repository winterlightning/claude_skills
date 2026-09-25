'Human Hands Bound Together.\n\nSymbol plan: Mirrored raised hands above three binding strokes; retained as one restraint scene without inventing a knot. Reduce bindings to two lines so hands remain legible.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f194c922-857f-464d-8555-6757619d7ad3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hostage fasten_f194c922-857f-464d-8555-6757619d7ad3.svg'
AUTHOR = 'gpt-6'

class UpturnedHandsWithBindingLines(Solo48):
    icon_id = 'upturned-hands-with-binding-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upturned', 'hands', 'with', 'binding', 'lines')

    def build(self):
        # Mirrored raised hands above three binding strokes; retained as one restraint scene without inventing a knot. Reduce bindings to two lines so hands remain legible.
        axis_x = 24
        p_6_10 = (6, 10)
        p_6_16 = (6, 16)
        p_6_19 = (6, 19)
        p_8_22 = (8, 22)
        p_10_26 = (10, 26)
        p_10_34 = (10, 34)
        p_10_42 = (10, 42)
        p_14_10 = (14, 10)
        p_14_18 = (14, 18)
        p_17_16 = (17, 16)
        p_20_19 = (20, 19)
        p_20_23 = (20, 23)
        p_20_26 = (20, 26)
        p_28_19 = (2 * axis_x - p_20_19[0], p_20_19[1])
        p_28_23 = (2 * axis_x - p_20_23[0], p_20_23[1])
        p_28_26 = (2 * axis_x - p_20_26[0], p_20_26[1])
        p_31_16 = (2 * axis_x - p_17_16[0], p_17_16[1])
        p_34_10 = (2 * axis_x - p_14_10[0], p_14_10[1])
        p_34_18 = (2 * axis_x - p_14_18[0], p_14_18[1])
        p_38_26 = (2 * axis_x - p_10_26[0], p_10_26[1])
        p_38_34 = (2 * axis_x - p_10_34[0], p_10_34[1])
        p_38_42 = (2 * axis_x - p_10_42[0], p_10_42[1])
        p_40_22 = (2 * axis_x - p_8_22[0], p_8_22[1])
        p_42_10 = (2 * axis_x - p_6_10[0], p_6_10[1])
        p_42_16 = (2 * axis_x - p_6_16[0], p_6_16[1])
        p_42_19 = (2 * axis_x - p_6_19[0], p_6_19[1])
        self.add_bezier('left-hand-1', p_10_26, (p_8_22, p_6_19, p_6_16))
        self.add_line('left-hand-2', p_6_16, p_6_10)
        self.add_arc('left-hand-3', p_6_10, p_14_10, radius_x=4, radius_y=4, sweep=True)
        self.add_line('left-hand-4', p_14_10, p_14_18)
        self.add_bezier('left-hand-5', p_14_18, (p_17_16, p_20_19, p_20_23))
        self.add_line('left-hand-6', p_20_23, p_20_26)
        self.add_contour('left-hand', 'left-hand-1', 'left-hand-2', 'left-hand-3', 'left-hand-4', 'left-hand-5', 'left-hand-6', closed=False)
        self.add_bezier('right-hand-1', p_38_26, (p_40_22, p_42_19, p_42_16))
        self.add_line('right-hand-2', p_42_16, p_42_10)
        self.add_arc('right-hand-3', p_42_10, p_34_10, radius_x=4, radius_y=4, sweep=False)
        self.add_line('right-hand-4', p_34_10, p_34_18)
        self.add_bezier('right-hand-5', p_34_18, (p_31_16, p_28_19, p_28_23))
        self.add_line('right-hand-6', p_28_23, p_28_26)
        self.add_contour('right-hand', 'right-hand-1', 'right-hand-2', 'right-hand-3', 'right-hand-4', 'right-hand-5', 'right-hand-6', closed=False)
        self.add_line('binding-34-1', p_10_34, p_38_34)
        self.add_contour('binding-34', 'binding-34-1', closed=False)
        self.add_line('binding-42-1', p_10_42, p_38_42)
        self.add_contour('binding-42', 'binding-42-1', closed=False)
