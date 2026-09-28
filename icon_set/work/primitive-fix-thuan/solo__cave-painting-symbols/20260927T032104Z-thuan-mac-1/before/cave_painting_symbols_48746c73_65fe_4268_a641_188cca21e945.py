'Cave painting symbols.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48746c73-65fe-4268-a641-188cca21e945'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/caveman symbols_48746c73-65fe-4268-a641-188cca21e945.svg'
AUTHOR = 'gpt-6'

class CavePaintingSymbols(Solo48):
    icon_id = 'cave-painting-symbols'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('cave painting', 'petroglyph', 'rune', 'prehistoric', 'symbols', 'marks', 'ancient', 'rock art')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_6_14 = (6, 14)
        p_6_24 = (6, 24)
        p_6_35 = (6, 35)
        p_14_6 = (14, 6)
        p_6_26 = (6, 26)
        p_14_18 = (14, 18)
        p_29_17 = (29, 17)
        p_29_9 = (29, 9)
        p_32_6 = (32, 6)
        p_42_14 = (42, 14)
        p_42_24 = (42, 24)
        p_22_22 = (22, 22)
        p_31_31 = (31, 31)
        p_22_39 = (22, 39)
        p_14_31 = (14, 31)
        p_19_42 = (19, 42)
        p_26_42 = (26, 42)
        self.add_line('staff-1', p_6_6, p_6_14)
        self.add_line('staff-2', p_6_14, p_6_24)
        self.add_line('staff-3', p_6_24, p_6_35)
        self.add_line('branch-upper', p_6_14, p_14_6)
        self.add_line('branch-lower', p_6_26, p_14_18)
        self.add_line('arch-1', p_29_17, p_29_9)
        self.add_line('arch-2', p_29_9, p_32_6)
        self.add_line('arch-3', p_32_6, p_42_14)
        self.add_line('arch-4', p_42_14, p_42_24)
        self.add_line('diamond-1', p_22_22, p_31_31)
        self.add_line('diamond-2', p_31_31, p_22_39)
        self.add_line('diamond-3', p_22_39, p_14_31)
        self.add_line('diamond-4', p_14_31, p_22_22)
        self.add_line('diamond-5', p_22_22, p_22_22)
        self.add_line('tail-left', p_22_39, p_19_42)
        self.add_line('tail-right', p_22_39, p_26_42)
        self.add_contour('staff', 'staff-1', 'staff-2', 'staff-3', closed=False)
        self.add_contour('arch', 'arch-1', 'arch-2', 'arch-3', 'arch-4', closed=False)
        self.add_contour('diamond', 'diamond-1', 'diamond-2', 'diamond-3', 'diamond-4', 'diamond-5', closed=True)
        self.relate('connect', 'staff', 'branch-upper')
        self.relate('connect', 'staff', 'branch-lower')
        self.relate('connect', 'diamond', 'tail-left')
        self.relate('connect', 'diamond', 'tail-right')
        self.relate('connect', 'tail-left', 'tail-right')
