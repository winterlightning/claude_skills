"""Independent 32px profile of wallet-clasp.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd'
SOURCE_PATH = 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd', 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wallet-clasp',)
SOLO_SOURCE_ICON_IDS = ('wallet-clasp',)
REFERENCE_EXPORT_SHA256 = 'b4723a46cd93b18bf5fb5fcf0dad6e9c2d424c06fcc22e72c7947aefc9339692'

class Drawing(Sub32):
    icon_id = 'wallet-clasp-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 5), (26, 5))
        self.add_arc('p1-r1-2', (26, 5), (30, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 9), (30, 13))
        self.add_line('p1-r1-4', (30, 13), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (30, 23))
        self.add_arc('p1-r1-6', (30, 23), (26, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (26, 27), (6, 27))
        self.add_arc('p1-r1-8', (6, 27), (2, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 23), (2, 11))
        self.add_line('p1-r1-10', (2, 11), (2, 9))
        self.add_arc('p1-r1-11', (2, 9), (6, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (2, 11), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 13), (23, 13))
        self.add_arc('p3-r1-2', (23, 13), (23, 22), radius_x=4.5, radius_y=4.5, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (23, 22), (30, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-3')
        self.relate("connect", 'p1-r1-5', 'p3-r1-3')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p1-r1-10', 'p2-r1-1')
