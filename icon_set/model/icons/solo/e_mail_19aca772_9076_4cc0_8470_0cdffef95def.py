"""e-mail: approved original model.

Construction: Wide envelope with a high straight V fold; distinguish it from the low gently rounded Airmail fold.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: mail from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '19aca772-9076-4cc0-8470-0cdffef95def'
SOURCE_PATH = 'pictographic-primitives/symbol/e mail_19aca772-9076-4cc0-8470-0cdffef95def.svg'
AUTHOR = 'gpt-6'

class EMail(Solo48):
    icon_id = 'e-mail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('e', 'mail', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'envelope', 4, 8, 44, 40, 4)
        poly(self, 'flap', (4, 12), (24, 25), (44, 12))
        contacts(self)
