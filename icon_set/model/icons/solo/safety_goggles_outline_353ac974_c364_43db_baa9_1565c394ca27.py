'Protective Eyewear Safety Goggles.\n\nSymbol plan: Single broad protective goggle lens with a rounded nose notch. Symmetric outline without unnecessary double rims.\nKeyshape: HRECT_M; authored on SOLO48, not scaled from source.\nLucide: glasses.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '353ac974-c364-43db-baa9-1565c394ca27'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/goggles_353ac974-c364-43db-baa9-1565c394ca27.svg'
AUTHOR = 'gpt-6'

class SafetyGogglesOutline(Solo48):
    icon_id = 'safety-goggles-outline'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('safety', 'goggles', 'outline')

    def build(self):
        # Single broad protective goggle lens with a rounded nose notch. Symmetric outline without unnecessary double rims.
        axis_x = 24
        p_4_15 = (4, 15)
        p_4_22 = (4, 22)
        p_4_32 = (4, 32)
        p_7_10 = (7, 10)
        p_9_38 = (9, 38)
        p_14_10 = (14, 10)
        p_15_38 = (15, 38)
        p_20_27 = (20, 27)
        p_21_38 = (21, 38)
        p_24_27 = (24, 27)
        p_27_38 = (2 * axis_x - p_21_38[0], p_21_38[1])
        p_28_27 = (2 * axis_x - p_20_27[0], p_20_27[1])
        p_33_38 = (2 * axis_x - p_15_38[0], p_15_38[1])
        p_34_10 = (2 * axis_x - p_14_10[0], p_14_10[1])
        p_39_38 = (2 * axis_x - p_9_38[0], p_9_38[1])
        p_41_10 = (2 * axis_x - p_7_10[0], p_7_10[1])
        p_44_15 = (2 * axis_x - p_4_15[0], p_4_15[1])
        p_44_22 = (2 * axis_x - p_4_22[0], p_4_22[1])
        p_44_32 = (2 * axis_x - p_4_32[0], p_4_32[1])
        self.add_line('goggles-1', p_14_10, p_34_10)
        self.add_bezier('goggles-2', p_34_10, (p_41_10, p_44_15, p_44_22))
        self.add_bezier('goggles-3', p_44_22, (p_44_32, p_39_38, p_33_38))
        self.add_bezier('goggles-4', p_33_38, (p_27_38, p_28_27, p_24_27))
        self.add_bezier('goggles-5', p_24_27, (p_20_27, p_21_38, p_15_38))
        self.add_bezier('goggles-6', p_15_38, (p_9_38, p_4_32, p_4_22))
        self.add_bezier('goggles-7', p_4_22, (p_4_15, p_7_10, p_14_10))
        self.add_contour('goggles', 'goggles-1', 'goggles-2', 'goggles-3', 'goggles-4', 'goggles-5', 'goggles-6', 'goggles-7', closed=True)
