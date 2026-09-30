"""Two overlapping sheets with a centered plus on the front. A single rear open outline sits ten units from the front; plus arms share one center. Lucide copy-plus informed interrupted overlap and centered mark.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, invalid, invalid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: SQUARE; fine source details simplified only for native readability.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (add-new-duplicate-copy SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'cd975e65-ffe5-4f54-9bf3-fe16cf89cfcd'
SOURCE_PATH = 'pictographic-primitives/files/copy_cd975e65-ffe5-4f54-9bf3-fe16cf89cfcd.svg'
AUTHOR = 'claude-opus-5-5'


class Icon(Container64):
    icon_id = 'add-new-duplicate-copy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Add New Duplicate Copy',)
    keywords = ('add', 'new', 'duplicate', 'copy')

    def build(self) -> None:
        self.add_line('rear-1', (6, 45), (6, 6))
        self.add_line('rear-2', (6, 6), (45, 6))
        self.add_line('front-1', (15, 15), (58, 15))
        self.add_line('front-2', (58, 15), (58, 58))
        self.add_line('front-3', (58, 58), (15, 58))
        self.add_line('front-4', (15, 58), (15, 15))
        self.add_line('left', (37, 37), (27, 37))
        self.add_line('right', (37, 37), (49, 37))
        self.add_line('top', (37, 37), (37, 27))
        self.add_line('bottom', (37, 37), (37, 49))
        self.add_contour('rear', 'rear-1', 'rear-2')
        self.add_contour('front', 'front-1', 'front-2', 'front-3', 'front-4', closed=True)
        self.relate('connect', 'left', 'right', 'top', 'bottom')
