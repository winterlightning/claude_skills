"""A video camera with a rounded body and projecting lens.

Keyshape HRECT_M: chosen for the reference silhouette.
Lucide video: connected trapezoid and rounded enclosure; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class DigitalVideoCamera(Container64):
    icon_id = 'digital-video-camera'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('digital', 'video', 'camera')

    def build(self) -> None:
        self.add_line('body-0', (8, 14), (38, 14))
        self.add_arc('body-1', (38, 14), (44, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-2', (44, 20), (44, 44))
        self.add_arc('body-3', (44, 44), (38, 50), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-4', (38, 50), (8, 50))
        self.add_arc('body-5', (8, 50), (2, 44), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-6', (2, 44), (2, 20))
        self.add_arc('body-7', (2, 20), (8, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_polyline("lens", (44,24), (62,18), (62,46), (44,40))
        self.relate("connect", 'body', 'lens')
