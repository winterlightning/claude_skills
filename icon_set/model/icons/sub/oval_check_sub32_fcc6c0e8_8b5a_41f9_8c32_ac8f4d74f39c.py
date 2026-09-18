"""Independent 32px profile of oval-check.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = 'pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c', 'pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/oval-check',)
SOLO_SOURCE_ICON_IDS = ('oval-check',)
REFERENCE_EXPORT_SHA256 = 'd72e7226c9146f68419dc2c8df7694c6870102230ad408f644f26251cec497af'

class Drawing(Sub32):
    icon_id = 'oval-check-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 15), (15, 20))
        self.add_line('p2-r1-2', (15, 20), (21, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
