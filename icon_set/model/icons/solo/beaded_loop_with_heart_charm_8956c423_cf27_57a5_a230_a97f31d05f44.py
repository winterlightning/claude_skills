"""Beaded loop with lower-right heart. SQUARE (2,2)-(46,46) supports the offset charm. Eight solid beads replace twelve touching hollow beads. Heart informed by Lucide lobes; asymmetry preserves source charm position."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8956c423-cf27-57a5-a230-a97f31d05f44'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/necklace pendant_8956c423-cf27-57a5-a230-a97f31d05f44.svg'
AUTHOR = 'astra-chatgpt'


class BeadedLoopWithHeartCharm(Solo48):
    icon_id = 'beaded-loop-with-heart-charm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bead', 'beaded', 'bracelet', 'necklace', 'heart', 'charm', 'jewellery', 'jewelry', 'loop')

    def build(self) -> None:
        self.add_dot("bead-0", (18, 2))
        self.add_dot("bead-1", (8, 8))
        self.add_dot("bead-2", (2, 18))
        self.add_dot("bead-3", (7, 28))
        self.add_dot("bead-4", (17, 33))
        self.add_dot("bead-5", (28, 28))
        self.add_dot("bead-6", (33, 18))
        self.add_dot("bead-7", (28, 8))
        self.add_arc('charm-l', (36, 33), (28, 29), radius_x=5, sweep=False)
        self.add_arc('charm-outer-l', (28, 29), (26, 33), radius_x=5, sweep=False)
        self.add_line('charm-ls', (26, 33), (36, 46))
        self.add_line('charm-rs', (36, 46), (46, 33))
        self.add_arc('charm-r', (46, 33), (36, 33), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('charm', 'charm-l', 'charm-outer-l', 'charm-ls', 'charm-rs', 'charm-r', closed=True)
        self.add_line('link', (28, 28), (28, 29))
        self.relate("connect", 'bead-5', 'link')
        self.relate("connect", 'charm', 'link')
