"""Travel Suitcase with Wheels: independently authored container.

Construction plan: Rounded suitcase, centered handle and two matching short wheels.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg. Lucide luggage original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'
AUTHOR = 'gpt-6'


class WheeledSuitcaseContainer(Container64):
    icon_id = 'wheeled-suitcase-container'
    category = 'travel'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('wheeled', 'suitcase', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'case',2,14,62,54,6)
        path(self,'handle',(22,14),[('L',(22,6)),('A',(26,2),4,4,True),('L',(38,2)),('A',(42,6),4,4,True),('L',(42,14))]);join('handle','case')
        for x in (16,48):line(f'wheel-{x}',(x,54),(x,62));join('case',f'wheel-{x}')
