"""A blank letter emerges from an open envelope with diagonal folds.
Centerline extremes (2,2)-(62,62); square fits the tall paper and envelope.
Lucide mail-open informs the rounded lower corners and connected diagonal
folds; both source renders establish the visible blank sheet. Mirrored in x.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart passes, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class OpenEnvelopeWithLetter(Container64):
    icon_id = 'open-envelope-with-letter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('open', 'envelope', 'with', 'letter')

    def build(self) -> None:
        self.add_line('side-right',(62,30),(62,56))
        self.add_arc('se',(62,56),(56,62),radius_x=6)
        self.add_line('bottom',(56,62),(8,62))
        self.add_arc('sw',(8,62),(2,56),radius_x=6)
        self.add_line('side-left',(2,56),(2,30))
        self.add_contour('envelope','side-right','se','bottom','sw','side-left')
        self.add_polyline('fold',(2,30),(22,44),(42,44),(62,30))
        self.relate('connect','envelope','fold')
        self.add_line('paper-left',(12,37),(12,6))
        self.add_arc('paper-nw',(12,6),(16,2),radius_x=4)
        self.add_line('paper-top',(16,2),(48,2))
        self.add_arc('paper-ne',(48,2),(52,6),radius_x=4)
        self.add_line('paper-right',(52,6),(52,37))
        self.add_contour('paper','paper-left','paper-nw','paper-top','paper-ne','paper-right')
        self.relate('connect','paper','fold')
        self.add_line('back-left',(2,30),(12,22))
        self.add_line('back-right',(52,22),(62,30))
        for side in ('left','right'):
            self.relate('connect','back-'+side,'paper')
            self.relate('connect','back-'+side,'envelope')
            self.relate('connect','back-'+side,'fold')
        self.add_line('seam-left',(22,44),(16,50))
        self.add_line('seam-right',(42,44),(48,50))
        self.relate('connect','seam-left','fold')
        self.relate('connect','seam-right','fold')
