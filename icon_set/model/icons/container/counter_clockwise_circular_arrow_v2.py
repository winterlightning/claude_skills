# Variant of counter-clockwise-circular-arrow; parent file remains unchanged.
"""An open circular arrow used as an enclosing container.

User explicitly confirmed the container family for this batch reference.
CIRCLE: visible radius 32 about (32,32). The loop has radius 24 about
(38,32), reaching x=62. A wider downward chevron extends visibly beyond
the left of the loop. Deliberate rightward offset leaves room for the head.
Lucide rotate-ccw informs the single circular sweep and attached chevron.
Hosting measured with compose.py: plus invalid, heart review, check invalid.
No semantic detail was dropped. Geometry is authored directly on CONTAINER64.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class CounterClockwiseCircularArrowVariant2(Container64):
    icon_id = 'counter-clockwise-circular-arrow-v2'
    variant_of = 'counter-clockwise-circular-arrow'
    variant_label = 'Prominent outer arrowhead'
    keyshape = Keyshape.CIRCLE
    aliases = ('counterclockwise-arrow-container', 'circular-arrow-container')
    keywords = ('circular', 'arrow', 'counterclockwise', 'ring', 'refresh', 'undo')

    def build(self) -> None:
        self.add_arc('loop', (38, 56), (14, 32), radius_x=24, large_arc=True, sweep=False)
        self.add_polyline('arrowhead', (4, 22), (14, 32), (24, 22))
        self.relate('connect', 'loop', 'arrowhead')
