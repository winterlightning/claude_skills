"""Independent 32px profile of rope-climber.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c734cba9-11d1-47ef-9193-480b63d4bd96'
SOURCE_PATH = 'pictographic-primitives/sports/climbing sports_c734cba9-11d1-47ef-9193-480b63d4bd96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c734cba9-11d1-47ef-9193-480b63d4bd96', 'pictographic-primitives/sports/climbing sports_c734cba9-11d1-47ef-9193-480b63d4bd96.svg'), ('64bc05d2-25cd-4e18-83c2-a00814ef966b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/climbing_64bc05d2-25cd-4e18-83c2-a00814ef966b.svg'))
PROFILE_SOURCE_KEYS = ('solo/rope-climber',)
SOLO_SOURCE_ICON_IDS = ('rope-climber',)
REFERENCE_EXPORT_SHA256 = '385e655134b8333f04ff418c7f109f38564527df7a98ea067d896aad407dbc53'

class Drawing(Sub32):
    icon_id = 'rope-climber-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Climber: head ring, level arm to a vertical rope, body and legs.
        self.add_arc('p1-r1-1', (8, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 6), (8, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (30, 2), (30, 18))
        self.add_line('p2-r1-2', (30, 18), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (12, 18), (12, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (12, 18), (30, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (12, 24))
        self.add_line('p5-r1-2', (12, 24), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
