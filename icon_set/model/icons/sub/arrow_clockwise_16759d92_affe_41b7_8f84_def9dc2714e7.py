"""Arrow Clockwise: A broad curved arrow sweeps around the left side and ends pointing right across the top. Generate this component alone; exclude 60 Text.

Construction: A left half-circle flows into top and bottom horizontal terminals; the top ends with a right head.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '16759d92-affe-41b7-8f84-def9dc2714e7'
SOURCE_PATH = 'pictographic-primitives/state/rotate 60_16759d92-affe-41b7-8f84-def9dc2714e7.svg'
AUTHOR = 'gpt-6'


class ArrowClockwise(Sub32):
    icon_id = 'arrow-clockwise'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'clockwise', 'broad', 'curved', 'sweeps', 'around', 'left', 'side')

    def build(self):
        self.add_line('bottom',(26,30),(16,30))
        self.add_arc('curve',(16,30),(16,6),radius_x=14,radius_y=12)
        self.add_line('top',(16,6),(30,6))
        self.add_contour('sweep','bottom','curve','top')
        self.add_polyline('head',(26,2),(30,6),(26,10))
        self.relate('connect','sweep','head')
