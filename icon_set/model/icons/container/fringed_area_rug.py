"""An upright rectangular rug has evenly spaced fringe at both ends.

Keyshape VRECT_XL: visible bounds (4, 0, 60, 64).
Lucide frame informs straight connected bars; source supplies paired fringed
edges. Centerline extremes (6,2)-(58,62). Seven fringe strokes at each end
retain the textile identity with generous spacing and bilateral symmetry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class FringedAreaRug(Container64):
    icon_id = 'fringed-area-rug'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('fringed-rug', 'area-rug')
    keywords = ('rug', 'mat', 'textile', 'fringe')

    def build(self) -> None:
        self.add_polyline('rug', (6, 8), (58, 8), (58, 56), (6, 56), closed=True)
        self.add_line('fringe-top-6', (6, 2), (6, 8))
        self.relate("connect", 'rug', 'fringe-top-6')
        self.add_line('fringe-bottom-6', (6, 56), (6, 62))
        self.relate("connect", 'rug', 'fringe-bottom-6')
        self.add_line('fringe-top-14', (14, 2), (14, 8))
        self.relate("connect", 'rug', 'fringe-top-14')
        self.add_line('fringe-bottom-14', (14, 56), (14, 62))
        self.relate("connect", 'rug', 'fringe-bottom-14')
        self.add_line('fringe-top-23', (23, 2), (23, 8))
        self.relate("connect", 'rug', 'fringe-top-23')
        self.add_line('fringe-bottom-23', (23, 56), (23, 62))
        self.relate("connect", 'rug', 'fringe-bottom-23')
        self.add_line('fringe-top-32', (32, 2), (32, 8))
        self.relate("connect", 'rug', 'fringe-top-32')
        self.add_line('fringe-bottom-32', (32, 56), (32, 62))
        self.relate("connect", 'rug', 'fringe-bottom-32')
        self.add_line('fringe-top-41', (41, 2), (41, 8))
        self.relate("connect", 'rug', 'fringe-top-41')
        self.add_line('fringe-bottom-41', (41, 56), (41, 62))
        self.relate("connect", 'rug', 'fringe-bottom-41')
        self.add_line('fringe-top-50', (50, 2), (50, 8))
        self.relate("connect", 'rug', 'fringe-top-50')
        self.add_line('fringe-bottom-50', (50, 56), (50, 62))
        self.relate("connect", 'rug', 'fringe-bottom-50')
        self.add_line('fringe-top-58', (58, 2), (58, 8))
        self.relate("connect", 'rug', 'fringe-top-58')
        self.add_line('fringe-bottom-58', (58, 56), (58, 62))
        self.relate("connect", 'rug', 'fringe-bottom-58')
