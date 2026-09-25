"""Independent 32px profile of horned-bull-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '749c49e8-3491-46dc-9c16-62b4f5a5ab0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/goat head_749c49e8-3491-46dc-9c16-62b4f5a5ab0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('749c49e8-3491-46dc-9c16-62b4f5a5ab0c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/goat head_749c49e8-3491-46dc-9c16-62b4f5a5ab0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horned-bull-head',)
SOLO_SOURCE_ICON_IDS = ('horned-bull-head',)
REFERENCE_EXPORT_SHA256 = 'd613ef1a19c07075d7c351c986a8cebfbd3e350bad0d0309fcb1d42d4d81ed97'

class Drawing(Sub32):
    icon_id = 'horned-bull-head-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 16), ((8, 12), (12, 10), (16, 10)))
        self.add_bezier('p1-r1-2', (16, 10), ((20, 10), (24, 12), (24, 16)))
        self.add_line('p1-r1-3', (24, 16), (24, 22))
        self.add_line('p1-r1-4', (24, 22), (20, 25))
        self.add_line('p1-r1-5', (20, 25), (20, 26))
        self.add_bezier('p1-r1-6', (20, 26), ((20, 28), (18, 30), (16, 30)))
        self.add_bezier('p1-r1-7', (16, 30), ((14, 30), (13, 28), (13, 26)))
        self.add_line('p1-r1-8', (13, 26), (13, 25))
        self.add_line('p1-r1-9', (13, 25), (8, 22))
        self.add_line('p1-r1-10', (8, 22), (8, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_bezier('p2-r1-1', (8, 16), ((5, 15), (5, 13), (5, 10)))
        self.add_line('p2-r1-2', (5, 10), (5, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (24, 16), ((27, 15), (27, 13), (27, 10)))
        self.add_line('p3-r1-2', (27, 10), (27, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
