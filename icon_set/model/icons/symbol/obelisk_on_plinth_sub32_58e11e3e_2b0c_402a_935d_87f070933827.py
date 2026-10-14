"""Independent 32px profile of obelisk-on-plinth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '58e11e3e-2b0c-402a-935d-87f070933827'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_58e11e3e-2b0c-402a-935d-87f070933827.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58e11e3e-2b0c-402a-935d-87f070933827', 'pictographic-primitives/landmarks/batch-02/tower_58e11e3e-2b0c-402a-935d-87f070933827.svg'),)
PROFILE_SOURCE_KEYS = ('solo/obelisk-on-plinth',)
SOLO_SOURCE_ICON_IDS = ('obelisk-on-plinth',)
REFERENCE_EXPORT_SHA256 = 'bcd71e46155f9c263ac76cf69ef02c8d3bdc2f65c108a3e0b801e8f2101214e9'

class Drawing(Sub32):
    icon_id = 'obelisk-on-plinth-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Obelisk on a plinth: pointed top, a gently tapering 8-unit shaft, a wide plinth.
        self.add_polyline('obelisk', (10, 22), (12, 8), (16, 2), (20, 8), (22, 22))
        self.add_polyline('plinth', (2, 22), (30, 22), (30, 30), (2, 30), closed=True)
        self.relate('connect', 'obelisk', 'plinth')
