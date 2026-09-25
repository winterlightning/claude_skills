'Memory module with notch.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f237c30-c7db-4dfc-91c5-5d21fb166711'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/computer ram_6f237c30-c7db-4dfc-91c5-5d21fb166711.svg'
AUTHOR = 'gpt-6'

class MemoryModuleWithNotch(Solo48):
    icon_id = 'memory-module-with-notch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'upgrade')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_4_8 = (4, 8)
        p_44_8 = (44, 8)
        p_44_40 = (44, 40)
        p_28_40 = (28, 40)
        p_28_36 = (28, 36)
        p_20_36 = (20, 36)
        p_20_40 = (20, 40)
        p_4_40 = (4, 40)
        p_12_16 = (12, 16)
        p_20_16 = (20, 16)
        p_20_24 = (20, 24)
        p_12_24 = (12, 24)
        p_28_16 = (28, 16)
        p_36_16 = (36, 16)
        p_36_24 = (36, 24)
        p_28_24 = (28, 24)
        self.add_line('board-0', p_4_8, p_44_8)
        self.add_line('board-1', p_44_8, p_44_40)
        self.add_line('board-2', p_44_40, p_28_40)
        self.add_line('board-3', p_28_40, p_28_36)
        self.add_line('board-4', p_28_36, p_20_36)
        self.add_line('board-5', p_20_36, p_20_40)
        self.add_line('board-6', p_20_40, p_4_40)
        self.add_line('board-7', p_4_40, p_4_8)
        self.add_line('chip-0-0', p_12_16, p_20_16)
        self.add_line('chip-0-1', p_20_16, p_20_24)
        self.add_line('chip-0-2', p_20_24, p_12_24)
        self.add_line('chip-0-3', p_12_24, p_12_16)
        self.add_line('chip-1-0', p_28_16, p_36_16)
        self.add_line('chip-1-1', p_36_16, p_36_24)
        self.add_line('chip-1-2', p_36_24, p_28_24)
        self.add_line('chip-1-3', p_28_24, p_28_16)
        self.add_contour('board', 'board-0', 'board-1', 'board-2', 'board-3', 'board-4', 'board-5', 'board-6', 'board-7', closed=True)
        self.add_contour('chip-0', 'chip-0-0', 'chip-0-1', 'chip-0-2', 'chip-0-3', closed=True)
        self.add_contour('chip-1', 'chip-1-0', 'chip-1-1', 'chip-1-2', 'chip-1-3', closed=True)
