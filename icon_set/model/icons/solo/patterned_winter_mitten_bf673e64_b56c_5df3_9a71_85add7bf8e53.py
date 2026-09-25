'Patterned winter mitten.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf673e64-b56c-5df3-9a71-85add7bf8e53'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/winter gloves_bf673e64-b56c-5df3-9a71-85add7bf8e53.svg'
AUTHOR = 'gpt-6'

class PatternedWinterMitten(Solo48):
    icon_id = 'patterned-winter-mitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('mitten', 'glove', 'winter', 'knit', 'pattern', 'zigzag', 'cold', 'clothing', 'snow')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_36 = (8, 36)
        p_8_24 = (8, 24)
        p_8_16 = (8, 16)
        p_30_16 = (30, 16)
        p_30_24 = (30, 24)
        p_34_20 = (34, 20)
        p_40_26 = (40, 26)
        p_40_27 = (40, 27)
        p_30_36 = (30, 36)
        p_8_44 = (8, 44)
        p_30_44 = (30, 44)
        p_14_20 = (14, 20)
        p_21_25 = (21, 25)
        p_27_21 = (27, 21)
        self.add_line('side-l', p_8_36, p_8_24)
        self.add_line('side-upper', p_8_24, p_8_16)
        self.add_arc('dome', p_8_16, p_30_16, radius_x=11, radius_y=12, sweep=True, large_arc=False)
        self.add_line('finger-side', p_30_16, p_30_24)
        self.add_line('thumb-root', p_30_24, p_34_20)
        self.add_arc('thumb-cap', p_34_20, p_40_26, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('thumb-side', p_40_26, p_40_27)
        self.add_line('palm', p_40_27, p_30_36)
        self.add_line('base', p_30_36, p_8_36)
        self.add_line('cuff-1', p_8_36, p_8_44)
        self.add_line('cuff-2', p_8_44, p_30_44)
        self.add_line('cuff-3', p_30_44, p_30_36)
        self.add_line('knit-1', p_8_24, p_14_20)
        self.add_line('knit-2', p_14_20, p_21_25)
        self.add_line('knit-3', p_21_25, p_27_21)
        self.add_line('knit-4', p_27_21, p_30_24)
        self.add_contour('mitten', 'side-l', 'side-upper', 'dome', 'finger-side', 'thumb-root', 'thumb-cap', 'thumb-side', 'palm', 'base', closed=True)
        self.add_contour('cuff', 'cuff-1', 'cuff-2', 'cuff-3', closed=False)
        self.add_contour('knit', 'knit-1', 'knit-2', 'knit-3', 'knit-4', closed=False)
        self.relate('connect', 'mitten', 'cuff')
        self.relate('connect', 'mitten', 'knit')
