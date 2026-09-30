"""Raise the factory roof and shorten the twin smokestacks to deepen the main building.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (industrial-factory-with-smokestacks SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class IndustrialFactoryWithSmokestacks(Container64):
    icon_id = 'industrial-factory-with-smokestacks'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('building-1', (6, 58), (6, 22))
        self.add_line('building-2', (6, 22), (22, 22))
        self.add_line('building-3', (22, 22), (32, 14))
        self.add_line('building-4', (32, 14), (42, 22))
        self.add_line('building-5', (42, 22), (58, 22))
        self.add_line('building-6', (58, 22), (58, 58))
        self.add_line('building-7', (58, 58), (6, 58))
        self.add_line('stack-left-1', (8, 22), (10, 6))
        self.add_line('stack-left-2', (10, 6), (18, 6))
        self.add_line('stack-left-3', (18, 6), (22, 22))
        self.add_line('stack-right-1', (42, 22), (46, 6))
        self.add_line('stack-right-2', (46, 6), (54, 6))
        self.add_line('stack-right-3', (54, 6), (56, 22))
        self.add_contour('building', 'building-1', 'building-2', 'building-3', 'building-4', 'building-5', 'building-6', 'building-7', closed=True)
        self.add_contour('stack-left', 'stack-left-1', 'stack-left-2', 'stack-left-3')
        self.add_contour('stack-right', 'stack-right-1', 'stack-right-2', 'stack-right-3')
        self.relate('connect', 'building', 'stack-left')
        self.relate('connect', 'building', 'stack-right')
