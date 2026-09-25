"""Independent 32px profile of paddles-pair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '147f327b-3496-428c-8373-84c03c8c062b'
SOURCE_PATH = 'pictographic-primitives/symbol/double paddle_147f327b-3496-428c-8373-84c03c8c062b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('147f327b-3496-428c-8373-84c03c8c062b', 'pictographic-primitives/symbol/double paddle_147f327b-3496-428c-8373-84c03c8c062b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paddles-pair',)
SOLO_SOURCE_ICON_IDS = ('paddles-pair',)
REFERENCE_EXPORT_SHA256 = '64866d309a7414408a2f9fdbd1e9f4f86cc27698d1a2dd35f4d97de60cebea81'

class Drawing(Sub32):
    icon_id = 'paddles-pair-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 5), (7, 19), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 19), (7, 5), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (7, 19), (7, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (25, 5), (25, 19), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (25, 19), (25, 5), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (25, 19), (25, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
