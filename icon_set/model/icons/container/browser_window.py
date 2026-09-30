"""Taller browser body; retained the full title bar and its three indicators.
Independent review variant of browser-window. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 40]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (browser-window SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class BrowserWindowContainer(Container64):
    icon_id = 'browser-window'
    keyshape = Keyshape.SQUARE
    aliases = ('app-window', 'web-browser-window', 'window')
    keywords = ('browser', 'window', 'web', 'page', 'panel', 'interface', 'ui')

    def build(self) -> None:
        self.add_line('header-top', (10, 6), (54, 6))
        self.add_line('divider', (6, 22), (58, 22))
        self.add_arc('shoulder-nw-arc', (6, 10), (10, 6), radius_x=4)
        self.add_line('shoulder-nw-side', (6, 22), (6, 10))
        self.add_arc('shoulder-ne-arc', (54, 6), (58, 10), radius_x=4)
        self.add_line('shoulder-ne-side', (58, 10), (58, 22))
        self.add_line('body-right', (58, 22), (58, 54))
        self.add_arc('body-corner-se', (58, 54), (54, 58), radius_x=4)
        self.add_line('body-bottom', (54, 58), (10, 58))
        self.add_arc('body-corner-sw', (10, 58), (6, 54), radius_x=4)
        self.add_line('body-left', (6, 54), (6, 22))
        self.add_line('light-1', (15, 14), (17, 14))
        self.add_line('light-2', (23, 14), (25, 14))
        self.add_line('light-3', (32, 14), (34, 14))
        self.add_contour('shoulder-nw', 'shoulder-nw-side', 'shoulder-nw-arc')
        self.add_contour('shoulder-ne', 'shoulder-ne-arc', 'shoulder-ne-side')
        self.add_contour('body', 'body-right', 'body-corner-se', 'body-bottom', 'body-corner-sw', 'body-left')
        self.relate('connect', 'header-top', 'shoulder-nw')
        self.relate('connect', 'header-top', 'shoulder-ne')
        self.relate('connect', 'divider', 'shoulder-nw')
        self.relate('connect', 'divider', 'shoulder-ne')
        self.relate('connect', 'divider', 'body')
        self.relate('connect', 'body', 'shoulder-nw')
        self.relate('connect', 'body', 'shoulder-ne')
