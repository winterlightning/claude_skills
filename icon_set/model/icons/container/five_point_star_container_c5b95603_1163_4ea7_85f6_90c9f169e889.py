"""Five Pointed Star Symbol: independently authored container.

Construction plan: One five-point outline, mirrored about the vertical axis; no inner symbol.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg. Lucide star original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'c5b95603-1163-4ea7-85f6-90c9f169e889'
SOURCE_PATH = 'pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg'
AUTHOR = 'gpt-6'


class FivePointStarContainer(Container64):
    icon_id = 'five-point-star-container'
    category = 'holidays'
    categories = ('holidays', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('five', 'point', 'star', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('star',(32,2),(40,24),(62,24),(44,38),(50,62),(32,48),(14,62),(20,38),(2,24),(24,24),closed=True)
