"""Independent 32px profile of bug-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64'
SOURCE_PATH = 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64', 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'), ('9a3ccf45-79d9-442e-9bbb-bf6598cc98bf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bug_9a3ccf45-79d9-442e-9bbb-bf6598cc98bf.svg'))
PROFILE_SOURCE_KEYS = ('solo/bug-beetle',)
SOLO_SOURCE_ICON_IDS = ('bug-beetle',)
REFERENCE_EXPORT_SHA256 = 'f8b19500a7958cb097600733a4c60115200d7536dfdd043e56be6366d6b34045'

class DrawingContainerSymbol(Sub32):
    icon_id = 'bug-beetle-sub32-symbol'
    related_origin_icon_id = 'bug-beetle-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bug-beetle-sub32'
    counterpart_icon_id = 'bug-beetle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Beetle: head dome on a round-bottomed body, two antennae, three legs per side 8 units apart.
        self.add_arc('p1-r1-1', (8, 12), (16, 4), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 4), (24, 12), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 12), (24, 22))
        self.add_arc('p1-r1-4', (24, 22), (16, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 30), (8, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (8, 22), (8, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        self.add_line('p2-r1-1', (8, 12), (24, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 5), (9, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 5), (23, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (8, 14), (2, 10))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (8, 20), (2, 20))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (10, 27), (4, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (24, 14), (30, 10))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (24, 20), (30, 20))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (22, 27), (28, 30))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        for leg in ('path-3-1', 'path-4-1', 'path-5-1', 'path-6-1', 'path-7-1', 'path-8-1', 'path-9-1', 'path-10-1'):
            self.relate('connect', 'path-1-1', leg)
        self.relate('connect', 'path-1-1', 'path-2-1')
