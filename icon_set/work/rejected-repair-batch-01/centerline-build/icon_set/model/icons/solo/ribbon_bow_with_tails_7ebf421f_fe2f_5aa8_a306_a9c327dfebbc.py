'Ribbon bow with tails.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ebf421f-fe2f-5aa8-a306-a9c327dfebbc'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/accessories ribbon tie_7ebf421f-fe2f-5aa8-a306-a9c327dfebbc.svg'
AUTHOR = 'gpt-6'

class RibbonBowWithTails(Solo48):
    icon_id = 'ribbon-bow-with-tails'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('ribbon', 'bow', 'gift', 'decoration', 'tie', 'accessory', 'present', 'wrapping')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_14 = (24, 14)
        p_11_6 = (11, 6)
        p_6_11 = (6, 11)
        p_6_21 = (6, 21)
        p_9_24 = (9, 24)
        p_15_23 = (15, 23)
        p_24_21 = (24, 21)
        p_37_6 = (37, 6)
        p_42_11 = (42, 11)
        p_42_21 = (42, 21)
        p_39_24 = (39, 24)
        p_33_23 = (33, 23)
        p_6_36 = (6, 36)
        p_18_42 = (18, 42)
        p_42_36 = (42, 36)
        p_30_42 = (30, 42)
        self.add_line('left-top', p_24_14, p_11_6)
        self.add_arc('left-upper', p_11_6, p_6_11, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('left-side', p_6_11, p_6_21)
        self.add_arc('left-lower', p_6_21, p_9_24, radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('left-return-1', p_9_24, p_15_23)
        self.add_line('left-return-2', p_15_23, p_24_21)
        self.add_line('knot', p_24_21, p_24_14)
        self.add_line('right-top', p_24_14, p_37_6)
        self.add_arc('right-upper', p_37_6, p_42_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('right-side', p_42_11, p_42_21)
        self.add_arc('right-lower', p_42_21, p_39_24, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('right-return-1', p_39_24, p_33_23)
        self.add_line('right-return-2', p_33_23, p_24_21)
        self.add_line('tail-left-1', p_15_23, p_6_36)
        self.add_line('tail-left-2', p_6_36, p_18_42)
        self.add_line('tail-left-3', p_18_42, p_24_21)
        self.add_line('tail-right-1', p_33_23, p_42_36)
        self.add_line('tail-right-2', p_42_36, p_30_42)
        self.add_line('tail-right-3', p_30_42, p_24_21)
        self.add_contour('left-loop', 'left-top', 'left-upper', 'left-side', 'left-lower', 'left-return-1', 'left-return-2', 'knot', closed=True)
        self.add_contour('right-loop', 'right-top', 'right-upper', 'right-side', 'right-lower', 'right-return-1', 'right-return-2', closed=False)
        self.add_contour('tail-left', 'tail-left-1', 'tail-left-2', 'tail-left-3', closed=False)
        self.add_contour('tail-right', 'tail-right-1', 'tail-right-2', 'tail-right-3', closed=False)
        self.relate('connect', 'left-loop', 'right-loop')
        self.relate('connect', 'left-loop', 'tail-left')
        self.relate('connect', 'right-loop', 'tail-right')
        self.relate('connect', 'left-loop', 'tail-right')
        self.relate('connect', 'right-loop', 'tail-left')
        self.relate('connect', 'tail-left', 'tail-right')
