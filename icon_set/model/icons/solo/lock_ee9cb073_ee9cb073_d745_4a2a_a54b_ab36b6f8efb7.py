"""lock-ee9cb073: approved original model.

Construction: Padlock with a circular keyhole in its body, separated from the unmarked padlock.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: lock from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'ee9cb073-d745-4a2a-a54b-ab36b6f8efb7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_ee9cb073-d745-4a2a-a54b-ab36b6f8efb7.svg'
AUTHOR = 'gpt-6'

class LockEe9cb073(Solo48):
    icon_id = 'lock-ee9cb073'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self, 'shackle', (14, 20), ('L', (14, 14)), ('A', 10, 10, True, (24, 4)), ('A', 10, 10, True, (34, 14)), ('L', (34, 20)))
        box(self, 'body', 8, 20, 40, 44, 4, xs=(14, 34))
        ellipse(self, 'keyhole', 24, 32, 3)
        contacts(self)
