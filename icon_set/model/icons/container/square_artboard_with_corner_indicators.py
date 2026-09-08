"""A square artboard surrounded by eight detached crop indicators. Keeps the sharp working-area corners.

Keyshape: SQUARE; centerline extremes recorded in build.
Construction reference: Lucide scan: balanced detached corner furniture, preserving the source straight marks.. Mirrored about x=32.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SquareArtboardWithCornerIndicators(Container64):
    icon_id = 'square-artboard-with-corner-indicators'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'artboard', 'with', 'corner', 'indicators')

    def build(self) -> None:
        # Centerline (2,2)-(62,62).
        self.add_polyline('artboard',(13,13),(51,13),(51,51),(13,51),closed=True)
        for n,p in enumerate((13,51)):
            self.add_line(f'top-{n}',(p,2),(p,5))
            self.add_line(f'bottom-{n}',(p,59),(p,62))
            self.add_line(f'left-{n}',(2,p),(5,p))
            self.add_line(f'right-{n}',(59,p),(62,p))
