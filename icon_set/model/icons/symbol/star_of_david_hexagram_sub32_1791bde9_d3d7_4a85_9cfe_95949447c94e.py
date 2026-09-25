"""Independent 32px profile of star-of-david-hexagram.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1791bde9-d3d7-4a85-9cfe-95949447c94e'
SOURCE_PATH = 'pictographic-primitives/symbol/star of david_1791bde9-d3d7-4a85-9cfe-95949447c94e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1791bde9-d3d7-4a85-9cfe-95949447c94e', 'pictographic-primitives/symbol/star of david_1791bde9-d3d7-4a85-9cfe-95949447c94e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/star-of-david-hexagram',)
SOLO_SOURCE_ICON_IDS = ('star-of-david-hexagram',)
REFERENCE_EXPORT_SHA256 = '3ff2eefcdb8fce544c54ed6a348d07efbd0d1035fee93e09628621a306e0c2c2'

class Drawing(Sub32):
    icon_id = 'star-of-david-hexagram-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (21, 9))
        self.add_line('p1-r1-2', (21, 9), (25, 16))
        self.add_line('p1-r1-3', (25, 16), (30, 23))
        self.add_line('p1-r1-4', (30, 23), (21, 23))
        self.add_line('p1-r1-5', (21, 23), (11, 23))
        self.add_line('p1-r1-6', (11, 23), (2, 23))
        self.add_line('p1-r1-7', (2, 23), (7, 16))
        self.add_line('p1-r1-8', (7, 16), (11, 9))
        self.add_line('p1-r1-9', (11, 9), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (2, 9), (11, 9))
        self.add_line('p2-r1-2', (11, 9), (21, 9))
        self.add_line('p2-r1-3', (21, 9), (30, 9))
        self.add_line('p2-r1-4', (30, 9), (25, 16))
        self.add_line('p2-r1-5', (25, 16), (21, 23))
        self.add_line('p2-r1-6', (21, 23), (16, 30))
        self.add_line('p2-r1-7', (16, 30), (11, 23))
        self.add_line('p2-r1-8', (11, 23), (7, 16))
        self.add_line('p2-r1-9', (7, 16), (2, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-5')
        self.relate('connect', 'p1-r1-5', 'p2-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-7')
        self.relate('connect', 'p1-r1-5', 'p2-r1-8')
        self.relate('connect', 'p1-r1-6', 'p2-r1-7')
        self.relate('connect', 'p1-r1-6', 'p2-r1-8')
        self.relate('connect', 'p1-r1-7', 'p2-r1-8')
        self.relate('connect', 'p1-r1-7', 'p2-r1-9')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-2')
        self.relate('connect', 'p1-r1-8', 'p2-r1-8')
        self.relate('connect', 'p1-r1-8', 'p2-r1-9')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-2')
