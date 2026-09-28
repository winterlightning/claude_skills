"""sign-badge-badge-maps: approved original model.

Construction: Flat-top map badge with rounded shoulders and a smooth pointed lower bowl, distinct from the domed shield.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: shield from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '51affb95-85ee-5312-8a83-f077a030e9a9'
SOURCE_PATH = 'pictographic-primitives/maps/sign badge badge_51affb95-85ee-5312-8a83-f077a030e9a9.svg'
AUTHOR = 'gpt-6'

class SignBadgeBadgeMaps(Solo48):
    icon_id = 'sign-badge-badge-maps'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    categories = ('maps', 'primitives')
    aliases = ()
    keywords = ('sign', 'badge', 'maps')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self, 'badge', (12, 4), ('L', (36, 4)), ('A', 4, 4, True, (40, 8)), ('L', (40, 24)), ('C', (40, 34), (32, 40), (24, 44)), ('C', (16, 40), (8, 34), (8, 24)), ('L', (8, 8)), ('A', 4, 4, True, (12, 4)), closed=True)
        contacts(self)
