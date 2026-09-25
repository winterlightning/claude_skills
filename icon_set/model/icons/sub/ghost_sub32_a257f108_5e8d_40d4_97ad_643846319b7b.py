"""Independent 32px profile of ghost.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a257f108-5e8d-40d4-97ad-643846319b7b'
SOURCE_PATH = 'pictographic-primitives/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a257f108-5e8d-40d4-97ad-643846319b7b', 'pictographic-primitives/symbol/ghost_a257f108-5e8d-40d4-97ad-643846319b7b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ghost',)
SOLO_SOURCE_ICON_IDS = ('ghost',)
REFERENCE_EXPORT_SHA256 = '6060ec47344bdb9577b363215c76cbfc21c9c01af9fd1470f54d160065400f0e'

class Drawing(Sub32):
    icon_id = 'ghost-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 24), (5, 13))
        self.add_arc('p1-r1-2', (5, 13), (16, 2), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 2), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (27, 13), (27, 24))
        self.add_bezier('p1-r1-5', (27, 24), ((27, 27), (27, 30), (24, 30)))
        self.add_bezier('p1-r1-6', (24, 30), ((22, 30), (22, 27), (20, 27)))
        self.add_bezier('p1-r1-7', (20, 27), ((18, 27), (18, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((14, 30), (14, 27), (12, 27)))
        self.add_bezier('p1-r1-9', (12, 27), ((10, 27), (10, 30), (8, 30)))
        self.add_bezier('p1-r1-10', (8, 30), ((5, 30), (5, 27), (5, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
