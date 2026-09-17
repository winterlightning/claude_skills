"""Arrow Counterclockwise: A broad curved arrow rises around the right side and ends in a left-pointing head at the top. Generate this component alone; exclude 75 Text.

Construction: The source upper-left head joins a top run and right return arc; keep its open lower end.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4b2c359b-884d-4e1a-9feb-4644db6c6829'
SOURCE_PATH = 'pictographic-primitives/state/rotate 75_4b2c359b-884d-4e1a-9feb-4644db6c6829.svg'
AUTHOR = 'gpt-6'


class ArrowCounterclockwiseState245(Sub32):
    icon_id = 'arrow-counterclockwise-state-245'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'counterclockwise', 'broad', 'curved', 'rises', 'around', 'right', 'side')

    def build(self):
        self.add_arc('curve',(16,30),(16,6),radius_x=14,radius_y=12,sweep=False)
        self.add_line('top',(16,6),(2,6))
        self.add_contour('shaft','curve','top')
        self.add_polyline('head',(6,2),(2,6),(6,10))
        self.relate('connect','shaft','head')
