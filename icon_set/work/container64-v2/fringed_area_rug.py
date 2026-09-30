"""An upright rectangular rug has evenly spaced fringe at both ends.

Keyshape VRECT_XL: visible bounds (4, 0, 60, 64).
Lucide frame informs straight connected bars; source supplies paired fringed
edges. Centerline extremes (6,2)-(58,62). The four original corner fringe
strokes are preserved, with two middle strokes added at each end, mirrored
about x=32. The original VRECT_XL proportions and empty interior are unchanged.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (fringed-area-rug VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class FringedAreaRug(Container64):
    icon_id = 'fringed-area-rug'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('fringed-rug', 'area-rug')
    keywords = ('rug', 'mat', 'textile', 'fringe')

    def build(self) -> None:
        self.add_line('rug-1', (10, 10), (54, 10))
        self.add_line('rug-2', (54, 10), (54, 54))
        self.add_line('rug-3', (54, 54), (10, 54))
        self.add_line('rug-4', (10, 54), (10, 10))
        self.add_line('fringe-top-6', (10, 4), (10, 10))
        self.add_line('fringe-bottom-6', (10, 54), (10, 60))
        self.add_line('fringe-top-58', (54, 4), (54, 10))
        self.add_line('fringe-bottom-58', (54, 54), (54, 60))
        self.add_line('fringe-top-26', (27, 4), (27, 10))
        self.add_line('fringe-bottom-26', (27, 54), (27, 60))
        self.add_line('fringe-top-38', (37, 4), (37, 10))
        self.add_line('fringe-bottom-38', (37, 54), (37, 60))
        self.add_contour('rug', 'rug-1', 'rug-2', 'rug-3', 'rug-4', closed=True)
        self.relate('connect', 'rug', 'fringe-top-6')
        self.relate('connect', 'rug', 'fringe-bottom-6')
        self.relate('connect', 'rug', 'fringe-top-58')
        self.relate('connect', 'rug', 'fringe-bottom-58')
        self.relate('connect', 'rug', 'fringe-top-26')
        self.relate('connect', 'rug', 'fringe-bottom-26')
        self.relate('connect', 'rug', 'fringe-top-38')
        self.relate('connect', 'rug', 'fringe-bottom-38')
