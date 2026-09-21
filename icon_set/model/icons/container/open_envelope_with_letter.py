"""Lower the envelope fold so the letter has more visible height.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class OpenEnvelopeWithLetter(Container64):
    icon_id = 'open-envelope-with-letter'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'envelope',(62,38),[('L',(62,56)),('A',(56,62),6,6,True),('L',(8,62)),('A',(2,56),6,6,True),('L',(2,38))])
        poly('fold',(2,38),(22,48),(42,48),(62,38));join('envelope','fold')
        path(self,'paper',(10,42),[('L',(10,6)),('A',(14,2),4,4,True),('L',(50,2)),('A',(54,6),4,4,True),('L',(54,42))]);join('paper','fold')
        for n,a,b in [('left',(22,48),(16,54)),('right',(42,48),(48,54))]:line('seam-'+n,a,b);join('seam-'+n,'fold')
