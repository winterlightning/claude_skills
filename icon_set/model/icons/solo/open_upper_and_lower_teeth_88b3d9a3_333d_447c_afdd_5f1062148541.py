'Human Jaw and Teeth.\n\nSymbol plan: Four rounded teeth on each separated jaw; repeat equal-width tooth arcs and retain broad gum roofs.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88b3d9a3-333d-447c-afdd-5f1062148541'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jaw_88b3d9a3-333d-447c-afdd-5f1062148541.svg'
AUTHOR = 'gpt-6'

class OpenUpperAndLowerTeeth(Solo48):
    icon_id = 'open-upper-and-lower-teeth'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'upper', 'and', 'lower', 'teeth')

    def build(self):
        # Four rounded teeth on each separated jaw; repeat equal-width tooth arcs and retain broad gum roofs.
        axis_x = 24
        p_4_12 = (4, 12)
        p_4_15 = (4, 15)
        p_4_33 = (4, 33)
        p_4_36 = (4, 36)
        p_8_8 = (8, 8)
        p_8_40 = (8, 40)
        p_14_8 = (14, 8)
        p_14_15 = (14, 15)
        p_14_33 = (14, 33)
        p_14_40 = (14, 40)
        p_24_8 = (24, 8)
        p_24_15 = (24, 15)
        p_24_33 = (24, 33)
        p_24_40 = (24, 40)
        p_34_8 = (2 * axis_x - p_14_8[0], p_14_8[1])
        p_34_15 = (2 * axis_x - p_14_15[0], p_14_15[1])
        p_34_33 = (2 * axis_x - p_14_33[0], p_14_33[1])
        p_34_40 = (2 * axis_x - p_14_40[0], p_14_40[1])
        p_40_8 = (2 * axis_x - p_8_8[0], p_8_8[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        p_44_12 = (2 * axis_x - p_4_12[0], p_4_12[1])
        p_44_15 = (2 * axis_x - p_4_15[0], p_4_15[1])
        p_44_33 = (2 * axis_x - p_4_33[0], p_4_33[1])
        p_44_36 = (2 * axis_x - p_4_36[0], p_4_36[1])
        self.add_arc('upper-1', p_4_12, p_8_8, radius_x=4, radius_y=4, sweep=True)
        self.add_line('upper-2', p_8_8, p_40_8)
        self.add_arc('upper-3', p_40_8, p_44_12, radius_x=4, radius_y=4, sweep=True)
        self.add_line('upper-4', p_44_12, p_44_15)
        self.add_arc('upper-5', p_44_15, p_34_15, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('upper-6', p_34_15, p_24_15, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('upper-7', p_24_15, p_14_15, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('upper-8', p_14_15, p_4_15, radius_x=5, radius_y=5, sweep=True)
        self.add_line('upper-9', p_4_15, p_4_12)
        self.add_contour('upper', 'upper-1', 'upper-2', 'upper-3', 'upper-4', 'upper-5', 'upper-6', 'upper-7', 'upper-8', 'upper-9', closed=True)
        self.add_line('upper-divider-14-1', p_14_8, p_14_15)
        self.add_contour('upper-divider-14', 'upper-divider-14-1', closed=False)
        self.relate("connect", 'upper', 'upper-divider-14')
        self.add_line('upper-divider-24-1', p_24_8, p_24_15)
        self.add_contour('upper-divider-24', 'upper-divider-24-1', closed=False)
        self.relate("connect", 'upper', 'upper-divider-24')
        self.add_line('upper-divider-34-1', p_34_8, p_34_15)
        self.add_contour('upper-divider-34', 'upper-divider-34-1', closed=False)
        self.relate("connect", 'upper', 'upper-divider-34')
        self.add_arc('lower-1', p_4_36, p_8_40, radius_x=4, radius_y=4, sweep=False)
        self.add_line('lower-2', p_8_40, p_40_40)
        self.add_arc('lower-3', p_40_40, p_44_36, radius_x=4, radius_y=4, sweep=False)
        self.add_line('lower-4', p_44_36, p_44_33)
        self.add_arc('lower-5', p_44_33, p_34_33, radius_x=5, radius_y=5, sweep=False)
        self.add_arc('lower-6', p_34_33, p_24_33, radius_x=5, radius_y=5, sweep=False)
        self.add_arc('lower-7', p_24_33, p_14_33, radius_x=5, radius_y=5, sweep=False)
        self.add_arc('lower-8', p_14_33, p_4_33, radius_x=5, radius_y=5, sweep=False)
        self.add_line('lower-9', p_4_33, p_4_36)
        self.add_contour('lower', 'lower-1', 'lower-2', 'lower-3', 'lower-4', 'lower-5', 'lower-6', 'lower-7', 'lower-8', 'lower-9', closed=True)
        self.add_line('lower-divider-14-1', p_14_40, p_14_33)
        self.add_contour('lower-divider-14', 'lower-divider-14-1', closed=False)
        self.relate("connect", 'lower', 'lower-divider-14')
        self.add_line('lower-divider-24-1', p_24_40, p_24_33)
        self.add_contour('lower-divider-24', 'lower-divider-24-1', closed=False)
        self.relate("connect", 'lower', 'lower-divider-24')
        self.add_line('lower-divider-34-1', p_34_40, p_34_33)
        self.add_contour('lower-divider-34', 'lower-divider-34-1', closed=False)
        self.relate("connect", 'lower', 'lower-divider-34')
