"""Broaden the frame, keeping a uniform eight-unit centerline border.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rectangular-picture-frame SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class RectangularPictureFrame(Container64):
    icon_id = 'rectangular-picture-frame'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('outer-1', (6, 6), (58, 6))
        self.add_line('outer-2', (58, 6), (58, 58))
        self.add_line('outer-3', (58, 58), (6, 58))
        self.add_line('outer-4', (6, 58), (6, 6))
        self.add_line('inner-1', (14, 14), (50, 14))
        self.add_line('inner-2', (50, 14), (50, 50))
        self.add_line('inner-3', (50, 50), (14, 50))
        self.add_line('inner-4', (14, 50), (14, 14))
        self.add_contour('outer', 'outer-1', 'outer-2', 'outer-3', 'outer-4', closed=True)
        self.add_contour('inner', 'inner-1', 'inner-2', 'inner-3', 'inner-4', closed=True)
