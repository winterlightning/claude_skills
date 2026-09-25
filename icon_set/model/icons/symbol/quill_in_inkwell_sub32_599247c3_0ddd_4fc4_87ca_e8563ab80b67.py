"""Independent 32px profile of quill-in-inkwell.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '599247c3-0ddd-4fc4-87ca-e8563ab80b67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/quill ink_599247c3-0ddd-4fc4-87ca-e8563ab80b67.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('599247c3-0ddd-4fc4-87ca-e8563ab80b67', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/quill ink_599247c3-0ddd-4fc4-87ca-e8563ab80b67.svg'), ('610efb6f-0e7e-481b-b2a4-7e9873ef369d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/quill inkwell_610efb6f-0e7e-481b-b2a4-7e9873ef369d.svg'))
PROFILE_SOURCE_KEYS = ('solo/quill-in-inkwell',)
SOLO_SOURCE_ICON_IDS = ('quill-in-inkwell',)
REFERENCE_EXPORT_SHA256 = '82ebbd97047a09ec811d014c6d46e8e88821d876421f5989b86aeb5166be6f52'

class Drawing(Sub32):
    icon_id = 'quill-in-inkwell-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 21), (7, 19))
        self.add_line('p1-r1-2', (7, 19), (13, 19))
        self.add_line('p1-r1-3', (13, 19), (19, 19))
        self.add_line('p1-r1-4', (19, 19), (19, 21))
        self.add_arc('p1-r1-5', (19, 21), (24, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 25), (24, 30))
        self.add_line('p1-r1-7', (24, 30), (2, 30))
        self.add_line('p1-r1-8', (2, 30), (2, 25))
        self.add_arc('p1-r1-9', (2, 25), (7, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_bezier('p2-r1-1', (16, 13), ((16, 7), (24, 2), (30, 2)))
        self.add_bezier('p2-r1-2', (30, 2), ((30, 10), (24, 13), (16, 13)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (13, 19), (16, 13))
        self.add_line('p3-r1-2', (16, 13), (22, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
