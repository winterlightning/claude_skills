"""Independent 32px profile of counterclockwise-circular-refresh-arrows-batch-020-03.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a11ecc5-12d2-479f-ad50-bf72f2730e09', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'),)
PROFILE_SOURCE_KEYS = ('solo/counterclockwise-circular-refresh-arrows-batch-020-03',)
SOLO_SOURCE_ICON_IDS = ('counterclockwise-circular-refresh-arrows-batch-020-03',)
REFERENCE_EXPORT_SHA256 = '220b2bf7d75ab1a8e4c652894547377547552a5ddf264e115ff661cd25b64d9a'

class Drawing(Sub32):
    icon_id = 'counterclockwise-circular-refresh-arrows-batch-020-03-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 8), ((24, 4), (20, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((13, 2), (10, 3), (8, 5)))
        self.add_bezier('p1-r1-3', (8, 5), ((4, 8), (2, 12), (2, 16)))
        self.add_bezier('p1-r1-4', (2, 16), ((2, 19), (3, 22), (5, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (5, 24), ((8, 28), (12, 30), (16, 30)))
        self.add_bezier('p2-r1-2', (16, 30), ((19, 30), (22, 29), (24, 27)))
        self.add_bezier('p2-r1-3', (24, 27), ((28, 24), (30, 20), (30, 16)))
        self.add_bezier('p2-r1-4', (30, 16), ((30, 13), (29, 10), (27, 8)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (5, 16), (5, 24))
        self.add_line('p3-r1-2', (5, 24), (13, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (19, 8), (27, 8))
        self.add_line('p4-r1-2', (27, 8), (27, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-4')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-4', 'p4-r1-1')
        self.relate("connect", 'p2-r1-4', 'p4-r1-2')
