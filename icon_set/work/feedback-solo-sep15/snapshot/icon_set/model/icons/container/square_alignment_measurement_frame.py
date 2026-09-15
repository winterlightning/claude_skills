"""A rounded square measurement frame with two inward ticks per edge. Unifies the shorter and longer tick references.

Keyshape: SQUARE; centerline extremes recorded in build.
Construction reference: Lucide scan: repeated quarter-circle frame corners.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SquareAlignmentMeasurementFrame(Container64):
    icon_id = 'square-alignment-measurement-frame'
    keyshape = Keyshape.SQUARE
    aliases = ('square-grid-layout',)
    keywords = ('square', 'alignment', 'measurement', 'frame')

    def build(self) -> None:
        # Centerline (2,2)-(62,62).
        self.add_line('frame-top',(10,2),(54,2))
        self.add_arc('frame-ne',(54,2),(62,10),radius_x=8)
        self.add_line('frame-right',(62,10),(62,54))
        self.add_arc('frame-se',(62,54),(54,62),radius_x=8)
        self.add_line('frame-bottom',(54,62),(10,62))
        self.add_arc('frame-sw',(10,62),(2,54),radius_x=8)
        self.add_line('frame-left',(2,54),(2,10))
        self.add_arc('frame-nw',(2,10),(10,2),radius_x=8)
        self.add_contour('frame',*('frame-'+x for x in ('top','ne','right','se','bottom','sw','left','nw')),closed=True)
        for n,x in enumerate((22,42)):
            self.add_line(f'tick-top-{n}',(x,2),(x,10))
            self.add_line(f'tick-bottom-{n}',(x,54),(x,62))
            self.add_line(f'tick-left-{n}',(2,x),(10,x))
            self.add_line(f'tick-right-{n}',(54,x),(62,x))
            for side in ('top','bottom','left','right'):
                self.relate('connect',f'tick-{side}-{n}','frame')
