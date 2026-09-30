"""Retain both rows of film perforations; remove the redundant horizontal dividers.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (film-frame-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class FilmFrameContainer(Container64):
    icon_id = 'film-frame-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('frame-0', (12, 6), (52, 6))
        self.add_arc('frame-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('frame-2', (58, 12), (58, 52))
        self.add_arc('frame-3', (58, 52), (52, 58), radius_x=6)
        self.add_line('frame-4', (52, 58), (12, 58))
        self.add_arc('frame-5', (12, 58), (6, 52), radius_x=6)
        self.add_line('frame-6', (6, 52), (6, 12))
        self.add_arc('frame-7', (6, 12), (12, 6), radius_x=6)
        self.add_line('perforation-14-10', (18, 14), (22, 14))
        self.add_line('perforation-30-10', (30, 14), (34, 14))
        self.add_line('perforation-46-10', (42, 14), (46, 14))
        self.add_line('perforation-14-54', (18, 50), (22, 50))
        self.add_line('perforation-30-54', (30, 50), (34, 50))
        self.add_line('perforation-46-54', (42, 50), (46, 50))
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', closed=True)
