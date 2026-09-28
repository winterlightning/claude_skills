"""Independent 32px profile of downhill-skier.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c92285fd-d928-4a7c-a2c3-2e02288f502f'
SOURCE_PATH = 'pictographic-primitives/sports/skiing slide down_c92285fd-d928-4a7c-a2c3-2e02288f502f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c92285fd-d928-4a7c-a2c3-2e02288f502f', 'pictographic-primitives/sports/skiing slide down_c92285fd-d928-4a7c-a2c3-2e02288f502f.svg'), ('5a60755a-84e0-4d24-9372-1ab838965a3f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/snowboard_5a60755a-84e0-4d24-9372-1ab838965a3f.svg'))
PROFILE_SOURCE_KEYS = ('solo/downhill-skier',)
SOLO_SOURCE_ICON_IDS = ('downhill-skier',)
REFERENCE_EXPORT_SHA256 = '91c9cdc3c3597fb096af5663cdaecf19d1b7363da504d1bd92ae78b271305a81'

class Drawing(Sub32):
    icon_id = 'downhill-skier-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (25, 6), (25, 11), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (25, 11), (25, 6), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (8, 12), (5, 2))
        self.add_line('p2-r1-2', (5, 2), (16, 7))
        self.add_line('p2-r1-3', (16, 7), (18, 19))
        self.add_line('p2-r1-4', (18, 19), (28, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 7), (10, 18))
        self.add_line('p3-r1-2', (10, 18), (15, 24))
        self.add_line('p3-r1-3', (15, 24), (11, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 23), (11, 27))
        self.add_line('p4-r1-2', (11, 27), (24, 30))
        self.add_line('p4-r1-3', (24, 30), (30, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-2')
