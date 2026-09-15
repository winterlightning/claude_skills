"""card-d486b4cd: approved original model.

Construction: Chip payment card with a rounded chip window and two short account marks, rather than a magnetic stripe.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: credit-card from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'd486b4cd-e594-4512-a823-0935e0604565'
SOURCE_PATH = 'pictographic-primitives/business/card_d486b4cd-e594-4512-a823-0935e0604565.svg'
AUTHOR = 'gpt-6'

class CardD486b4cd(Solo48):
    icon_id = 'card-d486b4cd'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'card', 4, 8, 44, 40, 4)
        box(self, 'chip', 13, 17, 23, 31, 2)
        line(self, 'mark-top', (32, 18), (35, 18))
        line(self, 'mark-bottom', (32, 30), (35, 30))
        contacts(self)
