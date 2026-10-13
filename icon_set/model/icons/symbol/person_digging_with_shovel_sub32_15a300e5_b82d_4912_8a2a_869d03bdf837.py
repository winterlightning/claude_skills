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
        # Digger: head, level arms, body curving to the hip, legs, shovel shaft with a straight blade.
        self.add_arc('p1-r1-1', (18, 6), (22, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 2), (26, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (26, 6), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (22, 10), (18, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_bezier('p2-r1-1', (20, 18), ((20, 22), (14, 26), (10, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 18), (26, 26))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (10, 26))
        self.add_line('p4-r1-2', (10, 26), (14, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 18), (20, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 30), (26, 26))
        self.add_line('p6-r1-2', (26, 26), (30, 22))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-2')
