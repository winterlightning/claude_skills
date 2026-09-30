"""Increase the artboard area and shorten the external indicator ticks.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-artboard-with-corner-indicators SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class SquareArtboardWithCornerIndicators(Container64):
    icon_id = 'square-artboard-with-corner-indicators'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('artboard-1', (14, 14), (50, 14))
        self.add_line('artboard-2', (50, 14), (50, 50))
        self.add_line('artboard-3', (50, 50), (14, 50))
        self.add_line('artboard-4', (14, 50), (14, 14))
        self.add_line('top-0', (14, 6), (14, 8))
        self.add_line('bottom-0', (14, 56), (14, 58))
        self.add_line('left-0', (6, 14), (8, 14))
        self.add_line('right-0', (56, 14), (58, 14))
        self.add_line('top-1', (50, 6), (50, 8))
        self.add_line('bottom-1', (50, 56), (50, 58))
        self.add_line('left-1', (6, 50), (8, 50))
        self.add_line('right-1', (56, 50), (58, 50))
        self.add_contour('artboard', 'artboard-1', 'artboard-2', 'artboard-3', 'artboard-4', closed=True)
