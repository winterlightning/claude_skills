# Variant of beaded-loop-with-heart-charm; parent file remains unchanged.
"""Beaded loop with lower-right heart. SQUARE (2,2)-(46,46) supports the offset charm. Eight solid beads replace twelve touching hollow beads. Heart informed by Lucide lobes; asymmetry preserves source charm position."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8956c423-cf27-57a5-a230-a97f31d05f44'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/necklace pendant_8956c423-cf27-57a5-a230-a97f31d05f44.svg'
AUTHOR = 'gpt-6'

class BeadedLoopWithHeartCharmVariant2(Solo48):
    icon_id = 'beaded-loop-with-heart-charm-v2'
    variant_of = 'beaded-loop-with-heart-charm'
    variant_label = 'the heart must have the same angle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('bead', 'beaded', 'bracelet', 'necklace', 'heart', 'charm', 'jewellery', 'jewelry', 'loop')

    def build(self) -> None:
        self.add_dot('bead-0', (18, 2))
        self.add_dot('bead-1', (8, 8))
        self.add_dot('bead-2', (2, 18))
        self.add_dot('bead-3', (7, 28))
        self.add_dot('bead-4', (17, 33))
        self.add_dot('bead-5', (28, 28))
        self.add_dot('bead-6', (33, 18))
        self.add_dot('bead-7', (28, 8))
        # Heart points southeast, matching the source charm's angle.
        self.add_arc('lobe-left', (34,34), (34,46), radius_x=6, sweep=False)
        self.add_line('side-left', (34,46), (46,46))
        self.add_line('side-right', (46,46), (46,34))
        self.add_arc('lobe-right', (46,34), (34,34), radius_x=6, sweep=False)
        self.add_contour('charm', 'lobe-left', 'side-left', 'side-right', 'lobe-right', closed=True)
        self.add_line('link', (28,28), (34,34))
        self.relate('connect', 'bead-5', 'link')
        self.relate('connect', 'charm', 'link')
