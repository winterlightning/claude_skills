"""Enlarge the lens slightly while retaining the diagonal handle.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (search-magnifying-glass SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class SearchMagnifyingGlass(Container64):
    icon_id = 'search-magnifying-glass'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('lens-0', (6, 28), (50, 28), radius_x=22)
        self.add_arc('lens-1', (50, 28), (6, 28), radius_x=22)
        self.add_line('handle', (42, 44), (58, 58))
        self.add_contour('lens', 'lens-0', 'lens-1', closed=True)
        self.relate('connect', 'lens', 'handle')
