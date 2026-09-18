"""Independent 32px profile of rope-climber.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 6), (14, 6), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (14, 6), (9, 6), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (30, 2), (30, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 16), (13, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 16), (5, 16))
        self.add_line('p4-r1-2', (5, 16), (2, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (13, 16), (21, 11))
        self.add_line('p5-r1-2', (21, 11), (30, 11))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (7, 22), (13, 22))
        self.add_line('p6-r1-2', (13, 22), (21, 22))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (13, 22), (5, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (13, 22), (22, 25))
        self.add_line('p8-r1-2', (22, 25), (22, 30))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_arc('p9-r1-1', (30, 11), (21, 22), radius_x=9, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p5-r1-2')
        self.relate("connect", 'p2-r1-1', 'p9-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p6-r1-1')
        self.relate("connect", 'p3-r1-1', 'p6-r1-2')
        self.relate("connect", 'p3-r1-1', 'p7-r1-1')
        self.relate("connect", 'p3-r1-1', 'p8-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p5-r1-2', 'p9-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-1', 'p8-r1-1')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
        self.relate("connect", 'p6-r1-2', 'p8-r1-1')
        self.relate("connect", 'p6-r1-2', 'p9-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
