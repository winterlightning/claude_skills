# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of bug-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64'
SOURCE_PATH = 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64', 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'), ('9a3ccf45-79d9-442e-9bbb-bf6598cc98bf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bug_9a3ccf45-79d9-442e-9bbb-bf6598cc98bf.svg'))
PROFILE_SOURCE_KEYS = ('solo/bug-beetle',)
SOLO_SOURCE_ICON_IDS = ('bug-beetle',)
REFERENCE_EXPORT_SHA256 = 'f8b19500a7958cb097600733a4c60115200d7536dfdd043e56be6366d6b34045'

class DrawingContainerSymbol(Sub32):
    icon_id = 'bug-beetle-sub32-symbol'
    variant_of = 'bug-beetle-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bug-beetle-sub32'
    counterpart_icon_id = 'bug-beetle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 5), (21, 5))
        self.add_arc('p1-r1-2', (21, 5), (25, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (25, 10), (25, 11))
        self.add_line('p1-r1-4', (25, 11), (25, 18))
        self.add_line('p1-r1-5', (25, 18), (25, 24))
        self.add_arc('p1-r1-6', (25, 24), (7, 24), radius_x=9, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (7, 24), (7, 18))
        self.add_line('p1-r1-8', (7, 18), (7, 11))
        self.add_line('p1-r1-9', (7, 11), (7, 10))
        self.add_arc('p1-r1-10', (7, 10), (11, 5), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (7, 11), (25, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 5), (8, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (7, 11), (4, 11))
        self.add_line('p4-r1-2', (4, 11), (2, 7))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (7, 18), (2, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (7, 24), (4, 25))
        self.add_line('p6-r1-2', (4, 25), (2, 28))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (21, 5), (24, 2))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (25, 11), (28, 11))
        self.add_line('p8-r1-2', (28, 11), (30, 7))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_line('p9-r1-1', (25, 18), (30, 18))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (25, 24), (28, 25))
        self.add_line('p10-r1-2', (28, 25), (30, 28))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p7-r1-1')
        self.relate('connect', 'p1-r1-2', 'p7-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p8-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p8-r1-1')
        self.relate('connect', 'p1-r1-4', 'p9-r1-1')
        self.relate('connect', 'p1-r1-5', 'p9-r1-1')
        self.relate('connect', 'p1-r1-5', 'p10-r1-1')
        self.relate('connect', 'p1-r1-6', 'p6-r1-1')
        self.relate('connect', 'p1-r1-6', 'p10-r1-1')
        self.relate('connect', 'p1-r1-7', 'p5-r1-1')
        self.relate('connect', 'p1-r1-7', 'p6-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p5-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-10', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p8-r1-1')
