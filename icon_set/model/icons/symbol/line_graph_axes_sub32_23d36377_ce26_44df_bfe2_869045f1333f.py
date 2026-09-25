"""Independent 32px profile of line-graph-axes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '23d36377-ce26-44df-bfe2-869045f1333f'
SOURCE_PATH = 'pictographic-primitives/symbol/graph 1_23d36377-ce26-44df-bfe2-869045f1333f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23d36377-ce26-44df-bfe2-869045f1333f', 'pictographic-primitives/symbol/graph 1_23d36377-ce26-44df-bfe2-869045f1333f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/line-graph-axes',)
SOLO_SOURCE_ICON_IDS = ('line-graph-axes',)
REFERENCE_EXPORT_SHA256 = 'e650d302255b2f8fdd937122f884c43f6b616f7913db4c0d81d5296be751e2b4'

class Drawing(Sub32):
    icon_id = 'line-graph-axes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 22))
        self.add_line('p1-r1-2', (2, 22), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 22), (10, 13))
        self.add_line('p2-r1-2', (10, 13), (18, 20))
        self.add_line('p2-r1-3', (18, 20), (28, 7))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
