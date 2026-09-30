"""Taller camera body and a narrower attached lens wedge.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (digital-video-camera HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class DigitalVideoCamera(Container64):
    icon_id = 'digital-video-camera'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('body-0', (10, 10), (40, 10))
        self.add_arc('body-1', (40, 10), (46, 16), radius_x=6)
        self.add_line('body-2', (46, 16), (46, 48))
        self.add_arc('body-3', (46, 48), (40, 54), radius_x=6)
        self.add_line('body-4', (40, 54), (10, 54))
        self.add_arc('body-5', (10, 54), (4, 48), radius_x=6)
        self.add_line('body-6', (4, 48), (4, 16))
        self.add_arc('body-7', (4, 16), (10, 10), radius_x=6)
        self.add_line('lens-1', (46, 26), (60, 18))
        self.add_line('lens-2', (60, 18), (60, 46))
        self.add_line('lens-3', (60, 46), (46, 38))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('lens', 'lens-1', 'lens-2', 'lens-3')
        self.relate('connect', 'body', 'lens')
