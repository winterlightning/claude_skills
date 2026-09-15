"""An empty upward triangle enclosure.

Keyshape HRECT_XL: (0, 4, 64, 60); chosen for the reference silhouette.
Construction reference: Lucide triangle: mirrored sloping sides and a horizontal base. Original and atomic-debug inspected.
Source sharp vertices retained as round stroke joins; 60 by 52 centerlines approximate an equilateral triangle.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class UpwardPointingTriangleSymbol(Container64):
    icon_id = 'upward-pointing-triangle-symbol'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('upward', 'pointing', 'triangle', 'symbol')

    def build(self) -> None:
        self.add_polyline('outline', (32, 6), (62, 58), (2, 58), closed=True)
