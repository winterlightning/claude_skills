"""Letter A: An uppercase A has two sloping sides meeting at a softly rounded apex and a horizontal crossbar. Generate this component alone; exclude Circle Frame.

Construction: Two mirrored sloping stems and a crossbar sharing exact points on the stems.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '892ef37d-05df-4d38-ac5b-1bfa3f406d52'
SOURCE_PATH = 'pictographic-primitives/state/a text in circle_892ef37d-05df-4d38-ac5b-1bfa3f406d52.svg'
AUTHOR = 'gpt-6'


class LetterASub(Sub32):
    icon_id = 'letter-a-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'uppercase', 'sloping', 'sides', 'meeting', 'softly', 'rounded', 'apex')

    def build(self):
        self.add_polyline('a',(2,30),(16,2),(30,30))
        self.add_line('bar',(8,18),(24,18))
        self.relate('connect','a','bar')
