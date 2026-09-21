"""Reduce the folded corner to leave the central paper area clear.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'a4b94225-2c9c-42ec-947b-c3b93395b100'
SOURCE_PATH = 'pictographic-primitives/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.svg'
AUTHOR = 'gpt-6'

class BottomFoldNoteContainer(Container64):
    icon_id = 'bottom-fold-note-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('paper',(2,2),(62,2),(62,50),(50,62),(2,62),closed=True)
        poly('fold',(50,62),(50,50),(62,50));join('fold','paper')
