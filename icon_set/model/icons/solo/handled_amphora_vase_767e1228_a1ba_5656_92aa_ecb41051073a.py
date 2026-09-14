'Handled amphora vase.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '767e1228-a1ba-5656-92aa-ecb41051073a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/vase_767e1228-a1ba-5656-92aa-ecb41051073a.svg'
AUTHOR = 'gpt-6'

class HandledAmphoraVase(Solo48):
    icon_id = 'handled-amphora-vase'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('vase', 'amphora', 'greek', 'pottery', 'handles', 'ceramic', 'vessel', 'antique')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_15_6 = (15, 6)
        p_18_13 = (18, 13)
        p_18_16 = (18, 16)
        p_13_26 = (13, 26)
        p_24_42 = (24, 42)
        p_35_26 = (35, 26)
        p_30_16 = (30, 16)
        p_30_13 = (30, 13)
        p_33_6 = (33, 6)
        p_6_19 = (6, 19)
        p_42_19 = (42, 19)
        p_18_42 = (18, 42)
        p_30_42 = (30, 42)
        self.add_line('lip-neck-left-1', p_15_6, p_18_13)
        self.add_line('lip-neck-left-2', p_18_13, p_18_16)
        self.add_arc('shoulder-left', p_18_16, p_13_26, radius_x=6, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('body-left', p_13_26, p_24_42, radius_x=11, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('body-right', p_24_42, p_35_26, radius_x=11, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('shoulder-right', p_35_26, p_30_16, radius_x=6, radius_y=10, sweep=False, large_arc=False)
        self.add_line('neck-lip-right-1', p_30_16, p_30_13)
        self.add_line('neck-lip-right-2', p_30_13, p_33_6)
        self.add_line('neck-lip-right-3', p_33_6, p_15_6)
        self.add_arc('handle-left-top', p_18_13, p_6_19, radius_x=12, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('handle-left-bottom', p_6_19, p_13_26, radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('handle-right-top', p_30_13, p_42_19, radius_x=12, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('handle-right-bottom', p_42_19, p_35_26, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('foot-1', p_18_42, p_24_42)
        self.add_line('foot-2', p_24_42, p_30_42)
        self.add_contour('outline', 'lip-neck-left-1', 'lip-neck-left-2', 'shoulder-left', 'body-left', 'body-right', 'shoulder-right', 'neck-lip-right-1', 'neck-lip-right-2', 'neck-lip-right-3', closed=True)
        self.add_contour('handle-left', 'handle-left-top', 'handle-left-bottom', closed=False)
        self.add_contour('handle-right', 'handle-right-top', 'handle-right-bottom', closed=False)
        self.add_contour('foot', 'foot-1', 'foot-2', closed=False)
        self.relate('connect', 'outline', 'handle-left')
        self.relate('connect', 'outline', 'handle-right')
        self.relate('connect', 'outline', 'foot')
