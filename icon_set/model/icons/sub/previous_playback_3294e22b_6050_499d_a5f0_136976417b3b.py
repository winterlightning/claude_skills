"""Previous Playback: A left-pointing outlined triangle sits beside a detached left chevron, both aligned across their centres. Generate this component alone; exclude Circle Frame.

Construction: A left triangle and separate left chevron keep the original ordering.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3294e22b-6050-499d-a5f0-136976417b3b'
SOURCE_PATH = 'pictographic-primitives/state/circle play backward_3294e22b-6050-499d-a5f0-136976417b3b.svg'
AUTHOR = 'gpt-6'


class PreviousPlayback(Sub32):
    icon_id = 'previous-playback'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('previous', 'playback', 'left', 'pointing', 'outlined', 'triangle', 'sits', 'beside')

    def build(self):
        self.add_polyline('chevron',(10,4),(2,16),(10,28))
        self.add_polyline('triangle',(30,4),(16,16),(30,28),closed=True)
