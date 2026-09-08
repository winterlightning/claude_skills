"""Two inward-facing brackets enclose a tall content area.
Centerline extremes (2,2)-(62,62); square fit follows the wider reference.
Lucide brackets informs equal quarter-circle corners and mirrored terminals.
Both source references consolidated; no semantic detail omitted.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class PairOfSquareBrackets(Container64):
    icon_id = 'pair-of-square-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('pair', 'of', 'square', 'brackets')

    def build(self) -> None:
        for side in ('left','right'):
            def p(x,y):
                return (x if side == 'left' else 64-x,y)
            self.add_line(side+'-top', p(10,2), p(6,2))
            self.add_arc(side+'-upper', p(6,2), p(2,6), radius_x=4, sweep=side=='right')
            self.add_line(side+'-spine', p(2,6), p(2,58))
            self.add_arc(side+'-lower', p(2,58), p(6,62), radius_x=4, sweep=side=='right')
            self.add_line(side+'-bottom', p(6,62), p(10,62))
            self.add_contour(side, *(side+'-'+s for s in ('top','upper','spine','lower','bottom')))
