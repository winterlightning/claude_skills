"""A square browser window with a divider and two header marks.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: app-window: rounded frame and straight title-bar divider; source uses two dashes. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (web-browser-window SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class WebBrowserWindow(Container64):
    icon_id = 'web-browser-window'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('web', 'browser', 'window')

    def build(self) -> None:
        self.add_line('top-0', (6, 22), (6, 12))
        self.add_arc('top-1', (6, 12), (12, 6), radius_x=6)
        self.add_line('top-2', (12, 6), (52, 6))
        self.add_arc('top-3', (52, 6), (58, 12), radius_x=6)
        self.add_line('top-4', (58, 12), (58, 22))
        self.add_line('divider', (6, 22), (58, 22))
        self.add_line('body-0', (58, 22), (58, 52))
        self.add_arc('body-1', (58, 52), (52, 58), radius_x=6)
        self.add_line('body-2', (52, 58), (12, 58))
        self.add_arc('body-3', (12, 58), (6, 52), radius_x=6)
        self.add_line('body-4', (6, 52), (6, 22))
        self.add_line('indicator-one', (16, 14), (18, 14))
        self.add_line('indicator-two', (28, 14), (30, 14))
        self.add_contour('top', 'top-0', 'top-1', 'top-2', 'top-3', 'top-4')
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4')
        self.relate('connect', 'top', 'divider')
        self.relate('connect', 'body', 'divider')
        self.relate('connect', 'top', 'body')
