"""Lower the envelope fold so the letter has more visible height.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-envelope-with-letter SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class OpenEnvelopeWithLetter(Container64):
    icon_id = 'open-envelope-with-letter'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # The envelope sits lower (its sides start at 40, the fold V bottoms out at 50) so the letter (14..50, kept
        # 8 from the envelope sides) holds a symbol of 24 with a 4 px gap (was 23).
        self.add_line('envelope-0', (58, 40), (58, 52))
        self.add_arc('envelope-1', (58, 52), (52, 58), radius_x=6)
        self.add_line('envelope-2', (52, 58), (12, 58))
        self.add_arc('envelope-3', (12, 58), (6, 52), radius_x=6)
        self.add_line('envelope-4', (6, 52), (6, 40))
        self.add_line('fold-1', (6, 40), (26, 50))
        self.add_line('fold-2', (26, 50), (38, 50))
        self.add_line('fold-3', (38, 50), (58, 40))
        self.add_line('paper-0', (14, 44), (14, 10))
        self.add_arc('paper-1', (14, 10), (18, 6), radius_x=4)
        self.add_line('paper-2', (18, 6), (46, 6))
        self.add_arc('paper-3', (46, 6), (50, 10), radius_x=4)
        self.add_line('paper-4', (50, 10), (50, 44))
        self.add_contour('envelope', 'envelope-0', 'envelope-1', 'envelope-2', 'envelope-3', 'envelope-4')
        self.add_contour('fold', 'fold-1', 'fold-2', 'fold-3')
        self.add_contour('paper', 'paper-0', 'paper-1', 'paper-2', 'paper-3', 'paper-4')
        self.relate('connect', 'envelope', 'fold')
        self.relate('connect', 'paper', 'fold')
