'symbol-non-specific: distinct review variant.\n\nConstruction: Generic oval symbol with an uninterrupted elliptical outline, distinct from rectangles with straight rails.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: rectangle-horizontal from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '070e2a8a-37c3-4533-b497-d491749afb89'
SOURCE_PATH = 'pictographic-primitives/protection/symbol non specific_070e2a8a-37c3-4533-b497-d491749afb89.svg'
AUTHOR = 'gpt-6'


class SymbolNonSpecificVariant2(Solo48):
    icon_id = 'symbol-non-specific-v2'
    variant_of = 'symbol-non-specific'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'non', 'specific', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self):
        ellipse(self,'oval',24,24,20,16)
        contacts(self)
