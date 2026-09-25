'Smartwatch.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcd267cd-6f18-4751-b281-118f4c4d05e0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/watch_dcd267cd-6f18-4751-b281-118f4c4d05e0.svg'
AUTHOR = 'gpt-6'

class Smartwatch(Solo48):
    icon_id = 'smartwatch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ('watch', 'wearable', 'smart-watch')
    keywords = ('watch', 'wearable', 'device', 'strap', 'band', 'time')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_14 = (10, 14)
        p_11_14 = (11, 14)
        p_23_14 = (23, 14)
        p_25_14 = (25, 14)
        p_29_18 = (29, 18)
        p_29_30 = (29, 30)
        p_25_34 = (25, 34)
        p_23_34 = (23, 34)
        p_11_34 = (11, 34)
        p_10_34 = (10, 34)
        p_6_30 = (6, 30)
        p_6_18 = (6, 18)
        p_17_6 = (17, 6)
        p_30_6 = (30, 6)
        p_42_18 = (42, 18)
        p_17_42 = (17, 42)
        p_30_42 = (30, 42)
        p_42_30 = (42, 30)
        self.add_line('case-top-left', p_10_14, p_11_14)
        self.add_line('case-top', p_11_14, p_23_14)
        self.add_line('case-top-right', p_23_14, p_25_14)
        self.add_arc('case-corner-ne', p_25_14, p_29_18, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('case-right', p_29_18, p_29_30)
        self.add_arc('case-corner-se', p_29_30, p_25_34, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('case-bottom-right', p_25_34, p_23_34)
        self.add_line('case-bottom', p_23_34, p_11_34)
        self.add_line('case-bottom-left', p_11_34, p_10_34)
        self.add_arc('case-corner-sw', p_10_34, p_6_30, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('case-left', p_6_30, p_6_18)
        self.add_arc('case-corner-nw', p_6_18, p_10_14, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('strap-top-outer-rise', p_11_14, p_17_6, radius_x=6, radius_y=8, sweep=True, large_arc=False)
        self.add_line('strap-top-outer-crest', p_17_6, p_30_6)
        self.add_arc('strap-top-outer-fall', p_30_6, p_42_18, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('strap-top-inner', p_23_14, p_30_6, radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('strap-bottom-outer-fall', p_11_34, p_17_42, radius_x=6, radius_y=8, sweep=False, large_arc=False)
        self.add_line('strap-bottom-outer-trough', p_17_42, p_30_42)
        self.add_arc('strap-bottom-outer-rise', p_30_42, p_42_30, radius_x=12, radius_y=12, sweep=False, large_arc=False)
        self.add_arc('strap-bottom-inner', p_23_34, p_30_42, radius_x=13, radius_y=13, sweep=False, large_arc=False)
        self.add_contour('case', 'case-top-left', 'case-top', 'case-top-right', 'case-corner-ne', 'case-right', 'case-corner-se', 'case-bottom-right', 'case-bottom', 'case-bottom-left', 'case-corner-sw', 'case-left', 'case-corner-nw', closed=True)
        self.add_contour('strap-top-outer', 'strap-top-outer-rise', 'strap-top-outer-crest', 'strap-top-outer-fall', closed=False)
        self.add_contour('strap-bottom-outer', 'strap-bottom-outer-fall', 'strap-bottom-outer-trough', 'strap-bottom-outer-rise', closed=False)
        self.relate('connect', 'case', 'strap-top-outer')
        self.relate('connect', 'case', 'strap-top-inner')
        self.relate('connect', 'case', 'strap-bottom-outer')
        self.relate('connect', 'case', 'strap-bottom-inner')
        self.relate('connect', 'strap-top-outer', 'strap-top-inner')
        self.relate('connect', 'strap-bottom-outer', 'strap-bottom-inner')
