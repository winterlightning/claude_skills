"""plus-math-symbol-circle: approved original model.

Construction: Circled mathematical plus with an outlined cross, distinguishing it clearly from the simple crossed-stroke add button.
Keyshape: CIRCLE; exact SOLO48 envelope.
Construction reference: circle-plus from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'b0bba548-63cf-4a5b-979d-41ee0f279414'
SOURCE_PATH = 'pictographic-primitives/interface-essential/plus math symbol circle_b0bba548-63cf-4a5b-979d-41ee0f279414.svg'
AUTHOR = 'gpt-6'

class PlusMathSymbolCircle(Solo48):
    icon_id = 'plus-math-symbol-circle'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('plus', 'math', 'symbol', 'circle', 'interface-essential')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self, 'ring', 24, 24, 20)
        poly(self, 'plus', (20, 13), (28, 13), (28, 20), (35, 20), (35, 28), (28, 28), (28, 35), (20, 35), (20, 28), (13, 28), (13, 20), (20, 20), closed=True)
        contacts(self)
