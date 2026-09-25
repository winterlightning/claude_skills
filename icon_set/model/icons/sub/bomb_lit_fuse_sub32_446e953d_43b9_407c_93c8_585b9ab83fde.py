"""Independent 32px profile of bomb-lit-fuse.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '446e953d-43b9-407c-93c8-585b9ab83fde'
SOURCE_PATH = 'pictographic-primitives/symbol/boom_446e953d-43b9-407c-93c8-585b9ab83fde.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('446e953d-43b9-407c-93c8-585b9ab83fde', 'pictographic-primitives/symbol/boom_446e953d-43b9-407c-93c8-585b9ab83fde.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bomb-lit-fuse',)
SOLO_SOURCE_ICON_IDS = ('bomb-lit-fuse',)
REFERENCE_EXPORT_SHA256 = '5cdd4d24847e89980cba5c6faa39e2e27c33da98efd29df5d6425defb5ab7c80'

class Drawing(Sub32):
    icon_id = 'bomb-lit-fuse-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (14, 16), (10, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 30), (2, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (2, 22), (14, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (14, 16), (22, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 2), (22, 8))
        self.add_line('p3-r1-2', (22, 8), (27, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (22, 8), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
