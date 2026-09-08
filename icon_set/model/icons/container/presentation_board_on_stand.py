"""A blank presentation panel with a single tray and two straight legs.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide presentation informs the open panel and projecting horizontal tray.
Kept the reference single tray and omitted no identity detail; paired legs mirror about x=32.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class PresentationBoardOnStand(Container64):
    icon_id = 'presentation-board-on-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('presentation', 'board', 'on', 'stand')

    def build(self) -> None:
        self.add_line('left-side', (6, 44), (6, 8))
        self.add_arc('corner-nw', (6, 8), (12, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_line('top', (12, 2), (52, 2))
        self.add_arc('corner-ne', (52, 2), (58, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('right-side', (58, 8), (58, 44))
        self.add_contour('panel', 'left-side', 'corner-nw', 'top', 'corner-ne', 'right-side', closed=False)
        self.add_line('tray', (2, 44), (62, 44))
        self.add_line('leg-left', (6, 44), (6, 62))
        self.add_line('leg-right', (58, 44), (58, 62))
        self.relate("connect", 'panel', 'tray')
        self.relate("connect", 'panel', 'leg-left')
        self.relate("connect", 'panel', 'leg-right')
        self.relate("connect", 'tray', 'leg-left')
        self.relate("connect", 'tray', 'leg-right')
