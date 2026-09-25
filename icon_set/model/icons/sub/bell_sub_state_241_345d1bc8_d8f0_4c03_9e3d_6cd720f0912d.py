"""Bell: A broad bell has a smoothly domed top, nearly upright sides, and a flared flat rim. A detached horizontal clapper sits below the centre of the rim.

Construction: The source bell has a plain domed crown, flared rim and detached short horizontal clapper, with no top knob.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '345d1bc8-d8f0-4c03-9e3d-6cd720f0912d'
SOURCE_PATH = 'pictographic-primitives/state/ring_345d1bc8-d8f0-4c03-9e3d-6cd720f0912d.svg'
AUTHOR = 'gpt-6'


class BellSubState241(Sub32):
    icon_id = 'bell-sub-state-241'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('bell', 'broad', 'smoothly', 'domed', 'top', 'nearly', 'upright', 'sides')

    def build(self):
        self.add_arc('crown',(6,12),(26,12),radius_x=10)
        points=[(26,12),(26,16),(30,22),(2,22),(6,16),(6,12)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'lower-{i}',a,b)
        self.add_contour('bell','crown',*(f'lower-{i}' for i in range(1,6)),closed=True)
        self.add_line('clapper',(12,30),(20,30))
