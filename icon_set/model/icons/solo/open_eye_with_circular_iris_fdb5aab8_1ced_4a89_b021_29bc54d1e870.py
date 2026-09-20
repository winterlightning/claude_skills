'Human Eye View Icon.\n\nSymbol plan: Symmetric almond eyelids and circular iris; omit small pupil for required nested clearance.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: eye.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdb5aab8-1ced-4a89-b021-29bc54d1e870'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eyeball_fdb5aab8-1ced-4a89-b021-29bc54d1e870.svg'
AUTHOR = 'gpt-6'

class OpenEyeWithCircularIris(Solo48):
    icon_id = 'open-eye-with-circular-iris'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('open', 'eye', 'with', 'circular', 'iris')

    def build(self):
        # Symmetric almond eyelids and circular iris; omit small pupil for required nested clearance.
        axis_x = 24
        p_4_24 = (4, 24)
        p_10_15 = (10, 15)
        p_10_33 = (10, 33)
        p_15_8 = (15, 8)
        p_15_40 = (15, 40)
        p_17_24 = (17, 24)
        p_24_8 = (24, 8)
        p_24_40 = (24, 40)
        p_31_24 = (2 * axis_x - p_17_24[0], p_17_24[1])
        p_33_8 = (2 * axis_x - p_15_8[0], p_15_8[1])
        p_33_40 = (2 * axis_x - p_15_40[0], p_15_40[1])
        p_38_15 = (2 * axis_x - p_10_15[0], p_10_15[1])
        p_38_33 = (2 * axis_x - p_10_33[0], p_10_33[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_bezier('eye-1', p_4_24, (p_10_15, p_15_8, p_24_8))
        self.add_bezier('eye-2', p_24_8, (p_33_8, p_38_15, p_44_24))
        self.add_bezier('eye-3', p_44_24, (p_38_33, p_33_40, p_24_40))
        self.add_bezier('eye-4', p_24_40, (p_15_40, p_10_33, p_4_24))
        self.add_contour('eye', 'eye-1', 'eye-2', 'eye-3', 'eye-4', closed=True)
        self.add_arc('iris-1', p_17_24, p_31_24, radius_x=7, radius_y=7, sweep=True)
        self.add_arc('iris-2', p_31_24, p_17_24, radius_x=7, radius_y=7, sweep=True)
        self.add_contour('iris', 'iris-1', 'iris-2', closed=True)
