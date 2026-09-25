'Bud branch in pitcher.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4fcea44-2a5f-481c-8527-6f48d16dfe84'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-05/vase plant_c4fcea44-2a5f-481c-8527-6f48d16dfe84.svg'
AUTHOR = 'gpt-6'

class BudBranchInPitcher(Solo48):
    icon_id = 'bud-branch-in-pitcher'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('bud', 'branch', 'in', 'pitcher')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_22_26 = (22, 26)
        p_31_26 = (31, 26)
        p_31_44 = (31, 44)
        p_11_44 = (11, 44)
        p_12_31 = (12, 31)
        p_10_26 = (10, 26)
        p_22_12 = (22, 12)
        p_8_14 = (8, 14)
        p_22_22 = (22, 22)
        p_36_14 = (36, 14)
        p_31_28 = (31, 28)
        p_31_40 = (31, 40)
        p_18_8 = (18, 8)
        p_26_8 = (26, 8)
        self.add_line('pitcher-1', p_22_26, p_31_26)
        self.add_line('pitcher-2', p_31_26, p_31_44)
        self.add_line('pitcher-3', p_31_44, p_11_44)
        self.add_line('pitcher-4', p_11_44, p_12_31)
        self.add_line('pitcher-5', p_12_31, p_10_26)
        self.add_line('pitcher-6', p_10_26, p_22_26)
        self.add_line('stem', p_22_26, p_22_12)
        self.add_line('twig-1', p_8_14, p_22_22)
        self.add_line('twig-2', p_22_22, p_36_14)
        self.add_arc('handle', p_31_28, p_31_40, radius_x=9, radius_y=6, sweep=True, large_arc=False)
        self.add_line('left', p_8_14, p_8_14)
        self.add_line('right', p_36_14, p_36_14)
        self.add_arc('top-top', p_18_8, p_26_8, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('top-bottom', p_26_8, p_18_8, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('pitcher', 'pitcher-1', 'pitcher-2', 'pitcher-3', 'pitcher-4', 'pitcher-5', 'pitcher-6', closed=False)
        self.add_contour('twig', 'twig-1', 'twig-2', closed=False)
        self.add_contour('top', 'top-top', 'top-bottom', closed=True)
        self.relate('connect', 'stem', 'pitcher')
        self.relate('connect', 'twig', 'stem')
        self.relate('connect', 'handle', 'pitcher')
        self.relate('connect', 'left', 'twig')
        self.relate('connect', 'right', 'twig')
        self.relate('connect', 'top', 'stem')
