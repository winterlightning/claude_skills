"""Independent 32px profile of walking-stick-figure.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e3a17fb-a451-57ee-9080-18af2bbac9d9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e3a17fb-a451-57ee-9080-18af2bbac9d9', 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'), ('7ce62344-aeae-474c-9800-f2104921b059', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/walking_7ce62344-aeae-474c-9800-f2104921b059.svg'))
PROFILE_SOURCE_KEYS = ('solo/walking-stick-figure',)
SOLO_SOURCE_ICON_IDS = ('walking-stick-figure',)
REFERENCE_EXPORT_SHA256 = '2c5a88771118fbec864ddc22b0ec466999bf304605e281927a6932fa6de9a7c0'

class Drawing(Sub32):
    icon_id = 'walking-stick-figure-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'wayfinding'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (15, 4), ((15, 3), (16, 2), (17, 2)))
        self.add_bezier('p1-r1-2', (17, 2), ((19, 2), (20, 3), (20, 4)))
        self.add_arc('p1-r1-3', (20, 4), (15, 4), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 13), (14, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 19), (16, 13))
        self.add_line('p3-r1-2', (16, 13), (24, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (5, 30), (14, 21))
        self.add_line('p4-r1-2', (14, 21), (23, 30))
        self.add_line('p4-r1-3', (23, 30), (27, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
