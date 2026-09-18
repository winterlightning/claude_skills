"""Independent 32px profile of building-929733e7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '929733e7-35b6-4e6e-bcee-05768cc7b7d3'
SOURCE_PATH = 'pictographic-primitives/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('929733e7-35b6-4e6e-bcee-05768cc7b7d3', 'pictographic-primitives/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-929733e7',)
SOLO_SOURCE_ICON_IDS = ('building-929733e7',)
REFERENCE_EXPORT_SHA256 = '7ca30296605e6290a01732226625a81724b195cdd0e173964f9cd4bcec01fdd1'

class Drawing(Sub32):
    icon_id = 'building-929733e7-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (8, 30))
        self.add_line('p1-r1-2', (8, 30), (15, 30))
        self.add_line('p1-r1-3', (15, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (8, 30), (8, 2))
        self.add_line('p2-r1-2', (8, 2), (20, 2))
        self.add_line('p2-r1-3', (20, 2), (20, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (15, 30), (15, 10))
        self.add_line('p3-r1-2', (15, 10), (20, 10))
        self.add_line('p3-r1-3', (20, 10), (27, 10))
        self.add_line('p3-r1-4', (27, 10), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (21, 17), (21, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-4')
        self.relate("connect", 'p2-r1-3', 'p3-r1-2')
        self.relate("connect", 'p2-r1-3', 'p3-r1-3')
