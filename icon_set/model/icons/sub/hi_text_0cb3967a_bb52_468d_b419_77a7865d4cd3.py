"""HI Text: The uppercase letters HI stand side by side, with two uprights joined by a central crossbar in the H and a plain vertical I. Generate this component alone; exclude Round Speech Bubble.

Construction: An uppercase H and plain I retain their separate vertical stems.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0cb3967a-bb52-468d-b419-77a7865d4cd3'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble round hi_0cb3967a-bb52-468d-b419-77a7865d4cd3.svg'
AUTHOR = 'gpt-6'


class HiText(Sub32):
    icon_id = 'hi-text'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('hi', 'text', 'uppercase', 'letters', 'stand', 'side', 'uprights', 'joined')

    def build(self):
        self.add_line('h-left',(2,4),(2,28))
        self.add_line('h-right',(16,4),(16,28))
        self.add_line('h-bar',(2,16),(16,16))
        self.relate('connect','h-left','h-bar')
        self.relate('connect','h-right','h-bar')
        self.add_line('i',(30,4),(30,28))
