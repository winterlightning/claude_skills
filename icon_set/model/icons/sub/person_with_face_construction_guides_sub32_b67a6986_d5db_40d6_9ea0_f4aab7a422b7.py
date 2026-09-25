"""Independent 32px profile of person-with-face-construction-guides.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b67a6986-d5db-40d6-9ea0-f4aab7a422b7'
SOURCE_PATH = 'pictographic-primitives/business/design person_b67a6986-d5db-40d6-9ea0-f4aab7a422b7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b67a6986-d5db-40d6-9ea0-f4aab7a422b7', 'pictographic-primitives/business/design person_b67a6986-d5db-40d6-9ea0-f4aab7a422b7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-with-face-construction-guides',)
SOLO_SOURCE_ICON_IDS = ('person-with-face-construction-guides',)
REFERENCE_EXPORT_SHA256 = 'ec7fd587461e3694347c59bc9c94079b1466ee586a0283f36cce5ef0ac342611'

class Drawing(Sub32):
    icon_id = 'person-with-face-construction-guides-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    categories = ('business', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 10), (16, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 18), (8, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (8, 10), (16, 2), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 10), (8, 10))
        self.add_line('p2-r1-2', (8, 10), (16, 10))
        self.add_line('p2-r1-3', (16, 10), (24, 10))
        self.add_line('p2-r1-4', (24, 10), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (2, 30), (16, 24), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (16, 24), (30, 30), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-1', 'p2-r1-4')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-2', 'p2-r1-4')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
