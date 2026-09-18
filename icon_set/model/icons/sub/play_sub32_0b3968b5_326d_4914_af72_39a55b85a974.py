"""Independent 32px profile of play.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0b3968b5-326d-4914-af72-39a55b85a974'
SOURCE_PATH = 'pictographic-primitives/design/play_0b3968b5-326d-4914-af72-39a55b85a974.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0b3968b5-326d-4914-af72-39a55b85a974', 'pictographic-primitives/design/play_0b3968b5-326d-4914-af72-39a55b85a974.svg'),)
PROFILE_SOURCE_KEYS = ('solo/play',)
SOLO_SOURCE_ICON_IDS = ('play',)
REFERENCE_EXPORT_SHA256 = '0863d89204b2c8d6430c7db536b6ab01c14c3bb507befab7d38b817ee808edb1'

class Drawing(Sub32):
    icon_id = 'play-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 15), (27, 18))
        self.add_line('p1-r1-2', (27, 18), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (2, 2))
        self.add_line('p1-r1-4', (2, 2), (30, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
