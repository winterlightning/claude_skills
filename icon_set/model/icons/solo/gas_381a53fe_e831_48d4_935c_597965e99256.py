"""gas: approved original model.

Construction: Gas flame with one main tongue and a smaller side tongue; natural flame asymmetry distinguishes it from a liquid drop.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: droplet from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '381a53fe-e831-48d4-935c-597965e99256'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gas_381a53fe-e831-48d4-935c-597965e99256.svg'
AUTHOR = 'gpt-6'

class Gas(Solo48):
    icon_id = 'gas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gas', '_uncategorized')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self, 'flame', (24, 4), ('C', (22, 15), (8, 18), (8, 29)), ('C', (8, 38), (15, 44), (24, 44)), ('C', (33, 44), (40, 38), (40, 29)), ('C', (40, 22), (36, 17), (33, 14)), ('C', (33, 23), (29, 25), (27, 23)), ('C', (23, 19), (29, 10), (24, 4)), closed=True)
        contacts(self)
