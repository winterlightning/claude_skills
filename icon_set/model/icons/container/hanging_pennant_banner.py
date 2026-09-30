"""Widen the banner while keeping the cord and pointed lower edge.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hanging-pennant-banner VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class HangingPennantBanner(Container64):
    icon_id = 'hanging-pennant-banner'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('rod', (10, 15), (54, 15))
        self.add_line('cord-1', (22, 15), (32, 4))
        self.add_line('cord-2', (32, 4), (42, 15))
        self.add_line('banner-1', (14, 15), (14, 49))
        self.add_line('banner-2', (14, 49), (32, 60))
        self.add_line('banner-3', (32, 60), (50, 49))
        self.add_line('banner-4', (50, 49), (50, 15))
        self.add_contour('cord', 'cord-1', 'cord-2')
        self.add_contour('banner', 'banner-1', 'banner-2', 'banner-3', 'banner-4')
        self.relate('connect', 'rod', 'cord')
        self.relate('connect', 'rod', 'banner')
        self.relate('connect', 'cord', 'banner')
