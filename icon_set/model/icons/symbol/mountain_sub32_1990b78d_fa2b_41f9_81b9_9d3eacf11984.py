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
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Mountain with a zigzag snowcap.
        self.add_polyline('peak', (2, 28), (16, 4), (30, 28), closed=True)
        self.add_polyline('snow', (10, 14), (16, 20), (22, 14))
        self.relate('connect', 'peak', 'snow')
