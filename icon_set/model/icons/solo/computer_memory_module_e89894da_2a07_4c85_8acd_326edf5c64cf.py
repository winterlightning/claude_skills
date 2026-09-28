'Computer memory module.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e89894da-2a07-4c85-8acd-326edf5c64cf'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/computer ram_e89894da-2a07-4c85-8acd-326edf5c64cf.svg'
AUTHOR = 'gpt-6'

class ComputerMemoryModule(Solo48):
    icon_id = 'computer-memory-module'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'storage')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_4_8 = (4, 8)
        p_44_8 = (44, 8)
        p_44_32 = (44, 32)
        p_36_32 = (36, 32)
        p_24_32 = (24, 32)
        p_12_32 = (12, 32)
        p_4_32 = (4, 32)
        p_12_16 = (12, 16)
        p_20_16 = (20, 16)
        p_20_24 = (20, 24)
        p_12_24 = (12, 24)
        p_28_16 = (28, 16)
        p_36_16 = (36, 16)
        p_36_24 = (36, 24)
        p_28_24 = (28, 24)
        p_12_40 = (12, 40)
        p_24_40 = (24, 40)
        p_36_40 = (36, 40)
        self.add_line('board-0', p_4_8, p_44_8)
        self.add_line('board-1', p_44_8, p_44_32)
        self.add_line('board-2', p_44_32, p_36_32)
        self.add_line('board-3', p_36_32, p_24_32)
        self.add_line('board-4', p_24_32, p_12_32)
        self.add_line('board-5', p_12_32, p_4_32)
        self.add_line('board-6', p_4_32, p_4_8)
        self.add_line('chip-0-0', p_12_16, p_20_16)
        self.add_line('chip-0-1', p_20_16, p_20_24)
        self.add_line('chip-0-2', p_20_24, p_12_24)
        self.add_line('chip-0-3', p_12_24, p_12_16)
        self.add_line('chip-1-0', p_28_16, p_36_16)
        self.add_line('chip-1-1', p_36_16, p_36_24)
        self.add_line('chip-1-2', p_36_24, p_28_24)
        self.add_line('chip-1-3', p_28_24, p_28_16)
        self.add_line('contact-0', p_12_32, p_12_40)
        self.add_line('contact-1', p_24_32, p_24_40)
        self.add_line('contact-2', p_36_32, p_36_40)
        self.add_contour('board', 'board-0', 'board-1', 'board-2', 'board-3', 'board-4', 'board-5', 'board-6', closed=True)
        self.add_contour('chip-0', 'chip-0-0', 'chip-0-1', 'chip-0-2', 'chip-0-3', closed=True)
        self.add_contour('chip-1', 'chip-1-0', 'chip-1-1', 'chip-1-2', 'chip-1-3', closed=True)
        self.relate('connect', 'contact-0', 'board')
        self.relate('connect', 'contact-1', 'board')
        self.relate('connect', 'contact-2', 'board')
