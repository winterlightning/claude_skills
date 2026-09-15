"""A pointed fabric pennant hanging from a rod and triangular cord.

VRECT_L: visible (8, 0, 56, 64); centerline (10, 2)-(54, 62).
Reference: batch_05 source render. Lucide pentagon closed angular construction informs the tapered lower field..
Angular fabric folds use round stroke joins; no ornament added.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class HangingPennantBanner(Container64):
    icon_id = "hanging-pennant-banner"
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('hanging', 'pennant', 'banner')

    def build(self) -> None:
        self.add_line('rod', (10, 14), (54, 14))
        self.add_polyline('cord', (14, 14), (32, 2), (50, 14), closed=False)
        self.add_polyline('banner', (14, 14), (14, 48), (32, 62), (50, 48), (50, 14), closed=False)
        self.relate("connect", 'rod', 'cord')
        self.relate("connect", 'rod', 'banner')
        self.relate("connect", 'cord', 'banner')
