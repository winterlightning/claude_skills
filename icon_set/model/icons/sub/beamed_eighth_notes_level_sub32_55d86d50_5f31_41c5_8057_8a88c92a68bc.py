"""Independent 32px profile of beamed-eighth-notes-level.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '55d86d50-5f31-41c5-8057-8a88c92a68bc'
SOURCE_PATH = 'pictographic-primitives/music/music_55d86d50-5f31-41c5-8057-8a88c92a68bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('55d86d50-5f31-41c5-8057-8a88c92a68bc', 'pictographic-primitives/music/music_55d86d50-5f31-41c5-8057-8a88c92a68bc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beamed-eighth-notes-level',)
SOLO_SOURCE_ICON_IDS = ('beamed-eighth-notes-level',)
REFERENCE_EXPORT_SHA256 = 'e6f606c08d859f55a74e34c54e0f373a4620bd93ba8b34df06b3082fd2160bb8'

class Drawing(Sub32):
    icon_id = 'beamed-eighth-notes-level-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'music'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 25), (7, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 21), (11, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (11, 25), (7, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (11, 25), (11, 12))
        self.add_line('p2-r1-2', (11, 12), (11, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (21, 25), (25, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (25, 21), (30, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (25, 30), (21, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (30, 25), (30, 9))
        self.add_line('p4-r1-2', (30, 9), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (11, 5), (30, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
