"""Enlarge the lens and camera body while preserving the raised top housing.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (photo-camera-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '6fa1ce5b-48af-4189-80e1-5043fdcf9429'
SOURCE_PATH = 'pictographic-primitives/photography/camera_6fa1ce5b-48af-4189-80e1-5043fdcf9429.svg'
AUTHOR = 'claude-opus-5-5'


class PhotoCameraContainer(Container64):
    icon_id = 'photo-camera-container'
    keyshape = Keyshape.SQUARE
    category = 'photography'
    categories = ('photography', 'other', 'primitives-generate')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('body-0', (12, 10), (22, 10))
        self.add_line('body-1', (22, 10), (28, 6))
        self.add_line('body-2', (28, 6), (36, 6))
        self.add_line('body-3', (36, 6), (42, 10))
        self.add_line('body-4', (42, 10), (52, 10))
        self.add_arc('body-5', (52, 10), (58, 16), radius_x=6)
        self.add_line('body-6', (58, 16), (58, 52))
        self.add_arc('body-7', (58, 52), (52, 58), radius_x=6)
        self.add_line('body-8', (52, 58), (12, 58))
        self.add_arc('body-9', (12, 58), (6, 52), radius_x=6)
        self.add_line('body-10', (6, 52), (6, 16))
        self.add_arc('body-11', (6, 16), (12, 10), radius_x=6)
        self.add_arc('lens-0', (15, 34), (49, 34), radius_x=17)
        self.add_arc('lens-1', (49, 34), (15, 34), radius_x=17)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_contour('lens', 'lens-0', 'lens-1', closed=True)
