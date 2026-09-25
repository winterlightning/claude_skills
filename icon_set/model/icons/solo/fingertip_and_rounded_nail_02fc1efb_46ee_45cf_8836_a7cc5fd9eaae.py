'Manicured Fingernail Symbol.\n\nSymbol plan: Rounded finger tip with inset nail and open cropped base.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02fc1efb-46ee-45cf-8836-a7cc5fd9eaae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fingernail_02fc1efb-46ee-45cf-8836-a7cc5fd9eaae.svg'
AUTHOR = 'gpt-6'

class FingertipAndRoundedNail(Solo48):
    icon_id = 'fingertip-and-rounded-nail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('fingertip', 'and', 'rounded', 'nail')

    def build(self):
        # Rounded finger tip with inset nail and open cropped base.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_44 = (8, 44)
        p_17_21 = (17, 21)
        p_17_27 = (17, 27)
        p_23_15 = (23, 15)
        p_23_33 = (23, 33)
        p_25_15 = (2 * axis_x - p_23_15[0], p_23_15[1])
        p_25_33 = (2 * axis_x - p_23_33[0], p_23_33[1])
        p_31_21 = (2 * axis_x - p_17_21[0], p_17_21[1])
        p_31_27 = (2 * axis_x - p_17_27[0], p_17_27[1])
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_line('finger-1', p_8_44, p_8_20)
        self.add_arc('finger-2', p_8_20, p_40_20, radius_x=16, radius_y=16, sweep=True)
        self.add_line('finger-3', p_40_20, p_40_44)
        self.add_contour('finger', 'finger-1', 'finger-2', 'finger-3', closed=False)
        self.add_line('nail-1', p_23_15, p_25_15)
        self.add_arc('nail-2', p_25_15, p_31_21, radius_x=6, radius_y=6, sweep=True)
        self.add_line('nail-3', p_31_21, p_31_27)
        self.add_arc('nail-4', p_31_27, p_25_33, radius_x=6, radius_y=6, sweep=True)
        self.add_line('nail-5', p_25_33, p_23_33)
        self.add_arc('nail-6', p_23_33, p_17_27, radius_x=6, radius_y=6, sweep=True)
        self.add_line('nail-7', p_17_27, p_17_21)
        self.add_arc('nail-8', p_17_21, p_23_15, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('nail', 'nail-1', 'nail-2', 'nail-3', 'nail-4', 'nail-5', 'nail-6', 'nail-7', 'nail-8', closed=True)
