"""Broaden the frame, keeping a uniform eight-unit centerline border.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class RectangularPictureFrame(Container64):
    icon_id = 'rectangular-picture-frame'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('outer',(2,2),(62,2),(62,62),(2,62),closed=True)
        poly('inner',(10,10),(54,10),(54,54),(10,54),closed=True)
