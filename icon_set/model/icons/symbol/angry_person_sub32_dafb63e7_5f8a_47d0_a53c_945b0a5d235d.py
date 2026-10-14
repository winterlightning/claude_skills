"""Independent 32px profile of angry-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'dafb63e7-5f8a-47d0-a53c-945b0a5d235d'
SOURCE_PATH = 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dafb63e7-5f8a-47d0-a53c-945b0a5d235d', 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angry-person',)
SOLO_SOURCE_ICON_IDS = ('angry-person',)
REFERENCE_EXPORT_SHA256 = '4ecc72aa7bda85e6b1e97b0021380500b4843c8e405d213f478ecd2db959034f'

class Drawing(Sub32):
    icon_id = 'angry-person-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Angry face: head circle, brows pulled down into a V, a flat grim mouth.
        self.add_arc('h-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('h-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('head', 'h-1', 'h-2', closed=True)
        self.add_polyline('brows', (13, 11), (16, 13), (19, 11))
        self.add_line('mouth', (13, 21), (19, 21))
