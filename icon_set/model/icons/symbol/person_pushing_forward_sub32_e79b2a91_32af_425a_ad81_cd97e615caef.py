"""Independent 32px profile of person-pushing-forward.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e79b2a91-32af-425a-ad81-cd97e615caef'
SOURCE_PATH = 'pictographic-primitives/symbol/person running_e79b2a91-32af-425a-ad81-cd97e615caef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e79b2a91-32af-425a-ad81-cd97e615caef', 'pictographic-primitives/symbol/person running_e79b2a91-32af-425a-ad81-cd97e615caef.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-pushing-forward',)
SOLO_SOURCE_ICON_IDS = ('person-pushing-forward',)
REFERENCE_EXPORT_SHA256 = 'f94fe3a8feb4cdb2c803c651da40ba426e2c5bf362f37a8d290e937e37621b67'

class Drawing(Sub32):
    icon_id = 'person-pushing-forward-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 7), (25, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (25, 7), (16, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 18), (10, 24))
        self.add_line('p2-r1-2', (10, 24), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 18), (19, 19))
        self.add_line('p3-r1-2', (19, 19), (30, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (10, 24), (19, 25))
        self.add_line('p4-r1-2', (19, 25), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
