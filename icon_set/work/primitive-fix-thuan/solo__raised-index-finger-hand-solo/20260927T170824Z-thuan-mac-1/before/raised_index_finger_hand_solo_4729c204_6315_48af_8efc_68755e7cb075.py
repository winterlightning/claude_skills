'Index Finger Pointing Up.\n\nSymbol plan: Raised index finger, folded-finger knuckle ridge and broad palm with thumb; simplify three narrow knuckle slits.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4729c204-6315-48af-8efc-68755e7cb075'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/finger_4729c204-6315-48af-8efc-68755e7cb075.svg'
AUTHOR = 'gpt-6'

class RaisedIndexFingerHandSolo(Solo48):
    icon_id = 'raised-index-finger-hand-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('raised', 'index', 'finger', 'hand', 'solo')

    def build(self):
        # Raised index finger, folded-finger knuckle ridge and broad palm with thumb; simplify three narrow knuckle slits.
        axis_x = 24
        p_8_21 = (8, 21)
        p_8_26 = (8, 26)
        p_8_28 = (8, 28)
        p_10_31 = (10, 31)
        p_13_20 = (13, 20)
        p_15_37 = (15, 37)
        p_18_9 = (18, 9)
        p_18_26 = (18, 26)
        p_18_44 = (18, 44)
        p_27_44 = (27, 44)
        p_28_9 = (28, 9)
        p_28_20 = (28, 20)
        p_33_16 = (33, 16)
        p_35_44 = (35, 44)
        p_40_20 = (40, 20)
        p_40_26 = (2 * axis_x - p_8_26[0], p_8_26[1])
        p_40_31 = (40, 31)
        p_40_40 = (40, 40)
        self.add_line('hand-1', p_18_26, p_18_9)
        self.add_arc('hand-2', p_18_9, p_28_9, radius_x=5, radius_y=5, sweep=True)
        self.add_line('hand-3', p_28_9, p_28_20)
        self.add_bezier('hand-4', p_28_20, (p_33_16, p_40_20, p_40_26))
        self.add_line('hand-5', p_40_26, p_40_31)
        self.add_bezier('hand-6', p_40_31, (p_40_40, p_35_44, p_27_44))
        self.add_bezier('hand-7', p_27_44, (p_18_44, p_15_37, p_10_31))
        self.add_bezier('hand-8', p_10_31, (p_8_28, p_8_28, p_8_26))
        self.add_bezier('hand-9', p_8_26, (p_8_21, p_13_20, p_18_26))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', 'hand-5', 'hand-6', 'hand-7', 'hand-8', 'hand-9', closed=True)
