"""An open circular power enclosure with a small ring above its opening.

SQUARE: centerline extremes (2,2)-(62,62). The user explicitly confirmed
container classification. Lucide power original and atomic-debug inform
an open circular sweep, but the supplied reference's small top circle is
retained instead of substituting Lucide's vertical bar. Mirrored about x=32;
no source-defining detail is dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class MinimalistPowerButton(Container64):
    icon_id = 'minimalist-power-button'
    keyshape = Keyshape.SQUARE
    aliases = ('power-ring-container',)
    keywords = ('power', 'button', 'switch', 'circle')

    def build(self) -> None:
        # Ellipse radii 30 and 25 about (32,37); exact 3:4:5 endpoints.
        self.add_arc('outer-ne',(50,17),(62,37),radius_x=30,radius_y=25)
        self.add_arc('outer-se',(62,37),(32,62),radius_x=30,radius_y=25)
        self.add_arc('outer-sw',(32,62),(2,37),radius_x=30,radius_y=25)
        self.add_arc('outer-nw',(2,37),(14,17),radius_x=30,radius_y=25)
        self.add_contour('outer','outer-ne','outer-se','outer-sw','outer-nw')
        self.add_arc('button-upper',(20,14),(44,14),radius_x=12)
        self.add_arc('button-lower',(44,14),(20,14),radius_x=12)
        self.add_contour('button','button-upper','button-lower',closed=True)
