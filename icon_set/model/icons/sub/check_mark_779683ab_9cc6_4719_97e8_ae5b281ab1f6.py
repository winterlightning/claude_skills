"""Check Mark: A check mark descends along a short left arm and rises along a longer right arm from a low central corner. Generate this component alone; exclude File Frame.

Construction: The short descending arm joins the long rising arm without changing the source check direction.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '779683ab-9cc6-4719-97e8-ae5b281ab1f6'
SOURCE_PATH = 'pictographic-primitives/state/file check_779683ab-9cc6-4719-97e8-ae5b281ab1f6.svg'
AUTHOR = 'gpt-6'


class CheckMark(Sub32):
    icon_id = 'check-mark'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'descends', 'along', 'short', 'left', 'arm', 'rises')

    def build(self):
        self.add_polyline('check',(2,18),(12,28),(30,4))
