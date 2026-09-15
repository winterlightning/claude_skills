'Beaded loop with heart charm.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8956c423-cf27-57a5-a230-a97f31d05f44'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/necklace pendant_8956c423-cf27-57a5-a230-a97f31d05f44.svg'
AUTHOR = 'gpt-6'

class BeadedLoopWithHeartCharm(Solo48):
    icon_id = 'beaded-loop-with-heart-charm'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('bead', 'beaded', 'bracelet', 'necklace', 'heart', 'charm', 'jewellery', 'jewelry', 'loop')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_6 = (19, 6)
        p_11_11 = (11, 11)
        p_6_19 = (6, 19)
        p_10_27 = (10, 27)
        p_17_31 = (17, 31)
        p_26_27 = (26, 27)
        p_31_18 = (31, 18)
        p_27_11 = (27, 11)
        p_34_31 = (34, 31)
        p_26_31 = (26, 31)
        p_34_42 = (34, 42)
        p_42_31 = (42, 31)
        self.add_line('bead-0', p_19_6, p_19_6)
        self.add_line('bead-1', p_11_11, p_11_11)
        self.add_line('bead-2', p_6_19, p_6_19)
        self.add_line('bead-3', p_10_27, p_10_27)
        self.add_line('bead-4', p_17_31, p_17_31)
        self.add_line('bead-5', p_26_27, p_26_27)
        self.add_line('bead-6', p_31_18, p_31_18)
        self.add_line('bead-7', p_27_11, p_27_11)
        self.add_arc('charm-l', p_34_31, p_26_31, radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('charm-ls', p_26_31, p_34_42)
        self.add_line('charm-rs', p_34_42, p_42_31)
        self.add_arc('charm-r', p_42_31, p_34_31, radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('link', p_26_27, p_26_31)
        self.add_contour('charm', 'charm-l', 'charm-ls', 'charm-rs', 'charm-r', closed=True)
        self.relate('connect', 'bead-5', 'link')
        self.relate('connect', 'charm', 'link')
        self.relate('connect', 'charm', 'link')
