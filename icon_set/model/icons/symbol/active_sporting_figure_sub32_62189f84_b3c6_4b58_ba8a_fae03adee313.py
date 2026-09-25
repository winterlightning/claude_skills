"""Independent 32px profile of active-sporting-figure.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '62189f84-b3c6-4b58-ba8a-fae03adee313'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-12/video game wii_62189f84-b3c6-4b58-ba8a-fae03adee313.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('62189f84-b3c6-4b58-ba8a-fae03adee313', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-12/video game wii_62189f84-b3c6-4b58-ba8a-fae03adee313.svg'),)
PROFILE_SOURCE_KEYS = ('solo/active-sporting-figure',)
SOLO_SOURCE_ICON_IDS = ('active-sporting-figure',)
REFERENCE_EXPORT_SHA256 = 'ffdbc1594b5662b3333005a67c1f6b8204b8c5f957d956f01020c4999bca81ec'

class Drawing(Sub32):
    icon_id = 'active-sporting-figure-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (20, 6), (24, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 2), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (28, 6), (24, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (24, 10), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (24, 16), ((24, 19), (19, 22), (16, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (24, 16))
        self.add_line('p3-r1-2', (24, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 30), (16, 22))
        self.add_line('p4-r1-2', (16, 22), (21, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
