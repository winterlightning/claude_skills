"""Independent 32px profile of cursor-2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a1fd996b-f7ee-4257-bb4f-d644721f5983'
SOURCE_PATH = 'pictographic-primitives/symbol/cursor 2_a1fd996b-f7ee-4257-bb4f-d644721f5983.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1fd996b-f7ee-4257-bb4f-d644721f5983', 'pictographic-primitives/symbol/cursor 2_a1fd996b-f7ee-4257-bb4f-d644721f5983.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor-2',)
SOLO_SOURCE_ICON_IDS = ('cursor-2',)
REFERENCE_EXPORT_SHA256 = '846d44356d5f1e755e597f63528bfb98f69016f34bab43edc3aff01725f9ff6d'

class Drawing(Sub32):
    icon_id = 'cursor-2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (30, 2))
        self.add_line('p1-r1-2', (30, 2), (18, 30))
        self.add_line('p1-r1-3', (18, 30), (13, 19))
        self.add_line('p1-r1-4', (13, 19), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
