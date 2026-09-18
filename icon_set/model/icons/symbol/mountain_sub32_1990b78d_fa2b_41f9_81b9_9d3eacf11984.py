"""Independent 32px profile of mountain.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1990b78d-fa2b-41f9-81b9-9d3eacf11984'
SOURCE_PATH = 'pictographic-primitives/nature/mountain_1990b78d-fa2b-41f9-81b9-9d3eacf11984.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1990b78d-fa2b-41f9-81b9-9d3eacf11984', 'pictographic-primitives/nature/mountain_1990b78d-fa2b-41f9-81b9-9d3eacf11984.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mountain',)
SOLO_SOURCE_ICON_IDS = ('mountain',)
REFERENCE_EXPORT_SHA256 = 'bda79293c877012095a9a3d93d345990a0bd790d4ad3b474850bfd411a447399'

class Drawing(Sub32):
    icon_id = 'mountain-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 20), (10, 11))
        self.add_line('p1-r1-2', (10, 11), (2, 27))
        self.add_line('p1-r1-3', (2, 27), (30, 27))
        self.add_line('p1-r1-4', (30, 27), (18, 5))
        self.add_line('p1-r1-5', (18, 5), (13, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
