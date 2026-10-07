"""Taller screen with a compact separate keyboard; keep the inter-object gap.
Independent CONTAINER64 revision, 4-unit strokes. Lucide monitor/presentation construction retained. Hosting results in container-fit-repair report.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (monitor-keyboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class MonitorKeyboard(Container64):
    icon_id = 'monitor-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('computer-monitor-and-keyboard',)
    keywords = ('monitor', 'keyboard')

    def build(self) -> None:
        # Screen 6..42 (was 6..40) with the keyboard 8 below it (50..58), so the screen holds a symbol of 24 with
        # a 4 px gap (was 22). Mirrored about x = 32.
        self.add_line('screen0', (10, 6), (54, 6))
        self.add_arc('screen1', (54, 6), (58, 10), radius_x=4)
        self.add_line('screen2', (58, 10), (58, 38))
        self.add_arc('screen3', (58, 38), (54, 42), radius_x=4)
        self.add_line('screen4', (54, 42), (10, 42))
        self.add_arc('screen5', (10, 42), (6, 38), radius_x=4)
        self.add_line('screen6', (6, 38), (6, 10))
        self.add_arc('screen7', (6, 10), (10, 6), radius_x=4)
        self.add_line('keyboard-1', (14, 50), (50, 50))
        self.add_line('keyboard-2', (50, 50), (56, 58))
        self.add_line('keyboard-3', (56, 58), (8, 58))
        self.add_line('keyboard-4', (8, 58), (14, 50))
        self.add_contour('screen', 'screen0', 'screen1', 'screen2', 'screen3', 'screen4', 'screen5', 'screen6', 'screen7', closed=True)
        self.add_contour('keyboard', 'keyboard-1', 'keyboard-2', 'keyboard-3', 'keyboard-4', closed=True)
