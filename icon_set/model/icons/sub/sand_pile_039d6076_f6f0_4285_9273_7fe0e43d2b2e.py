"""Sand Pile: Two sloping sides meet at a softly rounded peak to form an open triangular mound. Three tiny grain marks appear inside, with one above two lower marks.

Construction: A pointed mound has two matching open slopes and sparse detached grains.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'


class SandPile(Sub32):
    icon_id = 'sand-pile'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sand', 'pile', 'sloping', 'sides', 'meet', 'softly', 'rounded', 'peak')

    def build(self):
        self.add_polyline("mound",(2,28),(16,4),(30,28))
        self.add_dot("grain-upper",(16,16))
        self.add_dot("grain-lower",(16,26))
