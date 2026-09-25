"""Independent 32px profile of airplane-flying-over-globe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'edb3fdfa-2f3d-4eac-81a5-1655e873407e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/globe plane_edb3fdfa-2f3d-4eac-81a5-1655e873407e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('edb3fdfa-2f3d-4eac-81a5-1655e873407e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/globe plane_edb3fdfa-2f3d-4eac-81a5-1655e873407e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-flying-over-globe',)
SOLO_SOURCE_ICON_IDS = ('airplane-flying-over-globe',)
REFERENCE_EXPORT_SHA256 = '24d08038d039b09ecb0e3c74809f55f1632ec08ca4fa654051dd9ba6579fd980'

class Drawing(Sub32):
    icon_id = 'airplane-flying-over-globe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (10, 2), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 2), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (18, 10), (10, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (10, 18), (2, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 10), (10, 10))
        self.add_line('p2-r1-2', (10, 10), (18, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 2), (10, 10))
        self.add_line('p3-r1-2', (10, 10), (10, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (19, 30), (24, 25))
        self.add_line('p4-r1-2', (24, 25), (30, 19))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (18, 21), (24, 25))
        self.add_line('p5-r1-2', (24, 25), (28, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (16, 30), (19, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
