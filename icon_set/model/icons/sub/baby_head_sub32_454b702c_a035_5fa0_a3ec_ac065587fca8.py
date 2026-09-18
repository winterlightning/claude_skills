"""Independent 32px profile of baby-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('454b702c-a035-5fa0-a3ec-ac065587fca8', 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'), ('5393b57b-1ff9-4e16-b855-128e09e91ba7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/baby face_5393b57b-1ff9-4e16-b855-128e09e91ba7.svg'))
PROFILE_SOURCE_KEYS = ('solo/baby-head',)
SOLO_SOURCE_ICON_IDS = ('baby-head',)
REFERENCE_EXPORT_SHA256 = 'c68e2a7d40d4e7ea30956ae407215e1929527232a33f01a28390ff1f6647ba72'

class Drawing(Sub32):
    icon_id = 'baby-head-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'babies'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((2, 8), (8, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((24, 2), (30, 8), (30, 16)))
        self.add_bezier('p1-r1-3', (30, 16), ((30, 24), (24, 30), (16, 30)))
        self.add_bezier('p1-r1-4', (16, 30), ((8, 30), (2, 24), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (17, 2), ((17, 3), (17, 3), (17, 4)))
        self.add_bezier('p2-r1-2', (17, 4), ((17, 6), (16, 8), (12, 8)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 16), (10, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 16), (22, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (13, 22), ((14, 23), (15, 23), (16, 23)))
        self.add_bezier('p5-r1-2', (16, 23), ((17, 23), (18, 23), (19, 22)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
