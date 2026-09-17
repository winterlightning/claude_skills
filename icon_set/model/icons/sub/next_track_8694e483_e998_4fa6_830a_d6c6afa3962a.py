"""Next Track: A right-pointing outlined triangle sits beside a detached vertical stop bar, with the bar extending slightly beyond the triangle's height. Generate this component alone; exclude Circle Frame.

Construction: A right outlined triangle precedes one detached stop bar.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8694e483-e998-4fa6-830a-d6c6afa3962a'
SOURCE_PATH = 'pictographic-primitives/state/next circle_8694e483-e998-4fa6-830a-d6c6afa3962a.svg'
AUTHOR = 'gpt-6'


class NextTrack(Sub32):
    icon_id = 'next-track'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('next', 'track', 'right', 'pointing', 'outlined', 'triangle', 'sits', 'beside')

    def build(self):
        self.add_polyline('play',(2,6),(20,16),(2,26),closed=True)
        self.add_line('stop',(30,4),(30,28))
