'Minotaur bust.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86508a6a-37ec-4b4d-bb96-6228f39f0c08'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/minotaur_86508a6a-37ec-4b4d-bb96-6228f39f0c08.svg'
AUTHOR = 'gpt-6'

class MinotaurBust(Solo48):
    icon_id = 'minotaur-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('minotaur', 'bull', 'mythology', 'greek', 'horns', 'beast', 'labyrinth', 'legend')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_16 = (16, 16)
        p_32_16 = (32, 16)
        p_31_27 = (31, 27)
        p_26_32 = (26, 32)
        p_22_32 = (22, 32)
        p_17_27 = (17, 27)
        p_9_6 = (9, 6)
        p_39_6 = (39, 6)
        p_8_21 = (8, 21)
        p_40_21 = (40, 21)
        p_6_42 = (6, 42)
        p_14_36 = (14, 36)
        p_34_36 = (34, 36)
        p_42_42 = (42, 42)
        self.add_line('brow', p_16_16, p_32_16)
        self.add_line('cheek-right', p_32_16, p_31_27)
        self.add_arc('jaw-right', p_31_27, p_26_32, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('chin', p_26_32, p_22_32)
        self.add_arc('jaw-left', p_22_32, p_17_27, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('cheek-left', p_17_27, p_16_16)
        self.add_arc('horn-left', p_16_16, p_9_6, radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('horn-right', p_32_16, p_39_6, radius_x=7, radius_y=10, sweep=False, large_arc=False)
        self.add_line('ear-left-1', p_16_16, p_8_21)
        self.add_line('ear-right-1', p_32_16, p_40_21)
        self.add_arc('shoulder-left', p_6_42, p_14_36, radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_line('neck-left', p_14_36, p_22_32)
        self.add_line('neck-right', p_26_32, p_34_36)
        self.add_arc('shoulder-right', p_34_36, p_42_42, radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('head', 'brow', 'cheek-right', 'jaw-right', 'chin', 'jaw-left', 'cheek-left', closed=True)
        self.add_contour('ear-left', 'ear-left-1', closed=False)
        self.add_contour('ear-right', 'ear-right-1', closed=False)
        self.add_contour('bust-left', 'shoulder-left', 'neck-left', closed=False)
        self.add_contour('bust-right', 'neck-right', 'shoulder-right', closed=False)
        self.relate('connect', 'head', 'horn-left')
        self.relate('connect', 'head', 'horn-right')
        self.relate('connect', 'head', 'ear-left')
        self.relate('connect', 'head', 'ear-right')
        self.relate('connect', 'head', 'bust-left')
        self.relate('connect', 'head', 'bust-right')
        self.relate('connect', 'horn-left', 'ear-left')
        self.relate('connect', 'horn-right', 'ear-right')
