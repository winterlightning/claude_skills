"""A square browser window with a divider and two header marks.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: app-window: rounded frame and straight title-bar divider; source uses two dashes. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class WebBrowserWindow(Container64):
    icon_id = 'web-browser-window'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('web', 'browser', 'window')

    def build(self) -> None:
        self.add_line('top-0', (2, 18), (2, 8))
        self.add_arc('top-1', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_line('top-2', (8, 2), (56, 2))
        self.add_arc('top-3', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('top-4', (62, 8), (62, 18))
        self.add_contour('top', 'top-0', 'top-1', 'top-2', 'top-3', 'top-4', closed=False)
        self.add_line('divider', (2, 18), (62, 18))
        self.add_line('body-0', (62, 18), (62, 56))
        self.add_arc('body-1', (62, 56), (56, 62), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-2', (56, 62), (8, 62))
        self.add_arc('body-3', (8, 62), (2, 56), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-4', (2, 56), (2, 18))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', closed=False)
        self.relate("connect", 'top', 'divider')
        self.relate("connect", 'body', 'divider')
        self.relate("connect", 'top', 'body')
        self.add_line('indicator-one', (12, 10), (14, 10))
        self.add_line('indicator-two', (28, 10), (30, 10))
