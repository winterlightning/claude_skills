"""Taller screen with a compact separate keyboard; keep the inter-object gap.
Independent CONTAINER64 revision, 4-unit strokes. Lucide monitor/presentation construction retained. Hosting results in container-fit-repair report.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (monitor-keyboard SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

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
        self.add_line('screen0', (10, 6), (54, 6))
        self.add_arc('screen1', (54, 6), (58, 10), radius_x=4)
        self.add_line('screen2', (58, 10), (58, 36))
        self.add_arc('screen3', (58, 36), (54, 40), radius_x=4)
        self.add_line('screen4', (54, 40), (10, 40))
        self.add_arc('screen5', (10, 40), (6, 36), radius_x=4)
        self.add_line('screen6', (6, 36), (6, 10))
        self.add_arc('screen7', (6, 10), (10, 6), radius_x=4)
        self.add_line('keyboard-1', (14, 48), (50, 48))
        self.add_line('keyboard-2', (50, 48), (56, 58))
        self.add_line('keyboard-3', (56, 58), (8, 58))
        self.add_line('keyboard-4', (8, 58), (14, 48))
        self.add_contour('screen', 'screen0', 'screen1', 'screen2', 'screen3', 'screen4', 'screen5', 'screen6', 'screen7', closed=True)
        self.add_contour('keyboard', 'keyboard-1', 'keyboard-2', 'keyboard-3', 'keyboard-4', closed=True)
