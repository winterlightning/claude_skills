'Outdoor Barbecue Kettle Grill.\n\nSymbol plan: Open kettle grill with two splayed legs and one right wheel; remove crowded crossbar.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa61a116-e849-4e8f-b1cd-ea66cd4723ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grill_fa61a116-e849-4e8f-b1cd-ea66cd4723ca.svg'
AUTHOR = 'gpt-6'

class KettleGrillWithOneWheel(Solo48):
    icon_id = 'kettle-grill-with-one-wheel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('kettle', 'grill', 'with', 'one', 'wheel')

    def build(self):
        # Open kettle grill with two splayed legs and one right wheel; remove crowded crossbar.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_19 = (4, 19)
        p_8_40 = (8, 40)
        p_12_23 = (12, 23)
        p_15_22 = (15, 22)
        p_24_23 = (24, 23)
        p_33_22 = (2 * axis_x - p_15_22[0], p_15_22[1])
        p_33_35 = (33, 35)
        p_36_23 = (2 * axis_x - p_12_23[0], p_12_23[1])
        p_38_30 = (38, 30)
        p_43_35 = (43, 35)
        p_44_8 = (2 * axis_x - p_4_8[0], p_4_8[1])
        p_44_19 = (2 * axis_x - p_4_19[0], p_4_19[1])
        self.add_line('bowl-1', p_4_8, p_44_8)
        self.add_bezier('bowl-2', p_44_8, (p_44_19, p_36_23, p_24_23))
        self.add_bezier('bowl-3', p_24_23, (p_12_23, p_4_19, p_4_8))
        self.add_contour('bowl', 'bowl-1', 'bowl-2', 'bowl-3', closed=True)
        self.add_line('left-leg-1', p_15_22, p_8_40)
        self.add_contour('left-leg', 'left-leg-1', closed=False)
        self.relate("connect", 'bowl', 'left-leg')
        self.add_line('right-leg-1', p_33_22, p_38_30)
        self.add_contour('right-leg', 'right-leg-1', closed=False)
        self.relate("connect", 'bowl', 'right-leg')
        self.add_arc('wheel-1', p_33_35, p_43_35, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('wheel-2', p_43_35, p_33_35, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('wheel', 'wheel-1', 'wheel-2', closed=True)
        self.relate("connect", 'wheel', 'right-leg')
