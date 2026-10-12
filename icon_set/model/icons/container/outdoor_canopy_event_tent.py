"""An event canopy has a peaked roof and tied-back side curtains.
Centerline extremes (2,2)-(62,62); square accommodates roof and opening.
Lucide tent informs the simple straight roof; the supplied reference supplies
curtains, rebuilt with mirrored elliptical arcs. No features omitted.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (outdoor-canopy-event-tent SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class OutdoorCanopyEventTent(Container64):
    icon_id = 'outdoor-canopy-event-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('outdoor', 'canopy', 'event', 'tent')

    def build(self) -> None:
        # Lower roof (6..20, was 6..24) and curtains tied back 6 from the poles (open at the foot, so nothing
        # closes between curtain and pole), so the opening holds a symbol
        # of 24 with a 4 px gap (was 20). Mirrored about x = 32.
        self.add_line('roof-1', (6, 20), (32, 6))
        self.add_line('roof-2', (32, 6), (58, 20))
        self.add_line('frame-2', (6, 58), (6, 20))
        self.add_line('frame-3', (6, 20), (58, 20))
        self.add_line('frame-4', (58, 20), (58, 58))
        self.add_arc('left-upper', (16, 20), (12, 39), radius_x=24)
        self.add_arc('left-lower', (12, 39), (16, 58), radius_x=24)
        self.add_arc('right-upper', (48, 20), (52, 39), radius_x=24, sweep=False)
        self.add_arc('right-lower', (52, 39), (48, 58), radius_x=24, sweep=False)
        self.add_contour('roof', 'roof-1', 'roof-2')
        self.add_contour('frame', 'frame-2', 'frame-3', 'frame-4')
        self.add_contour('left-curtain', 'left-upper', 'left-lower')
        self.add_contour('right-curtain', 'right-upper', 'right-lower')
        self.relate('connect', 'roof', 'frame')
        self.relate('connect', 'left-curtain', 'frame')
        self.relate('connect', 'right-curtain', 'frame')
