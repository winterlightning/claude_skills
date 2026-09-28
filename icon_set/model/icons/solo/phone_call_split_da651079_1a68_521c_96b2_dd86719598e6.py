"""phone-call-split: approved original model.

Construction: Split-call routing arrow with a crisp central Y junction and straight diagonal branches; keep arrow corners purposeful.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: split from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'da651079-1a68-521c-96b2-dd86719598e6'
SOURCE_PATH = 'pictographic-primitives/phones/phone call split_da651079-1a68-521c-96b2-dd86719598e6.svg'
AUTHOR = 'gpt-6'

class PhoneCallSplit(Solo48):
    icon_id = 'phone-call-split'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('phone', 'call', 'split', 'phones')
    keyshape = Keyshape.SQUARE

    def build(self):
        line(self, 'stem', (24, 42), (24, 24))
        poly(self, 'branches', (6, 6), (24, 24), (42, 6))
        poly(self, 'left-head', (6, 18), (6, 6), (18, 6))
        poly(self, 'right-head', (30, 6), (42, 6), (42, 18))
        contacts(self)
