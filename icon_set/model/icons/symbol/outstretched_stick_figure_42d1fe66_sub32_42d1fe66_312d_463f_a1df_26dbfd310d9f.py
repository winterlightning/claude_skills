"""Independent 32px profile of outstretched-stick-figure-42d1fe66.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '42d1fe66-312d-463f-a1df-26dbfd310d9f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/anatomical davinci_42d1fe66-312d-463f-a1df-26dbfd310d9f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('42d1fe66-312d-463f-a1df-26dbfd310d9f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/anatomical davinci_42d1fe66-312d-463f-a1df-26dbfd310d9f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/outstretched-stick-figure-42d1fe66',)
SOLO_SOURCE_ICON_IDS = ('outstretched-stick-figure-42d1fe66',)
REFERENCE_EXPORT_SHA256 = 'b948e7840d43d6214850ff072cb13c31a0358743755bdeaab6d8eee06bb05316'

class Drawing(Sub32):
    icon_id = 'outstretched-stick-figure-42d1fe66-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 6), (12, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 19), (16, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 11), (16, 19))
        self.add_line('p4-r1-2', (16, 19), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (7, 30), (16, 21))
        self.add_line('p5-r1-2', (16, 21), (25, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
