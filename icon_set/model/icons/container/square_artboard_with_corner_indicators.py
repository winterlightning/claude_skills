"""Increase the artboard area and shorten the external indicator ticks.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class SquareArtboardWithCornerIndicators(Container64):
    icon_id = 'square-artboard-with-corner-indicators'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('artboard',(10,10),(54,10),(54,54),(10,54),closed=True)
        for n,p in enumerate((10,54)):
         line(f'top-{n}',(p,2),(p,4));line(f'bottom-{n}',(p,60),(p,62));line(f'left-{n}',(2,p),(4,p));line(f'right-{n}',(60,p),(62,p))
