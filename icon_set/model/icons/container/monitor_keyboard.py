"""Taller screen with a compact separate keyboard; keep the inter-object gap.
Independent CONTAINER64 revision, 4-unit strokes. Lucide monitor/presentation construction retained. Hosting results in container-fit-repair report."""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class MonitorKeyboard(Container64):
    icon_id = 'monitor-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ('computer-monitor-and-keyboard',)
    keywords = ('monitor', 'keyboard')

    def build(self) -> None:
        self.add_line('screen0', (6, 2), (58, 2))
        self.add_arc('screen1', (58, 2), (62, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen2', (62, 6), (62, 40))
        self.add_arc('screen3', (62, 40), (58, 44), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen4', (58, 44), (6, 44))
        self.add_arc('screen5', (6, 44), (2, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen6', (2, 40), (2, 6))
        self.add_arc('screen7', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('screen', 'screen0', 'screen1', 'screen2', 'screen3', 'screen4', 'screen5', 'screen6', 'screen7', closed=True)
        self.add_polyline('keyboard', (10, 52), (54, 52), (60, 62), (4, 62), closed=True)
SOURCE_ICON_ID = None
SOURCE_PATH = None
