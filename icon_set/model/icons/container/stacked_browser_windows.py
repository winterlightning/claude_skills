"""A browser window with a title bar overlaps a second window.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide panels-top-left: rounded frame and attached header divider.
Offset layers are deliberately asymmetric. Indicator row reduced to one short dash, shared across duplicate references.
Hosting (compose.py): plus passes, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class StackedBrowserWindows(Container64):
    icon_id = 'stacked-browser-windows'
    keyshape = Keyshape.SQUARE
    aliases = ('stacked-web-browser-windows',)
    keywords = ('stacked', 'browser', 'windows')

    def build(self) -> None:
        self.add_line('front-0', (16, 2), (56, 2))
        self.add_arc('front-1', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('front-2', (62, 8), (62, 46))
        self.add_arc('front-3', (62, 46), (56, 52), radius_x=6, radius_y=6, sweep=True)
        self.add_line('front-4', (56, 52), (16, 52))
        self.add_arc('front-5', (16, 52), (10, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('front-6', (10, 46), (10, 8))
        self.add_arc('front-7', (10, 8), (16, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('front', 'front-0', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', 'front-6', 'front-7', closed=True)
        self.add_line('divider', (10, 18), (62, 18))
        self.relate("connect", 'front', 'divider')
        self.add_line('indicator', (20, 10), (24, 10))
        self.add_line('back-0', (10, 14), (8, 14))
        self.add_arc('back-1', (8, 14), (2, 20), radius_x=6, radius_y=6, sweep=False)
        self.add_line('back-2', (2, 20), (2, 56))
        self.add_arc('back-3', (2, 56), (8, 62), radius_x=6, radius_y=6, sweep=False)
        self.add_line('back-4', (8, 62), (46, 62))
        self.add_arc('back-5', (46, 62), (52, 56), radius_x=6, radius_y=6, sweep=False)
        self.add_line('back-6', (52, 56), (52, 52))
        self.add_contour('back', 'back-0', 'back-1', 'back-2', 'back-3', 'back-4', 'back-5', 'back-6', closed=False)
        self.relate("connect", 'back', 'front')
