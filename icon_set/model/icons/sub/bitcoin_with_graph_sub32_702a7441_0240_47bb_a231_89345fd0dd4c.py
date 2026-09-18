"""Independent 32px profile of bitcoin-with-graph.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '702a7441-0240-47bb-a231-89345fd0dd4c'
SOURCE_PATH = 'pictographic-primitives/symbol/bitcoin with graph_702a7441-0240-47bb-a231-89345fd0dd4c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('702a7441-0240-47bb-a231-89345fd0dd4c', 'pictographic-primitives/symbol/bitcoin with graph_702a7441-0240-47bb-a231-89345fd0dd4c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bitcoin-with-graph',)
SOLO_SOURCE_ICON_IDS = ('bitcoin-with-graph',)
REFERENCE_EXPORT_SHA256 = 'a37e2c82e8cb88134d84bb7d857d616fcc4e061aee4c05056944f7455abcab70'

class Drawing(Sub32):
    icon_id = 'bitcoin-with-graph-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 26), (10, 11))
        self.add_line('p1-r1-2', (10, 11), (17, 27))
        self.add_line('p1-r1-3', (17, 27), (29, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (22, 8), (29, 5))
        self.add_line('p2-r1-2', (29, 5), (30, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
