'Human Eye with Upper Eyelid.\n\nSymbol plan: Raised upper lid above eye and circular iris; pupil omitted to keep clear center.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: eye.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b04007f0-05be-4f53-84a5-58871bbb4d01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eyelids_b04007f0-05be-4f53-84a5-58871bbb4d01.svg'
AUTHOR = 'gpt-6'

class EyeBeneathBroadUpperLid(Solo48):
    icon_id = 'eye-beneath-broad-upper-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('eye', 'beneath', 'broad', 'upper', 'lid')

    def build(self):
        # Raised upper lid above eye and circular iris; pupil omitted to keep clear center.
        axis_x = 24
        p_4_17 = (4, 17)
        p_4_29 = (4, 29)
        p_11_11 = (11, 11)
        p_12_23 = (12, 23)
        p_12_36 = (12, 36)
        p_16_8 = (16, 8)
        p_16_18 = (16, 18)
        p_16_40 = (16, 40)
        p_22_29 = (22, 29)
        p_24_8 = (24, 8)
        p_24_18 = (24, 18)
        p_24_40 = (24, 40)
        p_26_29 = (2 * axis_x - p_22_29[0], p_22_29[1])
        p_32_8 = (2 * axis_x - p_16_8[0], p_16_8[1])
        p_32_18 = (2 * axis_x - p_16_18[0], p_16_18[1])
        p_32_40 = (2 * axis_x - p_16_40[0], p_16_40[1])
        p_36_23 = (2 * axis_x - p_12_23[0], p_12_23[1])
        p_36_36 = (2 * axis_x - p_12_36[0], p_12_36[1])
        p_37_11 = (2 * axis_x - p_11_11[0], p_11_11[1])
        p_44_17 = (2 * axis_x - p_4_17[0], p_4_17[1])
        p_44_29 = (2 * axis_x - p_4_29[0], p_4_29[1])
        self.add_bezier('upper-lid-1', p_4_17, (p_11_11, p_16_8, p_24_8))
        self.add_bezier('upper-lid-2', p_24_8, (p_32_8, p_37_11, p_44_17))
        self.add_contour('upper-lid', 'upper-lid-1', 'upper-lid-2', closed=False)
        self.add_bezier('eye-1', p_4_29, (p_12_23, p_16_18, p_24_18))
        self.add_bezier('eye-2', p_24_18, (p_32_18, p_36_23, p_44_29))
        self.add_bezier('eye-3', p_44_29, (p_36_36, p_32_40, p_24_40))
        self.add_bezier('eye-4', p_24_40, (p_16_40, p_12_36, p_4_29))
        self.add_contour('eye', 'eye-1', 'eye-2', 'eye-3', 'eye-4', closed=True)
        self.add_arc('iris-1', p_22_29, p_26_29, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('iris-2', p_26_29, p_22_29, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('iris', 'iris-1', 'iris-2', closed=True)
