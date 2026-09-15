"""Pair of Paddles. Two equal oval heads and handles retain the source pair.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '147f327b-3496-428c-8373-84c03c8c062b'
SOURCE_PATH = 'pictographic-primitives/symbol/double paddle_147f327b-3496-428c-8373-84c03c8c062b.svg'
AUTHOR = 'gpt-6'


class PaddlesPair(Solo48):
    icon_id = 'paddles-pair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('paddles', 'table-tennis', 'ping-pong', 'rackets', 'maracas', 'sport', 'game', 'pair')

    def build(self) -> None:
        self.add_arc('left-head-right', (11, 8), (11, 28), radius_x=7, radius_y=10, sweep=True)
        self.add_arc('left-head-left', (11, 28), (11, 8), radius_x=7, radius_y=10, sweep=True)
        self.add_contour('left-head', 'left-head-right', 'left-head-left', closed=True)
        self.add_line('left-handle', (11, 28), (11, 40))
        self.relate("connect", 'left-head', 'left-handle')
        self.add_arc('right-head-right', (37, 8), (37, 28), radius_x=7, radius_y=10, sweep=True)
        self.add_arc('right-head-left', (37, 28), (37, 8), radius_x=7, radius_y=10, sweep=True)
        self.add_contour('right-head', 'right-head-right', 'right-head-left', closed=True)
        self.add_line('right-handle', (37, 28), (37, 40))
        self.relate("connect", 'right-head', 'right-handle')
