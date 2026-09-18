"""Independent 32px profile of batch-01-monitor.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '181755f1-a8ab-4d25-8475-ebcf6885f0c8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('181755f1-a8ab-4d25-8475-ebcf6885f0c8', 'pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/batch-01-monitor',)
SOLO_SOURCE_ICON_IDS = ('batch-01-monitor',)
REFERENCE_EXPORT_SHA256 = '34fd7e51467ec3794807bc853d4b93247b563e7325194d798f00a79542b88416'

class Drawing(Sub32):
    icon_id = 'batch-01-monitor-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (27, 5))
        self.add_arc('p1-r1-3', (27, 5), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 8), (30, 17))
        self.add_arc('p1-r1-5', (30, 17), (27, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (27, 20), (16, 20))
        self.add_line('p1-r1-7', (16, 20), (5, 20))
        self.add_arc('p1-r1-8', (5, 20), (2, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 17), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (16, 20), (16, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 27), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 27), (22, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
