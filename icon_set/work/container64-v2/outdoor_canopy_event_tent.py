"""An event canopy has a peaked roof and tied-back side curtains.
Centerline extremes (2,2)-(62,62); square accommodates roof and opening.
Lucide tent informs the simple straight roof; the supplied reference supplies
curtains, rebuilt with mirrored elliptical arcs. No features omitted.

Keyshape SQUARE; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (outdoor-canopy-event-tent SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

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
        self.add_line('roof-1', (6, 24), (32, 6))
        self.add_line('roof-2', (32, 6), (58, 24))
        self.add_line('frame-1', (16, 58), (6, 58))
        self.add_line('frame-2', (6, 58), (6, 24))
        self.add_line('frame-3', (6, 24), (58, 24))
        self.add_line('frame-4', (58, 24), (58, 58))
        self.add_line('frame-5', (58, 58), (48, 58))
        self.add_arc('left-upper', (22, 24), (6, 42), radius_x=16, radius_y=18)
        self.add_arc('left-lower', (6, 42), (16, 58), radius_x=10, radius_y=16)
        self.add_arc('right-upper', (42, 24), (58, 42), radius_x=16, radius_y=18, sweep=False)
        self.add_arc('right-lower', (58, 42), (48, 58), radius_x=10, radius_y=16, sweep=False)
        self.add_contour('roof', 'roof-1', 'roof-2')
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5')
        self.add_contour('left-curtain', 'left-upper', 'left-lower')
        self.add_contour('right-curtain', 'right-upper', 'right-lower')
        self.relate('connect', 'roof', 'frame')
        self.relate('connect', 'left-curtain', 'frame')
        self.relate('connect', 'right-curtain', 'frame')
