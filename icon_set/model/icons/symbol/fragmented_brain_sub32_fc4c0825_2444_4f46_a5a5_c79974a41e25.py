"""Independent 32px profile of fragmented-brain.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fc4c0825-2444-4f46-a5a5-c79974a41e25', 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fragmented-brain',)
SOLO_SOURCE_ICON_IDS = ('fragmented-brain',)
REFERENCE_EXPORT_SHA256 = '6cd7d2a64f86bf6bfbc1b8f7aaa9063cca619d5bd06f831e7a1ec81be0a614e7'

class Drawing(Sub32):
    icon_id = 'fragmented-brain-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Fragmented brain: oval brain, the central fissure, a crack splitting one half.
        self.add_arc('b-1', (2, 16), (30, 16), radius_x=14, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('b-2', (30, 16), (2, 16), radius_x=14, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('brain', 'b-1', 'b-2', closed=True)
        self.add_line('fissure', (16, 4), (16, 28))
        self.add_polyline('crack', (16, 16), (23, 13), (30, 16))
        self.relate('connect', 'brain', 'fissure')
        self.relate('connect', 'brain', 'crack')
        self.relate('connect', 'fissure', 'crack')
