'symbol-medical: distinct review variant.\n\nConstruction: Broad medical cross with deliberate square arm ends and equal sixteen-unit stem widths.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: plus from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c2218007-b6c4-5c1b-9355-0c9d6d72fb5c'
SOURCE_PATH = 'pictographic-primitives/protection/symbol medical_c2218007-b6c4-5c1b-9355-0c9d6d72fb5c.svg'
AUTHOR = 'gpt-6'


class SymbolMedicalVariant2(Solo48):
    icon_id = 'symbol-medical-v2'
    variant_of = 'symbol-medical'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'medical', 'protection')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self,'cross',(16,6),(32,6),(32,16),(42,16),(42,32),(32,32),(32,42),(16,42),(16,32),(6,32),(6,16),(16,16),closed=True)
        contacts(self)
