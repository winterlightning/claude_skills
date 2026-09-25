'Laboratory Test Tube.\n\nSymbol plan: Wide cap above a narrow round-bottom tube. Lucide test-tube informs open body construction.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: test-tube.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e371924-0a22-4a3c-ad1d-365fa1f247c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/holder_4e371924-0a22-4a3c-ad1d-365fa1f247c0.svg'
AUTHOR = 'gpt-6'

class RoundedTubeWithWideCap(Solo48):
    icon_id = 'rounded-tube-with-wide-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rounded', 'tube', 'with', 'wide', 'cap')

    def build(self):
        # Wide cap above a narrow round-bottom tube. Lucide test-tube informs open body construction.
        axis_x = 24
        p_8_6 = (8, 6)
        p_8_12 = (8, 12)
        p_10_4 = (10, 4)
        p_10_14 = (10, 14)
        p_16_14 = (16, 14)
        p_16_36 = (16, 36)
        p_32_14 = (2 * axis_x - p_16_14[0], p_16_14[1])
        p_32_36 = (2 * axis_x - p_16_36[0], p_16_36[1])
        p_38_4 = (2 * axis_x - p_10_4[0], p_10_4[1])
        p_38_14 = (2 * axis_x - p_10_14[0], p_10_14[1])
        p_40_6 = (2 * axis_x - p_8_6[0], p_8_6[1])
        p_40_12 = (2 * axis_x - p_8_12[0], p_8_12[1])
        self.add_line('cap-1', p_10_4, p_38_4)
        self.add_arc('cap-2', p_38_4, p_40_6, radius_x=2, radius_y=2, sweep=True)
        self.add_line('cap-3', p_40_6, p_40_12)
        self.add_arc('cap-4', p_40_12, p_38_14, radius_x=2, radius_y=2, sweep=True)
        self.add_line('cap-5', p_38_14, p_10_14)
        self.add_arc('cap-6', p_10_14, p_8_12, radius_x=2, radius_y=2, sweep=True)
        self.add_line('cap-7', p_8_12, p_8_6)
        self.add_arc('cap-8', p_8_6, p_10_4, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('cap', 'cap-1', 'cap-2', 'cap-3', 'cap-4', 'cap-5', 'cap-6', 'cap-7', 'cap-8', closed=True)
        self.add_line('tube-1', p_16_14, p_16_36)
        self.add_arc('tube-2', p_16_36, p_32_36, radius_x=8, radius_y=8, sweep=False)
        self.add_line('tube-3', p_32_36, p_32_14)
        self.add_contour('tube', 'tube-1', 'tube-2', 'tube-3', closed=False)
        self.relate("connect", 'tube', 'cap')
