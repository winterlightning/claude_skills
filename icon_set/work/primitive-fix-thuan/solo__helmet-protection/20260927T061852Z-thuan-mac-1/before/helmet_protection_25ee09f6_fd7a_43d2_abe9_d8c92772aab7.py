"""helmet-protection: approved original model.

Construction: Protective helmet with a flat central crest and two straight reinforcing ribs joined to the brim; round shoulders flank the crest.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: hard-hat from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.svg'
AUTHOR = 'gpt-6'

class HelmetProtection(Solo48):
    icon_id = 'helmet-protection'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'dome', (8, 30), ('L', (8, 20)), ('A', 12, 12, True, (20, 8)), ('L', (28, 8)), ('A', 12, 12, True, (40, 20)), ('L', (40, 30)))
        box(self, 'brim', 4, 30, 44, 40, 3, xs=(8, 20, 28, 40))
        line(self, 'left-rib', (20, 8), (20, 30))
        line(self, 'right-rib', (28, 8), (28, 30))
        contacts(self)
