"""A blank presentation panel with a single tray and two straight legs.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide presentation informs the open panel and projecting horizontal tray.
Kept the reference single tray and omitted no identity detail; paired legs mirror about x=32.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (presentation-board-on-stand SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class PresentationBoardOnStand(Container64):
    icon_id = 'presentation-board-on-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('presentation', 'board', 'on', 'stand')

    def build(self) -> None:
        self.add_line('left-side', (10, 42), (10, 12))
        self.add_arc('corner-nw', (10, 12), (16, 6), radius_x=6)
        self.add_line('top', (16, 6), (48, 6))
        self.add_arc('corner-ne', (48, 6), (54, 12), radius_x=6)
        self.add_line('right-side', (54, 12), (54, 42))
        self.add_line('tray', (6, 42), (58, 42))
        self.add_line('leg-left', (10, 42), (10, 58))
        self.add_line('leg-right', (54, 42), (54, 58))
        self.add_contour('panel', 'left-side', 'corner-nw', 'top', 'corner-ne', 'right-side')
        self.relate('connect', 'panel', 'tray')
        self.relate('connect', 'panel', 'leg-left')
        self.relate('connect', 'panel', 'leg-right')
        self.relate('connect', 'tray', 'leg-left')
        self.relate('connect', 'tray', 'leg-right')
