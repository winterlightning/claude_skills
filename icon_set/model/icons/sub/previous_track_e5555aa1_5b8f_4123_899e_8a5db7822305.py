"""Previous Track: A left-pointing outlined triangle sits beside a detached vertical stop bar on its left. Generate this component alone; exclude Circle Frame.

Construction: A detached left stop bar precedes a left-facing outlined triangle.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e5555aa1-5b8f-4123-899e-8a5db7822305'
SOURCE_PATH = 'pictographic-primitives/state/previous circle_e5555aa1-5b8f-4123-899e-8a5db7822305.svg'
AUTHOR = 'gpt-6'


class PreviousTrack(Sub32):
    icon_id = 'previous-track'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('previous', 'track', 'left', 'pointing', 'outlined', 'triangle', 'sits', 'beside')

    def build(self):
        self.add_line('stop',(2,4),(2,28))
        self.add_polyline('play',(30,6),(12,16),(30,26),closed=True)
