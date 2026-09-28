"""batch-02-desktop-computer-computers: approved original model.

Construction: Desktop display with a lower chin band, central pedestal and broad foot.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: monitor from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '94bf7c3e-3c0a-4019-a95a-f28f2638320e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer_94bf7c3e-3c0a-4019-a95a-f28f2638320e.svg'
AUTHOR = 'gpt-6'

class Batch02DesktopComputerComputers(Solo48):
    icon_id = 'batch-02-desktop-computer-computers'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'state')
    aliases = ()
    keywords = ('batch', 'desktop', 'computer', 'computers')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'screen', 4, 8, 44, 32, 4, xs=(24,), ys=(24,))
        line(self, 'chin', (4, 24), (44, 24))
        line(self, 'stand', (24, 32), (24, 40))
        line(self, 'foot', (12, 40), (36, 40))
        contacts(self)
