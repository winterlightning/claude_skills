"""Double Chevron Right: Two matching open chevrons point right, standing side by side with a narrow gap between them. Generate this component alone; exclude Circle Frame.

Construction: Two matching right chevrons share their height and horizontal translation.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f587e9fa-2c98-4afb-8edc-fcfcb1437a91'
SOURCE_PATH = 'pictographic-primitives/state/circle double next_f587e9fa-2c98-4afb-8edc-fcfcb1437a91.svg'
AUTHOR = 'gpt-6'


class DoubleChevronRight(Sub32):
    icon_id = 'double-chevron-right'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('double', 'chevron', 'right', 'matching', 'open', 'chevrons', 'point', 'standing')

    def build(self):
        for i,x in enumerate((2,18)):
            self.add_polyline(f'chevron-{i}',(x,4),(x+12,16),(x,28))
