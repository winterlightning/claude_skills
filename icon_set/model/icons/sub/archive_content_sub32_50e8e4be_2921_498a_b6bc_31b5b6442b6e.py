"""Independent 32px profile of archive-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '50e8e4be-2921-498a-b6bc-31b5b6442b6e'
SOURCE_PATH = 'pictographic-primitives/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50e8e4be-2921-498a-b6bc-31b5b6442b6e', 'pictographic-primitives/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/archive-content',)
SOLO_SOURCE_ICON_IDS = ('archive-content',)
REFERENCE_EXPORT_SHA256 = '926bff737c8bf8a9d8370db741bde00711aa04ccf2eeeb7ce457b3310227cfc3'

class Drawing(Sub32):
    icon_id = 'archive-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 9), (22, 9))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 15), (17, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 20), (20, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (5, 30), (5, 2))
        self.add_line('p4-r1-2', (5, 2), (27, 2))
        self.add_line('p4-r1-3', (27, 2), (27, 30))
        self.add_line('p4-r1-4', (27, 30), (5, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
