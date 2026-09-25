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
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (3, 8), (9, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 8), (3, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (23, 8), (29, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (29, 8), (23, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (13, 14), (19, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (19, 14), (13, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 20))
        self.add_arc('p4-r1-2', (2, 20), (9, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (23, 20), (30, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p5-r1-2', (30, 20), (30, 21))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_arc('p6-r1-1', (9, 27), (23, 27), radius_x=7, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
