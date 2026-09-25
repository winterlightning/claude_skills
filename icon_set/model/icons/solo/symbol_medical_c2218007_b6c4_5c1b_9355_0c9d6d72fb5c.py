"""symbol-medical: approved original model.

Construction: Broad medical cross with deliberate square arm ends and equal sixteen-unit stem widths.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: plus from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'c2218007-b6c4-5c1b-9355-0c9d6d72fb5c'
SOURCE_PATH = 'pictographic-primitives/protection/symbol medical_c2218007-b6c4-5c1b-9355-0c9d6d72fb5c.svg'
AUTHOR = 'gpt-6'

class SymbolMedical(Solo48):
    icon_id = 'symbol-medical'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('symbol', 'medical', 'protection')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self, 'cross', (16, 6), (32, 6), (32, 16), (42, 16), (42, 32), (32, 32), (32, 42), (16, 42), (16, 32), (6, 32), (6, 16), (16, 16), closed=True)
        contacts(self)
