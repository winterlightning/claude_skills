"""Independent 32px profile of state32-039d6076-f6f0-4285-9273-7fe0e43d2b2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'icon_set/assets/combination-state32/039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('039d6076-f6f0-4285-9273-7fe0e43d2b2e', 'icon_set/assets/combination-state32/039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9c4164af841b10c7194867f8a4c030ee5c3ae28e1c8ea493430bd67f3b8024e5'

class Drawing(Sub32):
    icon_id = 'state32-039d6076-f6f0-4285-9273-7fe0e43d2b2e'
    keyshape = Keyshape.HRECT_M
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (30, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 24), (10, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 20), (16, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 24), (23, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
