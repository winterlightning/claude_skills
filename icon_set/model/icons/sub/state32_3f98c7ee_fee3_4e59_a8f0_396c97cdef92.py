"""Independent 32px profile of state32-3f98c7ee-fee3-4e59-a8f0-396c97cdef92.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3f98c7ee-fee3-4e59-a8f0-396c97cdef92'
SOURCE_PATH = 'icon_set/assets/combination-state32/3f98c7ee-fee3-4e59-a8f0-396c97cdef92.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3f98c7ee-fee3-4e59-a8f0-396c97cdef92', 'icon_set/assets/combination-state32/3f98c7ee-fee3-4e59-a8f0-396c97cdef92.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'f61da0ef3c3436ed5cd7afe4e8423e1a4b5f5521d63ed7ef99fae26abb9d2a1b'

class Drawing(Sub32):
    icon_id = 'state32-3f98c7ee-fee3-4e59-a8f0-396c97cdef92'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 12), (20, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (16, 8), (16, 15))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (11, 21), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
