'Flaming brazier.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '187100cd-0bd8-46ed-983a-227a3588d8e9'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/greek fire_187100cd-0bd8-46ed-983a-227a3588d8e9.svg'
AUTHOR = 'gpt-6'

class FlamingBrazier(Solo48):
    icon_id = 'flaming-brazier'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('brazier', 'fire', 'flame', 'greek', 'olympic', 'torch', 'ritual', 'ancient')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_17 = (16, 17)
        p_19_12 = (19, 12)
        p_24_10 = (24, 10)
        p_26_4 = (26, 4)
        p_32_17 = (32, 17)
        p_8_26 = (8, 26)
        p_40_26 = (40, 26)
        p_33_34 = (33, 34)
        p_15_34 = (15, 34)
        p_12_44 = (12, 44)
        p_36_44 = (36, 44)
        self.add_arc('flame-left', p_16_17, p_19_12, radius_x=11, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('flame-notch', p_19_12, p_24_10, radius_x=3, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('flame-hook', p_24_10, p_26_4, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('flame-right', p_26_4, p_32_17, radius_x=19, radius_y=20, sweep=True, large_arc=False)
        self.add_line('rim', p_8_26, p_40_26)
        self.add_arc('bowl-right', p_40_26, p_33_34, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('bowl-bottom', p_33_34, p_15_34, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('bowl-left', p_15_34, p_8_26, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_line('leg-left', p_15_34, p_12_44)
        self.add_line('leg-right', p_33_34, p_36_44)
        self.add_contour('flame', 'flame-left', 'flame-notch', 'flame-hook', 'flame-right', closed=False)
        self.add_contour('bowl', 'rim', 'bowl-right', 'bowl-bottom', 'bowl-left', closed=True)
        self.relate('connect', 'bowl', 'leg-left')
        self.relate('connect', 'bowl', 'leg-right')
