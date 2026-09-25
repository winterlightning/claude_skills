"""Bell: A bell has a rounded crown with a small top knob, widening sides, and a flared straight lower rim. A tiny detached horizontal clapper appears beneath the centre.

Construction: The source bell keeps its crown knob, flared rim and detached short clapper.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec'
SOURCE_PATH = 'pictographic-primitives/state/notification_14b2c83a-b6f9-4186-8a3b-4d7a1895c6ec.svg'
AUTHOR = 'gpt-6'


class BellSubState187(Sub32):
    icon_id = 'bell-sub-state-187'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('bell', 'rounded', 'crown', 'small', 'top', 'knob', 'widening', 'sides')

    def build(self):
        self.add_arc('crown',(6,12),(26,12),radius_x=10,radius_y=8)
        points=[(26,12),(26,16),(30,22),(2,22),(6,16),(6,12)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'lower-{i}',a,b)
        self.add_contour('bell','crown',*(f'lower-{i}' for i in range(1,6)),closed=True)
        self.add_line('knob',(16,2),(16,4))
        self.relate('connect','bell','knob')
        self.add_line('clapper',(14,30),(18,30))
