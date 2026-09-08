"""An empty battery body has a connected rounded positive terminal.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide battery informs tangent quarter-circle body corners. The source supplies
the attached, outlined terminal. Centerline extremes (2,10)-(62,54).
The terminal intentionally extends rightward; no semantic detail removed.
Hosting measured with compose.py: plus does not pass, heart does not pass, check does not pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class EmptyBatteryLevelIndicator(Container64):
    icon_id = 'empty-battery-level-indicator'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('empty-battery', 'battery-container')
    keywords = ('battery', 'charge', 'empty', 'power')

    def build(self) -> None:
        self.add_line('body-top', (6, 10), (48, 10))
        self.add_arc('body-ne', (48, 10), (52, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_line('body-right', (52, 14), (52, 50))
        self.add_arc('body-se', (52, 50), (48, 54), radius_x=4, radius_y=4, sweep=True)
        self.add_line('body-bottom', (48, 54), (6, 54))
        self.add_arc('body-sw', (6, 54), (2, 50), radius_x=4, radius_y=4, sweep=True)
        self.add_line('body-left', (2, 50), (2, 14))
        self.add_arc('body-nw', (2, 14), (6, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('body', 'body-top', 'body-ne', 'body-right', 'body-se', 'body-bottom', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_line('terminal-top', (52, 24), (58, 24))
        self.add_arc('terminal-ne', (58, 24), (62, 28), radius_x=4, radius_y=4, sweep=True)
        self.add_line('terminal-right', (62, 28), (62, 36))
        self.add_arc('terminal-se', (62, 36), (58, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('terminal-bottom', (58, 40), (52, 40))
        self.add_contour('terminal', 'terminal-top', 'terminal-ne', 'terminal-right', 'terminal-se', 'terminal-bottom', closed=False)
        self.relate("connect", 'body', 'terminal')
