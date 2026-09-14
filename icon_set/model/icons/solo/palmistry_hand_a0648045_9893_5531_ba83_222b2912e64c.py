'Palmistry hand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0648045-9893-5531-ba83-222b2912e64c'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/palmistry_a0648045-9893-5531-ba83-222b2912e64c.svg'
AUTHOR = 'gpt-6'

class PalmistryHand(Solo48):
    icon_id = 'palmistry-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('palmistry', 'palm reading', 'hand', 'fortune', 'divination', 'fate', 'lines', 'mystic')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_26 = (10, 26)
        p_10_14 = (10, 14)
        p_18_14 = (18, 14)
        p_18_10 = (18, 10)
        p_26_10 = (26, 10)
        p_26_12 = (26, 12)
        p_34_12 = (34, 12)
        p_34_16 = (34, 16)
        p_42_16 = (42, 16)
        p_42_30 = (42, 30)
        p_30_42 = (30, 42)
        p_22_42 = (22, 42)
        p_12_34 = (12, 34)
        p_6_26 = (6, 26)
        p_18_23 = (18, 23)
        p_26_23 = (26, 23)
        p_34_23 = (34, 23)
        p_20_32 = (20, 32)
        p_32_32 = (32, 32)
        self.add_line('index-side', p_10_26, p_10_14)
        self.add_arc('index-tip', p_10_14, p_18_14, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('middle-rise', p_18_14, p_18_10)
        self.add_arc('middle-tip', p_18_10, p_26_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('middle-fall', p_26_10, p_26_12)
        self.add_arc('ring-tip', p_26_12, p_34_12, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('ring-fall', p_34_12, p_34_16)
        self.add_arc('little-tip', p_34_16, p_42_16, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('palm-side', p_42_16, p_42_30)
        self.add_arc('heel-right', p_42_30, p_30_42, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('wrist', p_30_42, p_22_42)
        self.add_arc('heel-left', p_22_42, p_12_34, radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_line('thumb-side', p_12_34, p_6_26)
        self.add_arc('thumb-tip', p_6_26, p_10_26, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_line('index-crease', p_18_14, p_18_23)
        self.add_line('middle-crease', p_26_12, p_26_23)
        self.add_line('ring-crease', p_34_16, p_34_23)
        self.add_line('palm-line', p_20_32, p_32_32)
        self.add_contour('hand', 'index-side', 'index-tip', 'middle-rise', 'middle-tip', 'middle-fall', 'ring-tip', 'ring-fall', 'little-tip', 'palm-side', 'heel-right', 'wrist', 'heel-left', 'thumb-side', 'thumb-tip', closed=True)
        self.relate('connect', 'hand', 'index-crease')
        self.relate('connect', 'hand', 'middle-crease')
        self.relate('connect', 'hand', 'ring-crease')
