"""A lidded waste bin with a wide rim and rounded base. No extra ribs added.

Keyshape: VRECT_XL; centerline extremes recorded in build.
Construction reference: Lucide trash: shared rim, upright sides and equal quarter-circle base corners.. Mirrored about x=32.
Hosting measured with compose.py: plus review, heart review, check review.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-trash-bin VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleTrashBin(Container64):
    icon_id = 'simple-trash-bin'
    keyshape = Keyshape.VRECT_L
    aliases = ('simple-trash-bin-symbol',)
    keywords = ('simple', 'trash', 'bin')

    def build(self) -> None:
        # Body widened to 12..52 (was 15..49) under the full rim, so the bin holds a symbol of 28 with a 4 px gap
        # (was 22). Mirrored about x = 32.
        self.add_line('rim', (10, 14), (54, 14))
        self.add_line('handle-left', (25, 14), (25, 8))
        self.add_arc('handle-nw', (25, 8), (29, 4), radius_x=4)
        self.add_line('handle-top', (29, 4), (35, 4))
        self.add_arc('handle-ne', (35, 4), (39, 8), radius_x=4)
        self.add_line('handle-right', (39, 8), (39, 14))
        self.add_line('body-right', (52, 14), (52, 54))
        self.add_arc('body-se', (52, 54), (46, 60), radius_x=6)
        self.add_line('body-base', (46, 60), (18, 60))
        self.add_arc('body-sw', (18, 60), (12, 54), radius_x=6)
        self.add_line('body-left', (12, 54), (12, 14))
        self.add_contour('handle', 'handle-left', 'handle-nw', 'handle-top', 'handle-ne', 'handle-right')
        self.add_contour('body', 'body-right', 'body-se', 'body-base', 'body-sw', 'body-left')
        self.relate('connect', 'rim', 'body')
        self.relate('connect', 'rim', 'handle')
