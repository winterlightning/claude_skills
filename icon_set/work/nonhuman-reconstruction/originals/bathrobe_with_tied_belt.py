'Bathrobe with tied belt.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/bathrobe_with_tied_belt.py'
AUTHOR = 'gpt-6'

class BathrobeWithTiedBelt(Solo48):
    icon_id = 'bathrobe-with-tied-belt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/clothing'
    aliases = ('bathrobe', 'robe', 'dressing-gown')
    keywords = ('bathrobe', 'robe', 'spa', 'bath', 'hotel', 'garment', 'clothing', 'belt')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_15_40 = (15, 40)
        p_15_22 = (15, 22)
        p_12_19 = (12, 19)
        p_8_10 = (8, 10)
        p_18_4 = (18, 4)
        p_30_4 = (30, 4)
        p_40_10 = (40, 10)
        p_36_19 = (36, 19)
        p_33_22 = (33, 22)
        p_33_40 = (33, 40)
        p_31_44 = (31, 44)
        p_17_44 = (17, 44)
        p_24_30 = (24, 30)
        p_15_30 = (15, 30)
        p_33_30 = (33, 30)
        self.add_line('robe-upper-0', p_15_40, p_15_22)
        self.add_line('robe-upper-1', p_15_22, p_12_19)
        self.add_line('robe-upper-2', p_12_19, p_8_10)
        self.add_line('robe-upper-3', p_8_10, p_18_4)
        self.add_line('robe-upper-4', p_18_4, p_30_4)
        self.add_line('robe-upper-5', p_30_4, p_40_10)
        self.add_line('robe-upper-6', p_40_10, p_36_19)
        self.add_line('robe-upper-7', p_36_19, p_33_22)
        self.add_line('robe-upper-8', p_33_22, p_33_40)
        self.add_arc('hem-right', p_33_40, p_31_44, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('hem-base', p_31_44, p_17_44)
        self.add_arc('hem-left', p_17_44, p_15_40, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('wrap-left', p_18_4, p_24_30)
        self.add_line('wrap-right', p_30_4, p_24_30)
        self.add_line('waist-belt', p_15_30, p_33_30)
        self.add_contour('robe-outline', 'robe-upper-0', 'robe-upper-1', 'robe-upper-2', 'robe-upper-3', 'robe-upper-4', 'robe-upper-5', 'robe-upper-6', 'robe-upper-7', 'robe-upper-8', 'hem-right', 'hem-base', 'hem-left', closed=True)
        self.relate('connect', 'robe-outline', 'wrap-left')
        self.relate('connect', 'robe-outline', 'wrap-right')
        self.relate('connect', 'robe-outline', 'waist-belt')
        self.relate('connect', 'wrap-left', 'wrap-right')
        self.relate('connect', 'wrap-left', 'waist-belt')
        self.relate('connect', 'wrap-right', 'waist-belt')
