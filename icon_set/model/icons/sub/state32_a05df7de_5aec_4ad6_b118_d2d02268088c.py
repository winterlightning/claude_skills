"""Independent 32px profile of state32-a05df7de-5aec-4ad6-b118-d2d02268088c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a05df7de-5aec-4ad6-b118-d2d02268088c'
SOURCE_PATH = 'icon_set/assets/combination-state32/a05df7de-5aec-4ad6-b118-d2d02268088c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a05df7de-5aec-4ad6-b118-d2d02268088c', 'icon_set/assets/combination-state32/a05df7de-5aec-4ad6-b118-d2d02268088c.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'da21dbd05fe13f1c9fc63f08fd726b76bf9e75dbaf77b94950cb4f6920ab18c1'

class Drawing(Sub32):
    icon_id = 'state32-a05df7de-5aec-4ad6-b118-d2d02268088c'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 10), (12, 22))
        self.add_line('p1-r1-2', (12, 22), (20, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
