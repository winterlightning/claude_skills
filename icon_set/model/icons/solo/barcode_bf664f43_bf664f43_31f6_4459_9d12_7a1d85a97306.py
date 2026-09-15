"""barcode-bf664f43: approved original model.

Construction: Five-bar barcode with equal spacing, distinct from the four-bar version.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: barcode from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'bf664f43-31f6-4459-9d12-7a1d85a97306'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_bf664f43-31f6-4459-9d12-7a1d85a97306.svg'
AUTHOR = 'gpt-6'

class BarcodeBf664f43(Solo48):
    icon_id = 'barcode-bf664f43'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        for i, x in enumerate((4, 14, 24, 34, 44)):
            line(self, f'bar-{i}', (x, 8), (x, 40))
        contacts(self)
