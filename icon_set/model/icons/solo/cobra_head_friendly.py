'Cobra head friendly.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/cobra_head_friendly.py'
AUTHOR = 'gpt-6'

class CobraHeadFriendly(Solo48):
    icon_id = 'cobra-head-friendly'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('cobra-head',)
    keywords = ('cobra', 'snake', 'reptile', 'hood', 'head', 'friendly')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_4 = (24, 4)
        p_40_19 = (40, 19)
        p_32_36 = (32, 36)
        p_29_41 = (29, 41)
        p_29_44 = (29, 44)
        p_19_44 = (19, 44)
        p_19_41 = (19, 41)
        p_16_36 = (16, 36)
        p_8_19 = (8, 19)
        p_19_20 = (19, 20)
        p_29_20 = (29, 20)
        self.add_arc('hood-upper-right', p_24_4, p_40_19, radius_x=16, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('hood-lower-right', p_40_19, p_32_36, radius_x=8, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('neck-turn-right', p_32_36, p_29_41, radius_x=3, radius_y=5, sweep=False, large_arc=False)
        self.add_line('neck-right', p_29_41, p_29_44)
        self.add_line('neck-base', p_29_44, p_19_44)
        self.add_line('neck-left', p_19_44, p_19_41)
        self.add_arc('neck-turn-left', p_19_41, p_16_36, radius_x=3, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('hood-lower-left', p_16_36, p_8_19, radius_x=8, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('hood-upper-left', p_8_19, p_24_4, radius_x=16, radius_y=15, sweep=True, large_arc=False)
        self.add_line('eye-left', p_19_20, p_19_20)
        self.add_line('eye-right', p_29_20, p_29_20)
        self.add_contour('hood', 'hood-upper-right', 'hood-lower-right', 'neck-turn-right', 'neck-right', 'neck-base', 'neck-left', 'neck-turn-left', 'hood-lower-left', 'hood-upper-left', closed=True)
