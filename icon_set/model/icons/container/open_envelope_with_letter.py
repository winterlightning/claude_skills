"""Lower the envelope fold so the letter has more visible height.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-envelope-with-letter SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
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
        self.add_line('envelope-0', (58, 35), (58, 52))
        self.add_arc('envelope-1', (58, 52), (52, 58), radius_x=6)
        self.add_line('envelope-2', (52, 58), (12, 58))
        self.add_arc('envelope-3', (12, 58), (6, 52), radius_x=6)
        self.add_line('envelope-4', (6, 52), (6, 35))
        self.add_line('fold-1', (6, 35), (26, 45))
        self.add_line('fold-2', (26, 45), (38, 45))
        self.add_line('fold-3', (38, 45), (58, 35))
        self.add_line('paper-0', (14, 39), (14, 10))
        self.add_arc('paper-1', (14, 10), (18, 6), radius_x=4)
        self.add_line('paper-2', (18, 6), (46, 6))
        self.add_arc('paper-3', (46, 6), (50, 10), radius_x=4)
        self.add_line('paper-4', (50, 10), (50, 39))
        self.add_line('seam-left', (26, 45), (20, 50))
        self.add_line('seam-right', (38, 45), (44, 50))
        self.add_contour('envelope', 'envelope-0', 'envelope-1', 'envelope-2', 'envelope-3', 'envelope-4')
        self.add_contour('fold', 'fold-1', 'fold-2', 'fold-3')
        self.add_contour('paper', 'paper-0', 'paper-1', 'paper-2', 'paper-3', 'paper-4')
        self.relate('connect', 'envelope', 'fold')
        self.relate('connect', 'paper', 'fold')
        self.relate('connect', 'seam-left', 'fold')
        self.relate('connect', 'seam-right', 'fold')
