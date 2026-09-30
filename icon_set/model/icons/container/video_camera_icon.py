"""A video camera body with a projecting tapered lens.

Keyshape HRECT_L, bounds (0, 8, 64, 56): chosen for the reference proportions.
Lucide construction: video: rounded body and attached trapezoid; intentional lens asymmetry. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart blocked, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (video-camera-icon HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class VideoCameraIcon(Container64):
    icon_id = 'video-camera-icon'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('video', 'camera', 'icon')

    def build(self) -> None:
        self.add_line('body-0', (10, 12), (39, 12))
        self.add_arc('body-1', (39, 12), (45, 18), radius_x=6)
        self.add_line('body-2', (45, 18), (45, 46))
        self.add_arc('body-3', (45, 46), (39, 52), radius_x=6)
        self.add_line('body-4', (39, 52), (10, 52))
        self.add_arc('body-5', (10, 52), (4, 46), radius_x=6)
        self.add_line('body-6', (4, 46), (4, 18))
        self.add_arc('body-7', (4, 18), (10, 12), radius_x=6)
        self.add_line('lens-0', (45, 26), (60, 19))
        self.add_line('lens-1', (60, 19), (60, 45))
        self.add_line('lens-2', (60, 45), (45, 38))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('lens', 'lens-0', 'lens-1', 'lens-2')
        self.relate('connect', 'body', 'lens')
