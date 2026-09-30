"""circle-check-symbol24: SYMBOL24 redraw of `circular-check-mark-symbol-sub32-symbol`.

Started from `symbol24.py from32` (every coordinate x 3/4, rounded toward the
centre). The 4-unit stroke does not scale, so gaps shrink; rebalance the drawing
at 24 and judge it visually before calling it done.
"""
from ...keyshapes import Keyshape
from ._base import Symbol24

SOURCE_ICON_ID = 'e827e098-b2c1-4c9d-a347-ed197ce977ef'
SOURCE_PATH = 'pictographic-primitives/other/circle check 1_e827e098-b2c1-4c9d-a347-ed197ce977ef.svg'
AUTHOR = 'claude-opus-5-5'
DERIVED_FROM_32 = 'circular-check-mark-symbol-sub32-symbol'


class CircleCheckSymbol24(Symbol24):
    icon_id = 'circle-check-symbol24'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'done', 'success', 'circular check mark')

    def build(self) -> None:
        self.add_arc('open-circle', (22, 12), (12, 2), radius_x=10, large_arc=True, sweep=True)
        # Both arms at 45 degrees (Lucide circle-check); the tip stops short of the
        # arc end so the opening still reads at 24 px.
        self.add_line('check-1', (8, 12), (11, 15))
        self.add_line('check-2', (11, 15), (18, 8))
        self.add_contour('check', 'check-1', 'check-2')
