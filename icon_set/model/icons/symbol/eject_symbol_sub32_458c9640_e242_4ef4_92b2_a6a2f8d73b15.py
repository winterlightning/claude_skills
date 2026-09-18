"""Independent 32px profile of eject-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '458c9640-e242-4ef4-92b2-a6a2f8d73b15'
SOURCE_PATH = 'pictographic-primitives/symbol/eject_458c9640-e242-4ef4-92b2-a6a2f8d73b15.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('458c9640-e242-4ef4-92b2-a6a2f8d73b15', 'pictographic-primitives/symbol/eject_458c9640-e242-4ef4-92b2-a6a2f8d73b15.svg'),)
PROFILE_SOURCE_KEYS = ('solo/eject-symbol',)
SOLO_SOURCE_ICON_IDS = ('eject-symbol',)
REFERENCE_EXPORT_SHA256 = 'b10e199c0ea5fc08acd80ea43cc9ea5c88a44f7dbbf175e13bed05e316683807'

class Drawing(Sub32):
    icon_id = 'eject-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 20), (16, 2))
        self.add_line('p2-r1-2', (16, 2), (2, 20))
        self.add_line('p2-r1-3', (2, 20), (30, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
