"""sub-square-symbol: approved original model.

Construction: Soft square symbol with large twelve-unit corner arcs and short straight sides.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '7b60aeaa-7ff1-45c8-9911-bc14a557e883'
SOURCE_PATH = 'pictographic-primitives/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.svg'
AUTHOR = 'gpt-6'

class SubSquareSymbol(Solo48):
    icon_id = 'sub-square-symbol'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'square', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self, 'frame', 6, 6, 42, 42, 12)
        contacts(self)
