'sub-square-symbol: distinct review variant.\n\nConstruction: Soft square symbol with large twelve-unit corner arcs and short straight sides.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7b60aeaa-7ff1-45c8-9911-bc14a557e883'
SOURCE_PATH = 'pictographic-primitives/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.svg'
AUTHOR = 'gpt-6'


class SubSquareSymbolVariant2(Solo48):
    icon_id = 'sub-square-symbol-v2'
    variant_of = 'sub-square-symbol'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'square', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'frame',6,6,42,42,12)
        contacts(self)
