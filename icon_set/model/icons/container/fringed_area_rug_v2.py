# Variant of fringed-area-rug; parent file remains unchanged.
"""An upright rectangular rug has evenly spaced fringe at both ends.

Keyshape VRECT_XL: visible bounds (4, 0, 60, 64).
Lucide frame informs straight connected bars; source supplies paired fringed
edges. Centerline extremes (6,2)-(58,62). Four corner fringe strokes in total
retain the textile identity with generous spacing and bilateral symmetry.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class FringedAreaRugVariant2(Container64):
    icon_id = 'fringed-area-rug-v2'
    variant_of = 'fringed-area-rug'
    variant_label = 'Four outer fringe strokes'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ('fringed-rug', 'area-rug')
    keywords = ('rug', 'mat', 'textile', 'fringe')

    def build(self) -> None:
        self.add_polyline('rug', (6, 8), (58, 8), (58, 56), (6, 56), closed=True)
        self.add_line('fringe-top-6', (6, 2), (6, 8))
        self.relate('connect', 'rug', 'fringe-top-6')
        self.add_line('fringe-bottom-6', (6, 56), (6, 62))
        self.relate('connect', 'rug', 'fringe-bottom-6')
        self.add_line('fringe-top-58', (58, 2), (58, 8))
        self.relate('connect', 'rug', 'fringe-top-58')
        self.add_line('fringe-bottom-58', (58, 56), (58, 62))
        self.relate('connect', 'rug', 'fringe-bottom-58')
