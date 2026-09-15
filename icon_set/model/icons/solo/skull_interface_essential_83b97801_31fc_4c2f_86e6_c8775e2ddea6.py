"""skull-interface-essential: approved original model.

Construction: Skull with an elliptical cranium, rounded jaw and two hollow circular eye sockets; broad cheeks keep the openings clear.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: skull from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '83b97801-31fc-4c2f-86e6-c8775e2ddea6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_83b97801-31fc-4c2f-86e6-c8775e2ddea6.svg'
AUTHOR = 'gpt-6'

class SkullInterfaceEssential(Solo48):
    icon_id = 'skull-interface-essential'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'skull', (4, 24), ('A', 20, 16, True, (24, 8)), ('A', 20, 16, True, (44, 24)), ('L', (44, 30)), ('A', 4, 4, True, (40, 34)), ('L', (36, 34)), ('L', (36, 36)), ('A', 4, 4, True, (32, 40)), ('L', (16, 40)), ('A', 4, 4, True, (12, 36)), ('L', (12, 34)), ('L', (8, 34)), ('A', 4, 4, True, (4, 30)), ('L', (4, 24)), closed=True)
        ellipse(self, 'eye-left', 16, 23, 3)
        ellipse(self, 'eye-right', 32, 23, 3)
        line(self, 'tooth', (24, 32), (24, 40))
        contacts(self)
