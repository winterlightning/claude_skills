"""Independent 32px profile of three-rising-steam-waves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f373133d-7144-4071-b8d3-1de535383f54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heat waves_f373133d-7144-4071-b8d3-1de535383f54.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f373133d-7144-4071-b8d3-1de535383f54', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heat waves_f373133d-7144-4071-b8d3-1de535383f54.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-rising-steam-waves',)
SOLO_SOURCE_ICON_IDS = ('three-rising-steam-waves',)
REFERENCE_EXPORT_SHA256 = 'a5e6c00104be61fe884bde640480929b6668b4dd90b2b1c2bd6fea0a0953fb44'

class Drawing(Sub32):
    icon_id = 'three-rising-steam-waves-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 2), ((5, 5), (4, 8), (4, 10)))
        self.add_bezier('p1-r1-2', (4, 10), ((4, 14), (6, 18), (6, 22)))
        self.add_bezier('p1-r1-3', (6, 22), ((6, 24), (5, 27), (2, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_bezier('p2-r1-1', (19, 2), ((16, 5), (15, 8), (15, 10)))
        self.add_bezier('p2-r1-2', (15, 10), ((15, 14), (17, 18), (17, 22)))
        self.add_bezier('p2-r1-3', (17, 22), ((17, 24), (16, 27), (13, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (30, 2), ((27, 5), (26, 8), (26, 10)))
        self.add_bezier('p3-r1-2', (26, 10), ((26, 14), (28, 18), (28, 22)))
        self.add_bezier('p3-r1-3', (28, 22), ((28, 24), (27, 27), (24, 30)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
