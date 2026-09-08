"""A cylindrical metal can with an oval rim and curved base.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide cylinder: elliptical rim and straight sides; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class MetalTinCan(Container64):
    icon_id = 'metal-tin-can'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('metal', 'tin', 'can')

    def build(self) -> None:
        self.add_arc('rim-0', (10, 10), (54, 10), radius_x=22, radius_y=8, sweep=True)
        self.add_arc('rim-1', (54, 10), (10, 10), radius_x=22, radius_y=8, sweep=True)
        self.add_contour('rim', 'rim-0', 'rim-1', closed=True)
        self.add_line('body-0', (54, 10), (54, 54))
        self.add_arc('body-1', (54, 54), (10, 54), radius_x=22, radius_y=8, sweep=True)
        self.add_line('body-2', (10, 54), (10, 10))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', closed=False)
        self.relate("connect", "rim", "body")
