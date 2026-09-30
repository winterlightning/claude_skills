"""Two inward-facing brackets enclose a tall content area.
Centerline extremes (2,2)-(62,62); square fit follows the wider reference.
Lucide brackets informs equal quarter-circle corners and mirrored terminals.
Both source references consolidated; no semantic detail omitted.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (pair-of-square-brackets SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class PairOfSquareBrackets(Container64):
    icon_id = 'pair-of-square-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('pair', 'of', 'square', 'brackets')

    def build(self) -> None:
        self.add_line('left-top', (14, 6), (10, 6))
        self.add_arc('left-upper', (10, 6), (6, 10), radius_x=4, sweep=False)
        self.add_line('left-spine', (6, 10), (6, 54))
        self.add_arc('left-lower', (6, 54), (10, 58), radius_x=4, sweep=False)
        self.add_line('left-bottom', (10, 58), (14, 58))
        self.add_line('right-top', (50, 6), (54, 6))
        self.add_arc('right-upper', (54, 6), (58, 10), radius_x=4)
        self.add_line('right-spine', (58, 10), (58, 54))
        self.add_arc('right-lower', (58, 54), (54, 58), radius_x=4)
        self.add_line('right-bottom', (54, 58), (50, 58))
        self.add_contour('left', 'left-top', 'left-upper', 'left-spine', 'left-lower', 'left-bottom')
        self.add_contour('right', 'right-top', 'right-upper', 'right-spine', 'right-lower', 'right-bottom')
