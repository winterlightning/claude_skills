"""An empty battery body has a connected rounded positive terminal.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide battery informs tangent quarter-circle body corners. The source supplies
the attached, outlined terminal. Centerline extremes (2,10)-(62,54).
The terminal intentionally extends rightward; no semantic detail removed.
Hosting measured with compose.py: plus does not pass, heart does not pass, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (empty-battery-level-indicator HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class EmptyBatteryLevelIndicator(Container64):
    icon_id = 'empty-battery-level-indicator'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('empty-battery', 'battery-container')
    keywords = ('battery', 'charge', 'empty', 'power')

    def build(self) -> None:
        self.add_line('body-top', (8, 12), (46, 12))
        self.add_arc('body-ne', (46, 12), (50, 16), radius_x=4)
        self.add_line('body-right', (50, 16), (50, 48))
        self.add_arc('body-se', (50, 48), (46, 52), radius_x=4)
        self.add_line('body-bottom', (46, 52), (8, 52))
        self.add_arc('body-sw', (8, 52), (4, 48), radius_x=4)
        self.add_line('body-left', (4, 48), (4, 16))
        self.add_arc('body-nw', (4, 16), (8, 12), radius_x=4)
        self.add_line('terminal-top', (50, 24), (56, 24))
        self.add_arc('terminal-ne', (56, 24), (60, 28), radius_x=4)
        self.add_line('terminal-right', (60, 28), (60, 36))
        self.add_arc('terminal-se', (60, 36), (56, 40), radius_x=4)
        self.add_line('terminal-bottom', (56, 40), (50, 40))
        self.add_contour('body', 'body-top', 'body-ne', 'body-right', 'body-se', 'body-bottom', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_contour('terminal', 'terminal-top', 'terminal-ne', 'terminal-right', 'terminal-se', 'terminal-bottom')
        self.relate('connect', 'body', 'terminal')
