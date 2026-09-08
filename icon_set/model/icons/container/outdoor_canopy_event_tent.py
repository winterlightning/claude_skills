"""An event canopy has a peaked roof and tied-back side curtains.
Centerline extremes (2,2)-(62,62); square accommodates roof and opening.
Lucide tent informs the simple straight roof; the supplied reference supplies
curtains, rebuilt with mirrored elliptical arcs. No features omitted.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class OutdoorCanopyEventTent(Container64):
    icon_id = 'outdoor-canopy-event-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('outdoor', 'canopy', 'event', 'tent')

    def build(self) -> None:
        self.add_polyline('roof',(2,22),(32,2),(62,22))
        self.add_polyline('frame',(14,62),(2,62),(2,22),(62,22),(62,62),(50,62))
        self.relate('connect','roof','frame')
        for side in ('left','right'):
            def p(x,y):
                return (x if side=='left' else 64-x,y)
            self.add_arc(side+'-upper',p(20,22),p(2,44),radius_x=18,radius_y=22,sweep=side=='left')
            self.add_arc(side+'-lower',p(2,44),p(14,62),radius_x=12,radius_y=18,sweep=side=='left')
            self.add_contour(side+'-curtain',side+'-upper',side+'-lower')
            self.relate('connect',side+'-curtain','frame')
