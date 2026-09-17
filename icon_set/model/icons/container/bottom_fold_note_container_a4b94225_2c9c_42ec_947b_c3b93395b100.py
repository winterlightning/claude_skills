"""Square Note with Folded Corner: independently authored container.

Construction plan: Square note with a folded lower-right corner; diagonal intentionally asymmetric.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.svg. Lucide file-stack original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
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
    keywords = ('bottom', 'fold', 'note', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('paper',(2,2),(62,2),(62,40),(40,62),(2,62),closed=True)
        poly('fold',(40,62),(40,40),(62,40));join('fold','paper')
