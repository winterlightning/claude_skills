"""Independent 32px profile of bar-graph-rising.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9eac7172-d6a3-4992-aaad-dd1cdbd21c70'
SOURCE_PATH = 'pictographic-primitives/symbol/bar graph_9eac7172-d6a3-4992-aaad-dd1cdbd21c70.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9eac7172-d6a3-4992-aaad-dd1cdbd21c70', 'pictographic-primitives/symbol/bar graph_9eac7172-d6a3-4992-aaad-dd1cdbd21c70.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bar-graph-rising',)
SOLO_SOURCE_ICON_IDS = ('bar-graph-rising',)
REFERENCE_EXPORT_SHA256 = '31e2f9ea4031cfe1facef7eda815cce8eafbd3f8a10ee9b549d431a76c85621e'

class Drawing(Sub32):
    icon_id = 'bar-graph-rising-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (2, 28), (8, 28))
        self.add_line('p1-r1-2', (8, 28), (13, 28))
        self.add_line('p1-r1-3', (13, 28), (19, 28))
        self.add_line('p1-r1-4', (19, 28), (24, 28))
        self.add_line('p1-r1-5', (24, 28), (30, 28))
        self.add_line('p2-r1-1', (2, 28), (2, 19))
        self.add_line('p2-r1-2', (2, 19), (13, 19))
        self.add_line('p2-r1-3', (13, 19), (13, 28))
        self.add_line('p3-r1-1', (13, 28), (13, 12))
        self.add_line('p3-r1-2', (13, 12), (22, 12))
        self.add_line('p3-r1-3', (22, 12), (22, 28))
        self.add_line('p4-r1-1', (22, 28), (22, 4))
        self.add_line('p4-r1-2', (22, 4), (30, 4))
        self.add_line('p4-r1-3', (30, 4), (30, 28))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-3')
