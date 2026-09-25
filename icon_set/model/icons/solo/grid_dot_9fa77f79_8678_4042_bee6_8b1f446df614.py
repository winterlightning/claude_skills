"""grid-dot: approved original model.

Construction: Grid-dot symbol: four equally spaced points inside a rounded square frame.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '9fa77f79-8678-4042-bee6-8b1f446df614'
SOURCE_PATH = 'pictographic-primitives/design/grid dot_9fa77f79-8678-4042-bee6-8b1f446df614.svg'
AUTHOR = 'gpt-6'

class GridDot(Solo48):
    icon_id = 'grid-dot'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('grid', 'dot', 'design')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self, 'frame', 6, 6, 42, 42, 4)
        for x in (17, 31):
            for y in (17, 31):
                self.add_dot(f'grid-{x}-{y}', (x, y))
        contacts(self)
