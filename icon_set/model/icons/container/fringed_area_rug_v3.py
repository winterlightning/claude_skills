# Variant of fringed-area-rug-v2; parent file remains unchanged.
"""An upright rectangular rug has evenly spaced fringe at both ends.

Keyshape VRECT_XL: visible bounds (4, 0, 60, 64).
Lucide frame informs straight connected bars; source supplies paired fringed
edges. Centerline extremes (6,2)-(58,62). The four original corner fringe
strokes are preserved, with two middle strokes added at each end, mirrored
about x=32. The original VRECT_XL proportions and empty interior are unchanged.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class FringedAreaRugVariant3(Container64):
    icon_id = 'fringed-area-rug-v3'
    variant_of = 'fringed-area-rug-v2'
    variant_label = 'Paired middle fringe at both ends'
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
        for x in (26, 38):
            self.add_line(f'fringe-top-{x}', (x, 2), (x, 8))
            self.relate('connect', 'rug', f'fringe-top-{x}')
            self.add_line(f'fringe-bottom-{x}', (x, 56), (x, 62))
            self.relate('connect', 'rug', f'fringe-bottom-{x}')
