"""Check Mark: A check mark has a short descending left arm joined to a longer rising right arm at a low corner. Generate this component alone; exclude Heart Frame.

Construction: The short left stroke and longer rising right stroke preserve the source check.
Keyshape: HRECT_M; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4bbd96be-f6bf-4a56-b592-6fde129cb45c'
SOURCE_PATH = 'pictographic-primitives/state/heart check_4bbd96be-f6bf-4a56-b592-6fde129cb45c.svg'
AUTHOR = 'gpt-6'


class CheckMarkState130(Sub32):
    icon_id = 'check-mark-state-130'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'descending', 'left', 'arm', 'joined', 'longer')

    def build(self):
        self.add_polyline('check',(2,14),(12,24),(30,8))
