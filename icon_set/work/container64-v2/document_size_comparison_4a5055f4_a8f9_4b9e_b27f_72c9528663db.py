"""Document Size Comparison. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
Hosting probes: plus-sign-state-131 and check-mark are invalid; heart-state-63
is review. The document pair is not a general-purpose symbol host.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (document-size-comparison SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '4a5055f4-a8f9-4b9e-b27f-72c9528663db'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes two document measure_4a5055f4-a8f9-4b9e-b27f-72c9528663db.svg'
AUTHOR = 'claude-opus-5-5'


class Drawing(Container64):
    icon_id = 'document-size-comparison'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('document', 'size', 'comparison')

    def build(self) -> None:
        self.add_line('small-page-1', (6, 38), (14, 38))
        self.add_line('small-page-2', (14, 38), (22, 46))
        self.add_line('small-page-3', (22, 46), (22, 58))
        self.add_line('small-page-4', (22, 58), (6, 58))
        self.add_line('small-page-5', (6, 58), (6, 38))
        self.add_line('large-page-1', (30, 22), (50, 22))
        self.add_line('large-page-2', (50, 22), (58, 34))
        self.add_line('large-page-3', (58, 34), (58, 58))
        self.add_line('large-page-4', (58, 58), (30, 58))
        self.add_line('large-page-5', (30, 58), (30, 22))
        self.add_line('small-measure', (6, 28), (22, 28))
        self.add_line('small-left-1', (6, 24), (6, 28))
        self.add_line('small-left-2', (6, 28), (6, 32))
        self.add_line('small-right-1', (22, 24), (22, 28))
        self.add_line('small-right-2', (22, 28), (22, 32))
        self.add_line('large-measure', (30, 9), (58, 9))
        self.add_line('large-left-1', (30, 6), (30, 9))
        self.add_line('large-left-2', (30, 9), (30, 12))
        self.add_line('large-right-1', (58, 6), (58, 9))
        self.add_line('large-right-2', (58, 9), (58, 12))
        self.add_contour('small-page', 'small-page-1', 'small-page-2', 'small-page-3', 'small-page-4', 'small-page-5', closed=True)
        self.add_contour('large-page', 'large-page-1', 'large-page-2', 'large-page-3', 'large-page-4', 'large-page-5', closed=True)
        self.add_contour('small-left', 'small-left-1', 'small-left-2')
        self.add_contour('small-right', 'small-right-1', 'small-right-2')
        self.add_contour('large-left', 'large-left-1', 'large-left-2')
        self.add_contour('large-right', 'large-right-1', 'large-right-2')
        self.relate('connect', 'small-measure', 'small-left')
        self.relate('connect', 'small-measure', 'small-right')
        self.relate('connect', 'large-measure', 'large-left')
        self.relate('connect', 'large-measure', 'large-right')
