'Mathematical Calculator.\n\nSymbol plan: Calculator with blank display and four structural keys. Operation marks removed at native scale; controls remain intrinsic, not text.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: calculator.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76f13b31-0b08-4c82-8daa-711a44b46d08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/accounting calculator 1_76f13b31-0b08-4c82-8daa-711a44b46d08.svg'
AUTHOR = 'gpt-6'

class CalculatorFourOperationKeys(Solo48):
    icon_id = 'calculator-four-operation-keys'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('calculator', 'four', 'operation', 'keys')

    def build(self):
        # Calculator with blank display and four structural keys. Operation marks removed at native scale; controls remain intrinsic, not text.
        axis_x = 24
        p_8_9 = (8, 9)
        p_8_39 = (8, 39)
        p_13_4 = (13, 4)
        p_13_44 = (13, 44)
        p_18_15 = (18, 15)
        p_18_27 = (18, 27)
        p_18_35 = (18, 35)
        p_30_15 = (2 * axis_x - p_18_15[0], p_18_15[1])
        p_30_27 = (2 * axis_x - p_18_27[0], p_18_27[1])
        p_30_35 = (2 * axis_x - p_18_35[0], p_18_35[1])
        p_35_4 = (2 * axis_x - p_13_4[0], p_13_4[1])
        p_35_44 = (2 * axis_x - p_13_44[0], p_13_44[1])
        p_40_9 = (2 * axis_x - p_8_9[0], p_8_9[1])
        p_40_39 = (2 * axis_x - p_8_39[0], p_8_39[1])
        self.add_line('case-1', p_13_4, p_35_4)
        self.add_arc('case-2', p_35_4, p_40_9, radius_x=5, radius_y=5, sweep=True)
        self.add_line('case-3', p_40_9, p_40_39)
        self.add_arc('case-4', p_40_39, p_35_44, radius_x=5, radius_y=5, sweep=True)
        self.add_line('case-5', p_35_44, p_13_44)
        self.add_arc('case-6', p_13_44, p_8_39, radius_x=5, radius_y=5, sweep=True)
        self.add_line('case-7', p_8_39, p_8_9)
        self.add_arc('case-8', p_8_9, p_13_4, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('case', 'case-1', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', 'case-8', closed=True)
        self.add_line('display-1', p_18_15, p_30_15)
        self.add_contour('display', 'display-1', closed=False)
        self.add_line('key-18-27-1', p_18_27, p_18_27)
        self.add_contour('key-18-27', 'key-18-27-1', closed=False)
        self.add_line('key-18-36-1', p_18_35, p_18_35)
        self.add_contour('key-18-36', 'key-18-36-1', closed=False)
        self.add_line('key-30-27-1', p_30_27, p_30_27)
        self.add_contour('key-30-27', 'key-30-27-1', closed=False)
        self.add_line('key-30-36-1', p_30_35, p_30_35)
        self.add_contour('key-30-36', 'key-30-36-1', closed=False)
