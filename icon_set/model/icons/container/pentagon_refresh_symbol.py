"""A pentagonal enclosure whose upper right edge ends in a clockwise arrow.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide pentagon informs the coherent five-sided outline.
The opening and arrow create intentional directional asymmetry; rounded joins retain deliberate polygon corners.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (pentagon-refresh-symbol SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class PentagonRefreshSymbol(Container64):
    icon_id = 'pentagon-refresh-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('pentagon', 'refresh', 'symbol')

    def build(self) -> None:
        self.add_line('perimeter-1', (52, 20), (58, 27))
        self.add_line('perimeter-2', (58, 27), (48, 58))
        self.add_line('perimeter-3', (48, 58), (16, 58))
        self.add_line('perimeter-4', (16, 58), (6, 27))
        self.add_line('perimeter-5', (6, 27), (32, 6))
        self.add_line('perimeter-6', (32, 6), (46, 16))
        self.add_line('arrowhead-1', (38, 16), (46, 16))
        self.add_line('arrowhead-2', (46, 16), (44, 8))
        self.add_contour('perimeter', 'perimeter-1', 'perimeter-2', 'perimeter-3', 'perimeter-4', 'perimeter-5', 'perimeter-6')
        self.add_contour('arrowhead', 'arrowhead-1', 'arrowhead-2')
        self.relate('connect', 'perimeter', 'arrowhead')
