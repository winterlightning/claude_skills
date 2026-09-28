"""table-row-selected: approved original model.

Construction: Table with a wide selected middle row and a centered selection dot; narrow outer rows make it distinct from a regular data grid.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: layout-grid from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '5802ffd8-7306-4609-a53e-bc51b5281303'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__table-row-selected/20260927T094425Z-thuan-mac-1/reference/table row selected_5802ffd8-7306-4609-a53e-bc51b5281303.svg'
AUTHOR = 'gpt-6'
REVISION_COMPARISON = 'The rejected table lost the source’s vertical column divider and introduced a dot.'
REVISION_CHANGE = 'Restored the center column and four-cell layout.'


class TableRowSelected(Solo48):
    icon_id = 'table-row-selected'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('table', 'row', 'selected', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self, 'frame', 6, 6, 42, 42, 4, ys=(16, 32))
        line(self, 'upper-row', (6, 16), (42, 16))
        line(self, 'lower-row', (6, 32), (42, 32))
        line(self, 'column', (24, 6), (24, 42))
        self.relate('connect', 'column', 'frame')
        self.relate('connect', 'column', 'upper-row')
        self.relate('connect', 'column', 'lower-row')
        contacts(self)
