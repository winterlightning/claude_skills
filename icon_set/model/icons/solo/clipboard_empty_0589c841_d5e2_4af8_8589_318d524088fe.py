"""Clipboard. Enlarges the clip opening to survive the stroke weight; leaves the board empty.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide clipboard: an open board perimeter meets a rounded top clip; supplied reference sets the round clip shape.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0589c841-d5e2-4af8-8589-318d524088fe'
SOURCE_PATH = 'pictographic-primitives/symbol/clipboard_0589c841-d5e2-4af8-8589-318d524088fe.svg'
AUTHOR = 'gpt-6'


class ClipboardEmpty(Solo48):
    icon_id = 'clipboard-empty'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('clipboard', 'board', 'notes', 'document', 'list', 'paper', 'office', 'task')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_arc('clip-top', (16, 12), (32, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('clip-bottom', (32, 12), (16, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('clip', 'clip-top', 'clip-bottom', closed=True)
        self.add_line('top-right', (32, 12), (36, 12))
        self.add_arc('ne', (36, 12), (40, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right', (40, 16), (40, 40))
        self.add_arc('se', (40, 40), (36, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (36, 44), (12, 44))
        self.add_arc('sw', (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (8, 40), (8, 16))
        self.add_arc('nw', (8, 16), (12, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('top-left', (12, 12), (16, 12))
        self.add_contour('board', 'top-right', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', 'top-left')
        self.relate("connect", 'clip', 'board')
