'Professional Travel Suitcase.\n\nSymbol plan: Travel suitcase with centered handle and plain seam; the actual reference has no distinct latch.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: briefcase-business.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c25c3740-a2a0-493f-b5d6-8c6d5d57045b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tourism_c25c3740-a2a0-493f-b5d6-8c6d5d57045b.svg'
AUTHOR = 'gpt-6'

class TravelSuitcase(Solo48):
    icon_id = 'travel-suitcase'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('travel', 'suitcase')

    def build(self):
        # Travel suitcase with centered handle and plain seam; the actual reference has no distinct latch.
        axis_x = 24
        p_4_20 = (4, 20)
        p_4_28 = (4, 28)
        p_4_36 = (4, 36)
        p_8_16 = (8, 16)
        p_8_40 = (8, 40)
        p_16_8 = (16, 8)
        p_16_16 = (16, 16)
        p_32_8 = (2 * axis_x - p_16_8[0], p_16_8[1])
        p_32_16 = (2 * axis_x - p_16_16[0], p_16_16[1])
        p_40_16 = (2 * axis_x - p_8_16[0], p_8_16[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        p_44_20 = (2 * axis_x - p_4_20[0], p_4_20[1])
        p_44_28 = (2 * axis_x - p_4_28[0], p_4_28[1])
        p_44_36 = (2 * axis_x - p_4_36[0], p_4_36[1])
        self.add_line('case-1', p_16_16, p_32_16)
        self.add_line('case-2', p_32_16, p_40_16)
        self.add_arc('case-3', p_40_16, p_44_20, radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-4', p_44_20, p_44_28)
        self.add_line('case-5', p_44_28, p_44_36)
        self.add_arc('case-6', p_44_36, p_40_40, radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-7', p_40_40, p_8_40)
        self.add_arc('case-8', p_8_40, p_4_36, radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-9', p_4_36, p_4_28)
        self.add_line('case-10', p_4_28, p_4_20)
        self.add_arc('case-11', p_4_20, p_8_16, radius_x=4, radius_y=4, sweep=True)
        self.add_line('case-12', p_8_16, p_16_16)
        self.add_contour('case', 'case-1', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', 'case-8', 'case-9', 'case-10', 'case-11', 'case-12', closed=True)
        self.add_line('handle-1', p_16_16, p_16_8)
        self.add_line('handle-2', p_16_8, p_32_8)
        self.add_line('handle-3', p_32_8, p_32_16)
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', closed=False)
        self.relate("connect", 'handle', 'case')
        self.add_line('seam-1', p_4_28, p_44_28)
        self.add_contour('seam', 'seam-1', closed=False)
        self.relate("connect", 'seam', 'case')
