'Witches cauldron.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0575da1b-6796-47d7-acc0-06fde95480bb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/witch cauldron_0575da1b-6796-47d7-acc0-06fde95480bb.svg'
AUTHOR = 'gpt-6'

class WitchesCauldron(Solo48):
    icon_id = 'witches-cauldron'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('cauldron', 'witch', 'pot', 'potion', 'brew', 'magic', 'halloween', 'spell')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_21 = (6, 21)
        p_10_21 = (10, 21)
        p_38_21 = (38, 21)
        p_42_21 = (42, 21)
        p_34_37 = (34, 37)
        p_14_37 = (14, 37)
        p_10_42 = (10, 42)
        p_38_42 = (38, 42)
        p_18_6 = (18, 6)
        p_16_8 = (16, 8)
        p_13_11 = (13, 11)
        p_13_12 = (13, 21)
        p_32_6 = (32, 6)
        p_29_8 = (29, 8)
        p_27_11 = (27, 11)
        p_27_12 = (27, 21)
        self.add_line('rim-1', p_6_21, p_10_21)
        self.add_line('rim-2a', p_10_21, p_13_12)
        self.add_line('rim-2b', p_13_12, p_27_12)
        self.add_line('rim-2c', p_27_12, p_38_21)
        self.add_line('rim-3', p_38_21, p_42_21)
        self.add_arc('bowl-right', p_38_21, p_34_37, radius_x=15, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('bowl-base', p_34_37, p_14_37, radius_x=18, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('bowl-left', p_14_37, p_10_21, radius_x=15, radius_y=13, sweep=True, large_arc=False)
        self.add_line('foot-left', p_14_37, p_10_42)
        self.add_line('foot-right', p_34_37, p_38_42)
        self.add_arc('left-steam-top', p_18_6, p_16_8, radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-steam-bottom', p_16_8, p_13_11, radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('left-steam-stem', p_13_11, p_13_12)
        self.add_arc('right-steam-top', p_32_6, p_29_8, radius_x=3, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('right-steam-bottom', p_29_8, p_27_11, radius_x=2, radius_y=3, sweep=False, large_arc=False)
        self.add_line('right-steam-stem', p_27_11, p_27_12)
        self.add_contour('rim', 'rim-1', 'rim-2a', 'rim-2b', 'rim-2c', 'rim-3', closed=False)
        self.add_contour('bowl', 'bowl-right', 'bowl-base', 'bowl-left', closed=False)
        self.add_contour('left-steam', 'left-steam-top', 'left-steam-bottom', 'left-steam-stem', closed=False)
        self.add_contour('right-steam', 'right-steam-top', 'right-steam-bottom', 'right-steam-stem', closed=False)
        self.relate('connect', 'rim', 'bowl')
        self.relate('connect', 'bowl', 'foot-left')
        self.relate('connect', 'bowl', 'foot-right')
        self.relate('connect','left-steam','rim')
        self.relate('connect','right-steam','rim')
