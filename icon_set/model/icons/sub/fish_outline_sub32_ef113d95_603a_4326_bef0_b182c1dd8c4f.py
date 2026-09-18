"""Independent 32px profile of fish-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ef113d95-603a-4326-bef0-b182c1dd8c4f'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with two small circle_ef113d95-603a-4326-bef0-b182c1dd8c4f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef113d95-603a-4326-bef0-b182c1dd8c4f', 'pictographic-primitives/symbol/fish with two small circle_ef113d95-603a-4326-bef0-b182c1dd8c4f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fish-outline',)
SOLO_SOURCE_ICON_IDS = ('fish-outline',)
REFERENCE_EXPORT_SHA256 = '282cb86edd60880d8b70509e61bfd98da69c019099d9fa4202a80fd2b3bc6d1c'

class Drawing(Sub32):
    icon_id = 'fish-outline-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (9, 11))
        self.add_arc('p1-r1-2', (9, 11), (16, 5), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 5), (30, 16), radius_x=18, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (30, 16), (16, 27), radius_x=18, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 27), (9, 21), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (9, 21), (2, 27))
        self.add_line('p1-r1-7', (2, 27), (4, 16))
        self.add_line('p1-r1-8', (4, 16), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (20, 13), (20, 20), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
