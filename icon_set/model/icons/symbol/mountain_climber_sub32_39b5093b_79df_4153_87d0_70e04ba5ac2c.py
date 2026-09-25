"""Independent 32px profile of mountain-climber.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '39b5093b-79df-4153-87d0-70e04ba5ac2c'
SOURCE_PATH = 'pictographic-primitives/sports/climbing mountain_39b5093b-79df-4153-87d0-70e04ba5ac2c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39b5093b-79df-4153-87d0-70e04ba5ac2c', 'pictographic-primitives/sports/climbing mountain_39b5093b-79df-4153-87d0-70e04ba5ac2c.svg'), ('c63b6ce9-917b-4f7e-a312-f05bbdf42679', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/climb_c63b6ce9-917b-4f7e-a312-f05bbdf42679.svg'))
PROFILE_SOURCE_KEYS = ('solo/mountain-climber',)
SOLO_SOURCE_ICON_IDS = ('mountain-climber',)
REFERENCE_EXPORT_SHA256 = 'a1a189c8ba0c55beae8fee4f4d551ba5c6848be6aa60a0a307e33cc65a3aaa49'

class Drawing(Sub32):
    icon_id = 'mountain-climber-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 7), (11, 7), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (11, 7), (6, 7), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (30, 2), (25, 8))
        self.add_line('p2-r1-2', (25, 8), (25, 13))
        self.add_line('p2-r1-3', (25, 13), (22, 16))
        self.add_line('p2-r1-4', (22, 16), (25, 22))
        self.add_line('p2-r1-5', (25, 22), (25, 30))
        self.add_line('p2-r1-6', (25, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (10, 16), (7, 25))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 16), (16, 16))
        self.add_line('p4-r1-2', (16, 16), (22, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (10, 16), (2, 14))
        self.add_line('p5-r1-2', (2, 14), (2, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (7, 25), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (7, 25), (16, 22))
        self.add_line('p7-r1-2', (16, 22), (18, 28))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate('connect', 'p2-r1-3', 'p4-r1-2')
        self.relate('connect', 'p2-r1-4', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p7-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
