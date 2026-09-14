'Intertwined snakes.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'
AUTHOR = 'gpt-6'

class IntertwinedSnakes(Solo48):
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('snake', 'serpent', 'intertwined', 'caduceus', 'mythology', 'coil', 'reptile', 'symbol')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_11 = (19, 11)
        p_21_6 = (21, 6)
        p_16_6 = (16, 6)
        p_6_14 = (6, 14)
        p_14_21 = (14, 21)
        p_24_24 = (24, 24)
        p_34_27 = (34, 27)
        p_42_34 = (42, 34)
        p_32_42 = (32, 42)
        p_32_6 = (32, 6)
        p_42_14 = (42, 14)
        p_34_21 = (34, 21)
        p_14_27 = (14, 27)
        p_6_34 = (6, 34)
        p_16_42 = (16, 42)
        p_21_42 = (21, 42)
        p_19_37 = (19, 37)
        self.add_line('head-a-1', p_19_11, p_21_6)
        self.add_line('head-a-2', p_21_6, p_16_6)
        self.add_arc('upper-a-outer', p_16_6, p_6_14, radius_x=10, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('upper-a-inner', p_6_14, p_14_21, radius_x=8, radius_y=7, sweep=False, large_arc=False)
        self.add_line('cross-a-upper', p_14_21, p_24_24)
        self.add_line('cross-a-lower', p_24_24, p_34_27)
        self.add_arc('lower-a-inner', p_34_27, p_42_34, radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tail-a', p_42_34, p_32_42, radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('tail-b', p_32_6, p_42_14, radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('upper-b-inner', p_42_14, p_34_21, radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_line('cross-b-upper', p_34_21, p_24_24)
        self.add_line('cross-b-lower', p_24_24, p_14_27)
        self.add_arc('lower-b-inner', p_14_27, p_6_34, radius_x=8, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('lower-b-outer', p_6_34, p_16_42, radius_x=10, radius_y=8, sweep=False, large_arc=False)
        self.add_line('head-b-1', p_16_42, p_21_42)
        self.add_line('head-b-2', p_21_42, p_19_37)
        self.add_contour('snake-a', 'head-a-1', 'head-a-2', 'upper-a-outer', 'upper-a-inner', 'cross-a-upper', 'cross-a-lower', 'lower-a-inner', 'tail-a', closed=False)
        self.add_contour('snake-b', 'tail-b', 'upper-b-inner', 'cross-b-upper', 'cross-b-lower', 'lower-b-inner', 'lower-b-outer', 'head-b-1', 'head-b-2', closed=False)
        self.relate('connect', 'snake-a', 'snake-b')
