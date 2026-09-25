"""Independent 32px profile of graph-finance.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5552619f-de1f-40a4-b0e9-95549bca7398'
SOURCE_PATH = 'pictographic-primitives/finance/graph_5552619f-de1f-40a4-b0e9-95549bca7398.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5552619f-de1f-40a4-b0e9-95549bca7398', 'pictographic-primitives/finance/graph_5552619f-de1f-40a4-b0e9-95549bca7398.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graph-finance',)
SOLO_SOURCE_ICON_IDS = ('graph-finance',)
REFERENCE_EXPORT_SHA256 = '98909fae104b98e47184c2860738fa345555ce4de4727aad7122f947edff9a6d'

class Drawing(Sub32):
    icon_id = 'graph-finance-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'finance'
    categories = ('primitives', 'finance')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 27), (6, 27))
        self.add_line('p1-r1-2', (6, 27), (16, 27))
        self.add_line('p1-r1-3', (16, 27), (26, 27))
        self.add_line('p1-r1-4', (26, 27), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 5), (6, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 11), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (26, 15), (26, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
