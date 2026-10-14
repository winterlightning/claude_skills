"""Independent 32px profile of airchair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e130f83-d8c1-50d3-98ae-5ea5bac53dab'
SOURCE_PATH = 'pictographic-primitives/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e130f83-d8c1-50d3-98ae-5ea5bac53dab', 'pictographic-primitives/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airchair',)
SOLO_SOURCE_ICON_IDS = ('airchair',)
REFERENCE_EXPORT_SHA256 = 'b29a2058073322dc8827bab0577109cf27871d6049be52fa197c1ecb460a2bd7'

class Drawing(Sub32):
    icon_id = 'airchair-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 30), (4, 14))
        self.add_arc('p1-r1-2', (4, 14), (12, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (12, 14), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (28, 30), (28, 14))
        self.add_arc('p2-r1-2', (28, 14), (20, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (20, 14), (20, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (4, 22), (28, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'path-1-1', 'path-4-1')
        self.relate('connect', 'path-2-1', 'path-4-1')
