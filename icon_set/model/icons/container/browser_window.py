"""Taller browser body; retained the full title bar and its three indicators.
Independent review variant of browser-window. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 40]. See container-fit-repair report for measured hosting results."""
from __future__ import annotations
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class BrowserWindowContainer(Container64):
    icon_id = 'browser-window'
    keyshape = Keyshape.SQUARE
    aliases = ('app-window', 'web-browser-window', 'window')
    keywords = ('browser', 'window', 'web', 'page', 'panel', 'interface', 'ui')

    def build(self) -> None:
        self.add_line('header-top', (6, 2), (58, 2))
        self.add_line('divider', (2, 18), (62, 18))
        self.add_arc('shoulder-nw-arc', (2, 6), (6, 2), radius_x=4)
        self.add_line('shoulder-nw-side', (2, 18), (2, 6))
        self.add_contour('shoulder-nw', 'shoulder-nw-side', 'shoulder-nw-arc')
        self.add_arc('shoulder-ne-arc', (58, 2), (62, 6), radius_x=4)
        self.add_line('shoulder-ne-side', (62, 6), (62, 18))
        self.add_contour('shoulder-ne', 'shoulder-ne-arc', 'shoulder-ne-side')
        self.add_line('body-right', (62, 18), (62, 58))
        self.add_arc('body-corner-se', (62, 58), (58, 62), radius_x=4)
        self.add_line('body-bottom', (58, 62), (6, 62))
        self.add_arc('body-corner-sw', (6, 62), (2, 58), radius_x=4)
        self.add_line('body-left', (2, 58), (2, 18))
        self.add_contour('body', 'body-right', 'body-corner-se', 'body-bottom', 'body-corner-sw', 'body-left')
        for first, second in (('header-top', 'shoulder-nw'), ('header-top', 'shoulder-ne'), ('divider', 'shoulder-nw'), ('divider', 'shoulder-ne'), ('divider', 'body'), ('body', 'shoulder-nw'), ('body', 'shoulder-ne')):
            self.relate('connect', first, second)
        self.add_line('light-1', (12, 10), (14, 10))
        self.add_line('light-2', (22, 10), (24, 10))
        self.add_line('light-3', (32, 10), (34, 10))
