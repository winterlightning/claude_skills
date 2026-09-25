"""Check Mark: A short descending arm meets a longer rising arm at a sharp low corner. Generate this component alone; exclude Diamond Frame.

Construction: The source check is isolated from its diamond frame without altering its two-arm structure.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bdda71e5-4ed5-43c8-bae0-4dbe45a7e154'
SOURCE_PATH = 'pictographic-primitives/state/rhombus check_bdda71e5-4ed5-43c8-bae0-4dbe45a7e154.svg'
AUTHOR = 'gpt-6'


class CheckMarkState240(Sub32):
    icon_id = 'check-mark-state-240'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'descending', 'arm', 'meets', 'longer', 'rising')

    def build(self):
        self.add_polyline('check',(2,14),(12,24),(30,8))
