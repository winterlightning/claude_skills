"""Independent 32px profile of person-silhouette-wavy.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '01aff74c-6e7d-4c53-9e84-005da220b852'
SOURCE_PATH = 'pictographic-primitives/symbol/sub square_01aff74c-6e7d-4c53-9e84-005da220b852.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('01aff74c-6e7d-4c53-9e84-005da220b852', 'pictographic-primitives/symbol/sub square_01aff74c-6e7d-4c53-9e84-005da220b852.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-silhouette-wavy',)
SOLO_SOURCE_ICON_IDS = ('person-silhouette-wavy',)
REFERENCE_EXPORT_SHA256 = 'f8da5746d8999fa9687bf0adf25a6c6341cefc750d77599e42cf2bdf945a2a2a'

class Drawing(Sub32):
    icon_id = 'person-silhouette-wavy-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 28))
        self.add_arc('p1-r1-2', (2, 28), (7, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (7, 24), (13, 21))
        self.add_line('p1-r1-4', (13, 21), (13, 17))
        self.add_arc('p1-r1-5', (13, 17), (10, 11), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 11), (10, 8))
        self.add_arc('p1-r1-7', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (22, 8), (22, 11))
        self.add_arc('p1-r1-9', (22, 11), (19, 17), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (19, 17), (19, 21))
        self.add_line('p1-r1-11', (19, 21), (25, 24))
        self.add_arc('p1-r1-12', (25, 24), (30, 28), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (30, 28), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
