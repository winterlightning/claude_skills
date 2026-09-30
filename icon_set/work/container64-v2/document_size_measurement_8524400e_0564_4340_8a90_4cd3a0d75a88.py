"""An upright clipped document with horizontal and vertical dimension markers. Caps share equal spans and axes; document and two measured edges remain distinct. Lucide files informed the page contour; measurement geometry comes from the source.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: valid, review, valid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: SQUARE; fine source details simplified only for native readability.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (document-size-measurement SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '8524400e-0564-4340-8a90-4cd3a0d75a88'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes one document measure_8524400e-0564-4340-8a90-4cd3a0d75a88.svg'
AUTHOR = 'claude-opus-5-5'


class Icon(Container64):
    icon_id = 'document-size-measurement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Document Size Measurement',)
    keywords = ('document', 'size', 'measurement')

    def build(self) -> None:
        self.add_line('page-upper-1', (9, 6), (34, 6))
        self.add_line('page-upper-2', (34, 6), (44, 18))
        self.add_line('page-upper-3', (44, 18), (44, 39))
        self.add_arc('page-br', (44, 39), (41, 42), radius_x=3)
        self.add_line('page-bottom', (41, 42), (9, 42))
        self.add_arc('page-bl', (9, 42), (6, 39), radius_x=3)
        self.add_line('page-left', (6, 39), (6, 9))
        self.add_arc('page-tl', (6, 9), (9, 6), radius_x=3)
        self.add_line('horizontal', (6, 54), (44, 54))
        self.add_line('horizontal-cap-0-a', (6, 50), (6, 54))
        self.add_line('horizontal-cap-0-b', (6, 54), (6, 58))
        self.add_line('horizontal-cap-1-a', (44, 50), (44, 54))
        self.add_line('horizontal-cap-1-b', (44, 54), (44, 58))
        self.add_line('vertical', (54, 6), (54, 42))
        self.add_line('vertical-cap-0-a', (50, 6), (54, 6))
        self.add_line('vertical-cap-0-b', (54, 6), (58, 6))
        self.add_line('vertical-cap-1-a', (50, 42), (54, 42))
        self.add_line('vertical-cap-1-b', (54, 42), (58, 42))
        self.add_contour('page', 'page-upper-1', 'page-upper-2', 'page-upper-3', 'page-br', 'page-bottom', 'page-bl', 'page-left', 'page-tl', closed=True)
        self.relate('connect', 'horizontal', 'horizontal-cap-0-a', 'horizontal-cap-0-b')
        self.relate('connect', 'horizontal', 'horizontal-cap-1-a', 'horizontal-cap-1-b')
        self.relate('connect', 'vertical', 'vertical-cap-0-a', 'vertical-cap-0-b')
        self.relate('connect', 'vertical', 'vertical-cap-1-a', 'vertical-cap-1-b')
