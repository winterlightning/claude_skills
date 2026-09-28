"""rectangle-remove-state: approved original model.

Construction: Remove-state panel with a clear horizontal minus, distinct from the close-X panel.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: rectangle-horizontal from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'

class RectangleRemoveState(Solo48):
    icon_id = 'rectangle-remove-state'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('rectangle', 'remove', 'state')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'frame', 4, 8, 44, 40, 4)
        line(self, 'minus', (16, 24), (32, 24))
        contacts(self)
