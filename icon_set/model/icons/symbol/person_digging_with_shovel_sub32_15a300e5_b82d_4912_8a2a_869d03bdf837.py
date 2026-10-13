"""Independent 32px profile of person-digging-with-shovel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '15a300e5-b82d-4912-8a2a-869d03bdf837'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person with a shovel_15a300e5-b82d-4912-8a2a-869d03bdf837.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('15a300e5-b82d-4912-8a2a-869d03bdf837', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person with a shovel_15a300e5-b82d-4912-8a2a-869d03bdf837.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-digging-with-shovel',)
SOLO_SOURCE_ICON_IDS = ('person-digging-with-shovel',)
REFERENCE_EXPORT_SHA256 = '4af79c2cef66b5b18720e1fd20bac84ab96f6c02a93284ec2e9a30b251f9b4bf'

class Drawing(Sub32):
    icon_id = 'person-digging-with-shovel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (20, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 2), (24, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (24, 6), (20, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (20, 10), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (20, 16), ((20, 21), (14, 24), (10, 24)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 16), (24, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (10, 24))
        self.add_line('p4-r1-2', (10, 24), (14, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 16), (20, 16))
        self.add_line('p5-r1-2', (20, 16), (24, 24))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (24, 24), (28, 21))
        self.add_line('p6-r1-2', (28, 21), (30, 30))
        self.add_line('p6-r1-3', (30, 30), (21, 28))
        self.add_line('p6-r1-4', (21, 28), (24, 24))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
        self.relate('connect', 'p5-r1-2', 'p6-r1-1')
        self.relate('connect', 'p5-r1-2', 'p6-r1-4')
