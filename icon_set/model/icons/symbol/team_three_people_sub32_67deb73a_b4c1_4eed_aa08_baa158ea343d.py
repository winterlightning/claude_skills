"""Independent 32px profile of team-three-people.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '67deb73a-b4c1-4eed-aa08-baa158ea343d'
SOURCE_PATH = 'pictographic-primitives/symbol/team_67deb73a-b4c1-4eed-aa08-baa158ea343d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('67deb73a-b4c1-4eed-aa08-baa158ea343d', 'pictographic-primitives/symbol/team_67deb73a-b4c1-4eed-aa08-baa158ea343d.svg'), ('e945361d-c5a9-4fd9-95aa-74d13dfd018c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/three persons_e945361d-c5a9-4fd9-95aa-74d13dfd018c.svg'))
PROFILE_SOURCE_KEYS = ('solo/team-three-people',)
SOLO_SOURCE_ICON_IDS = ('team-three-people',)
REFERENCE_EXPORT_SHA256 = 'bef89b66e11d810b126d89d28978037014d86baad2c0af09d2384bd248bc23d7'

class Drawing(Sub32):
    icon_id = 'team-three-people-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 4), (6, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 4), (2, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_arc('p2-r1-1', (26, 4), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 4), (26, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_arc('p3-r1-1', (14, 10), (18, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (18, 10), (14, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=True)
        self.add_arc('p4-r1-1', (6, 30), (26, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (2, 18), ((2, 13), (7, 12), (10, 22)))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (30, 18), ((30, 13), (25, 12), (22, 22)))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'path-4-1', 'path-5-1')
        self.relate('connect', 'path-4-1', 'path-6-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
