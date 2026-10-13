"""Independent 32px profile of arrows-diagonal-resize.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'eab2ea44-17e8-4abd-a74b-7e5c171a7bae'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right 1_eab2ea44-17e8-4abd-a74b-7e5c171a7bae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eab2ea44-17e8-4abd-a74b-7e5c171a7bae', 'pictographic-primitives/symbol/arrows left right 1_eab2ea44-17e8-4abd-a74b-7e5c171a7bae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-diagonal-resize',)
SOLO_SOURCE_ICON_IDS = ('arrows-diagonal-resize',)
REFERENCE_EXPORT_SHA256 = '365667a38a52e3912ff5f6573ad8ffa3d41e6f4c8c28e6f61e284e52b2c26efc'

class Drawing(Sub32):
    icon_id = 'arrows-diagonal-resize-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Diagonal resize: two arrows pointing out from the centre along one diagonal.
        self.add_line('shaft-1', (20, 12), (30, 2))
        self.add_polyline('head-1', (22, 2), (30, 2), (30, 10))
        self.add_line('shaft-2', (12, 20), (2, 30))
        self.add_polyline('head-2', (2, 22), (2, 30), (10, 30))
        self.relate('connect', 'shaft-1', 'head-1')
        self.relate('connect', 'shaft-2', 'head-2')
