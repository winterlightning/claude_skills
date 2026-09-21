"""Taller camera body and a narrower attached lens wedge.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class DigitalVideoCamera(Container64):
    icon_id = 'digital-video-camera'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'body',2,6,48,58,6)
        poly('lens',(48,22),(62,14),(62,50),(48,42));join('body','lens')
