"""A desktop display stands above a broad trapezoidal keyboard.

Keyshape SQUARE: visible extremes (0, 0, 48, 48).
Lucide monitor: rounded screen and centered stand. Drop chin stripe and replace splayed legs with a clear single post to preserve the separate keyboard at native size."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42b12fe3-b736-5239-ab2e-91d8f0f66555'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/desktop monitor keyboard_42b12fe3-b736-5239-ab2e-91d8f0f66555.svg'
AUTHOR = 'astra-chatgpt'


class MonitorWithDeskKeyboard(Solo48):
    icon_id = 'monitor-with-desk-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('monitor', 'keyboard', 'desktop', 'computer', 'workstation', 'screen', 'typing', 'pc')

    def build(self) -> None:
        self.add_line('screen-top0', (6, 2), (42, 2))
        self.add_arc('screen-ne', (42, 2), (46, 6), radius_x=4, sweep=True)
        self.add_line('screen-right', (46, 6), (46, 25))
        self.add_arc('screen-se', (46, 25), (42, 29), radius_x=4, sweep=True)
        self.add_line('screen-bottom0', (42, 29), (24, 29))
        self.add_line('screen-bottom1', (24, 29), (6, 29))
        self.add_arc('screen-sw', (6, 29), (2, 25), radius_x=4, sweep=True)
        self.add_line('screen-left', (2, 25), (2, 6))
        self.add_arc('screen-nw', (2, 6), (6, 2), radius_x=4, sweep=True)
        self.add_contour('screen', 'screen-top0', 'screen-ne', 'screen-right', 'screen-se', 'screen-bottom0', 'screen-bottom1', 'screen-sw', 'screen-left', 'screen-nw', closed=True)
        self.add_line('stand', (24, 29), (24, 36))
        self.relate("connect", 'screen', 'stand')
        self.add_polyline('keyboard', (8, 36), (24, 36), (40, 36), (44, 46), (4, 46), closed=True)
        self.relate("connect", 'stand', 'keyboard')
