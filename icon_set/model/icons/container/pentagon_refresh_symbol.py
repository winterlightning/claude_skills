"""A pentagonal enclosure whose upper right edge ends in a clockwise arrow.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide pentagon informs the coherent five-sided outline.
The opening and arrow create intentional directional asymmetry; rounded joins retain deliberate polygon corners.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class PentagonRefreshSymbol(Container64):
    icon_id = 'pentagon-refresh-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('pentagon', 'refresh', 'symbol')

    def build(self) -> None:
        self.add_polyline('perimeter', (54, 18), (62, 25), (50, 62), (14, 62), (2, 25), (32, 2), (48, 14), closed=False)
        self.add_polyline('arrowhead', (38, 14), (48, 14), (46, 4), closed=False)
        self.relate("connect", 'perimeter', 'arrowhead')
