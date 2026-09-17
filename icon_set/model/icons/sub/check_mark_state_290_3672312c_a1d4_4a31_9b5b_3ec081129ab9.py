"""Check Mark: A short downstroke joins a longer rising arm. Generate this component alone; exclude Circle Frame, User Bust.

Construction: Isolate the source check from its portrait and circular frame.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3672312c-a1d4-4a31-9b5b-3ec081129ab9'
SOURCE_PATH = 'pictographic-primitives/state/user check_3672312c-a1d4-4a31-9b5b-3ec081129ab9.svg'
AUTHOR = 'gpt-6'


class CheckMarkState290(Sub32):
    icon_id = 'check-mark-state-290'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'downstroke', 'joins', 'longer', 'rising', 'arm')

    def build(self):
        self.add_polyline('check',(2,18),(12,28),(30,4))
