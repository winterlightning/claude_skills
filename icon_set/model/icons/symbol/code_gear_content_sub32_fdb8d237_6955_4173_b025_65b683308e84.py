"""Independent 32px profile of code-gear-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fdb8d237-6955-4173-b025-65b683308e84'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fdb8d237-6955-4173-b025-65b683308e84', 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code-gear-content',)
SOLO_SOURCE_ICON_IDS = ('code-gear-content',)
REFERENCE_EXPORT_SHA256 = 'b0b55ee24401989dd47ec8cb1bd27d40c8122fdcbbd457810a7a82f944cf290f'

class Drawing(Sub32):
    icon_id = 'code-gear-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Code settings: a small gear above a pair of code brackets.
        self.add_polyline('gear', (18, 4), (17, 2), (15, 2), (14, 4), (13, 5), (10, 5), (10, 6), (11, 8), (11, 10), (10, 12), (10, 13), (13, 13), (14, 14), (15, 16), (17, 16), (18, 14), (19, 13), (22, 13), (22, 12), (21, 10), (21, 8), (22, 6), (22, 5), (19, 5), closed=True)
        self.add_polyline('bracket-left', (9, 22), (2, 26), (9, 30))
        self.add_polyline('bracket-right', (23, 22), (30, 26), (23, 30))
