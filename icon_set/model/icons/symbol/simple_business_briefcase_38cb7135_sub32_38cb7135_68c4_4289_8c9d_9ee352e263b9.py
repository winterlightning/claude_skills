"""Independent 32px profile of simple-business-briefcase-38cb7135.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '38cb7135-68c4-4289-8c9d-9ee352e263b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/case_38cb7135-68c4-4289-8c9d-9ee352e263b9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38cb7135-68c4-4289-8c9d-9ee352e263b9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/case_38cb7135-68c4-4289-8c9d-9ee352e263b9.svg'), ('e756308e-0744-49f8-9b09-d1933550ea61', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/briefcase_e756308e-0744-49f8-9b09-d1933550ea61.svg'))
PROFILE_SOURCE_KEYS = ('solo/simple-business-briefcase-38cb7135',)
SOLO_SOURCE_ICON_IDS = ('simple-business-briefcase-38cb7135',)
REFERENCE_EXPORT_SHA256 = '248232e9f63f23b3e63f09edfe6ed7ae9e16c71cbf9004cb875fb145ef191c1c'

class Drawing(Sub32):
    icon_id = 'simple-business-briefcase-38cb7135-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/case'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 10), (10, 10))
        self.add_line('p1-r1-2', (10, 10), (22, 10))
        self.add_line('p1-r1-3', (22, 10), (27, 10))
        self.add_arc('p1-r1-4', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 13), (30, 24))
        self.add_arc('p1-r1-6', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (27, 27), (5, 27))
        self.add_arc('p1-r1-8', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 24), (2, 13))
        self.add_arc('p1-r1-10', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (10, 10), (10, 8))
        self.add_arc('p2-r1-2', (10, 8), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 5), (19, 5))
        self.add_arc('p2-r1-4', (19, 5), (22, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (22, 8), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
