"""Retain both rows of film perforations; remove the redundant horizontal dividers.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class FilmFrameContainer(Container64):
    icon_id = 'film-frame-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'frame',2,2,62,62,6)
        for y in (10,54):
         for x in (14,30,46):line(f'perforation-{x}-{y}',(x,y),(x+4,y))
