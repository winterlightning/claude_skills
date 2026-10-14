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
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (20, 9))
        self.add_line('p1-r1-2', (20, 9), (28, 9))
        self.add_line('p1-r1-3', (28, 9), (24, 16))
        self.add_line('p1-r1-4', (24, 16), (28, 23))
        self.add_line('p1-r1-5', (28, 23), (20, 23))
        self.add_line('p1-r1-6', (20, 23), (16, 30))
        self.add_line('p1-r1-7', (16, 30), (12, 23))
        self.add_line('p1-r1-8', (12, 23), (4, 23))
        self.add_line('p1-r1-9', (4, 23), (8, 16))
        self.add_line('p1-r1-10', (8, 16), (4, 9))
        self.add_line('p1-r1-11', (4, 9), (12, 9))
        self.add_line('p1-r1-12', (12, 9), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=True)
