"""state-mail: approved original model.

Construction: Square mail state badge: centered V fold with a vertical lower seam; compact proportions distinguish it from the wide envelopes.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: mail from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'f42c1e62-6183-4903-b7ff-5d9817c49685'
SOURCE_PATH = 'pictographic-primitives/symbol/state mail_f42c1e62-6183-4903-b7ff-5d9817c49685.svg'
AUTHOR = 'gpt-6'

class StateMail(Solo48):
    icon_id = 'state-mail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('state', 'mail', 'symbol')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self, 'envelope', 6, 6, 42, 42, 4, xs=(24,))
        poly(self, 'fold', (6, 10), (24, 24), (42, 10))
        line(self, 'seam', (24, 24), (24, 42))
        contacts(self)
