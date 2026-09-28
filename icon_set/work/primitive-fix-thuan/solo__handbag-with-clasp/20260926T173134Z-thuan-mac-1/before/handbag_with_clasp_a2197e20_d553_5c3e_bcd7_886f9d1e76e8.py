'Handbag with clasp.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2197e20-d553-5c3e-bcd7-886f9d1e76e8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/bag purse_a2197e20-d553-5c3e-bcd7-886f9d1e76e8.svg'
AUTHOR = 'gpt-6'

class HandbagWithClasp(Solo48):
    icon_id = 'handbag-with-clasp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('bag', 'handbag', 'purse', 'clasp', 'fashion', 'accessory', 'satchel', 'flap')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_13_17 = (13, 17)
        p_15_17 = (15, 17)
        p_33_17 = (33, 17)
        p_35_17 = (35, 17)
        p_42_24 = (42, 24)
        p_42_35 = (42, 35)
        p_35_42 = (35, 42)
        p_13_42 = (13, 42)
        p_6_35 = (6, 35)
        p_6_24 = (6, 24)
        p_6_23 = (6, 23)
        p_19_30 = (19, 30)
        p_29_30 = (29, 30)
        p_42_23 = (42, 23)
        p_22_26 = (22, 26)
        p_26_26 = (26, 26)
        p_29_31 = (29, 31)
        p_26_34 = (26, 34)
        p_22_34 = (22, 34)
        p_19_31 = (19, 31)
        self.add_line('body-0-attach-0', p_13_17, p_15_17)
        self.add_line('body-0-attach-1', p_15_17, p_33_17)
        self.add_line('body-0-attach-2', p_33_17, p_35_17)
        self.add_arc('body-1', p_35_17, p_42_24, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('body-2', p_42_24, p_42_35)
        self.add_arc('body-3', p_42_35, p_35_42, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('body-4', p_35_42, p_13_42)
        self.add_arc('body-5', p_13_42, p_6_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('body-6', p_6_35, p_6_24)
        self.add_arc('body-7', p_6_24, p_13_17, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('handle', p_15_17, p_33_17, radius_x=9, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('flap-left', p_6_23, p_19_30, radius_x=13, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('flap-right', p_29_30, p_42_23, radius_x=13, radius_y=7, sweep=False, large_arc=False)
        self.add_line('clasp-0', p_22_26, p_26_26)
        self.add_arc('clasp-1', p_26_26, p_29_30, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('clasp-2', p_29_30, p_29_31)
        self.add_arc('clasp-3', p_29_31, p_26_34, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('clasp-4', p_26_34, p_22_34)
        self.add_arc('clasp-5', p_22_34, p_19_31, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('clasp-6', p_19_31, p_19_30)
        self.add_arc('clasp-7', p_19_30, p_22_26, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('body', 'body-0-attach-0', 'body-0-attach-1', 'body-0-attach-2', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('clasp', 'clasp-0', 'clasp-1', 'clasp-2', 'clasp-3', 'clasp-4', 'clasp-5', 'clasp-6', 'clasp-7', closed=True)
        self.relate('connect', 'body', 'handle')
        self.relate('connect', 'body', 'flap-left')
        self.relate('connect', 'body', 'flap-right')
        self.relate('connect', 'clasp', 'flap-left')
        self.relate('connect', 'clasp', 'flap-right')
