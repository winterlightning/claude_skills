"""A lidded waste bin with a wide rim and rounded base. No extra ribs added.

Keyshape: VRECT_XL; centerline extremes recorded in build.
Construction reference: Lucide trash: shared rim, upright sides and equal quarter-circle base corners.. Mirrored about x=32.
Hosting measured with compose.py: plus review, heart review, check review.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SimpleTrashBin(Container64):
    icon_id = 'simple-trash-bin'
    keyshape = Keyshape.VRECT_XL
    aliases = ('simple-trash-bin-symbol',)
    keywords = ('simple', 'trash', 'bin')

    def build(self) -> None:
        # Centerline (6,2)-(58,62).
        self.add_line('rim',(6,12),(58,12))
        self.add_line('handle-left',(22,12),(22,6))
        self.add_arc('handle-nw',(22,6),(26,2),radius_x=4)
        self.add_line('handle-top',(26,2),(38,2))
        self.add_arc('handle-ne',(38,2),(42,6),radius_x=4)
        self.add_line('handle-right',(42,6),(42,12))
        self.add_contour('handle','handle-left','handle-nw','handle-top','handle-ne','handle-right')
        self.add_line('body-right',(52,12),(52,56))
        self.add_arc('body-se',(52,56),(46,62),radius_x=6)
        self.add_line('body-base',(46,62),(18,62))
        self.add_arc('body-sw',(18,62),(12,56),radius_x=6)
        self.add_line('body-left',(12,56),(12,12))
        self.add_contour('body','body-right','body-se','body-base','body-sw','body-left')
        self.relate('connect','rim','body')
        self.relate('connect','rim','handle')
