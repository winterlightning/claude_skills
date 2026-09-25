"""batch-01-laptop-computers: approved original model.

Construction: Wide laptop screen with a base that tapers inward to a flat, softly rounded front edge.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: laptop from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '4679969c-dfb9-4a03-ab57-4d2eded56e5a'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.svg'
AUTHOR = 'gpt-6'

class Batch01LaptopComputers(Solo48):
    icon_id = 'batch-01-laptop-computers'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'screen', (4, 30), ('L', (4, 12)), ('A', 4, 4, True, (8, 8)), ('L', (40, 8)), ('A', 4, 4, True, (44, 12)), ('L', (44, 30)))
        path(self, 'base', (4, 30), ('L', (44, 30)), ('C', (42, 36), (41, 40), (36, 40)), ('L', (12, 40)), ('C', (7, 40), (6, 36), (4, 30)), closed=True)
        contacts(self)
