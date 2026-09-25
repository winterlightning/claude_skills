"""Circular Refresh Arrow: independently authored container.

Construction plan: Circular clockwise arrow with a broad open lower-right gap; retain source direction.
Keyshape CIRCLE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/synchronize refresh arrow_b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0.svg. Lucide refresh-cw original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize refresh arrow_b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0.svg'
AUTHOR = 'gpt-6'


class ClockwiseRefreshContainer(Container64):
    icon_id = 'clockwise-refresh-container'
    category = 'interface-essential'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('clockwise', 'refresh', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'ring',(32,62),[('A',(2,32),30,30,True),('A',(32,2),30,30,True),('A',(62,32),30,30,True)])
        poly('head',(50,24),(62,32),(54,42));join('head','ring')
