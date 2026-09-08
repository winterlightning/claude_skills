"""A video camera body with a projecting tapered lens.

Keyshape HRECT_L, bounds (0, 8, 64, 56): chosen for the reference proportions.
Lucide construction: video: rounded body and attached trapezoid; intentional lens asymmetry. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart blocked, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class VideoCameraIcon(Container64):
    icon_id = 'video-camera-icon'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('video', 'camera', 'icon')

    def build(self) -> None:
        self.add_line('body-0', (8, 10), (40, 10))
        self.add_arc('body-1', (40, 10), (46, 16), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-2', (46, 16), (46, 48))
        self.add_arc('body-3', (46, 48), (40, 54), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-4', (40, 54), (8, 54))
        self.add_arc('body-5', (8, 54), (2, 48), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-6', (2, 48), (2, 16))
        self.add_arc('body-7', (2, 16), (8, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_line('lens-0', (46, 24), (62, 17))
        self.add_line('lens-1', (62, 17), (62, 47))
        self.add_line('lens-2', (62, 47), (46, 40))
        self.add_contour('lens', 'lens-0', 'lens-1', 'lens-2', closed=False)
        self.relate("connect", 'body', 'lens')
