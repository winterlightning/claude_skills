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
        # Star-jump figure: head, a neck joining it to the body, arms up and legs apart.
        self.add_arc('head-1', (14, 4), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (18, 4), (14, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('neck', (16, 6), (16, 18))
        self.add_line('arm-l', (16, 18), (2, 10))
        self.add_line('arm-r', (16, 18), (30, 10))
        self.add_line('leg-l', (16, 18), (6, 30))
        self.add_line('leg-r', (16, 18), (26, 30))
        self.relate('connect', 'head', 'neck')
        self.relate('connect', 'arm-l', 'neck')
        self.relate('connect', 'arm-l', 'arm-r')
        self.relate('connect', 'arm-l', 'leg-l')
        self.relate('connect', 'arm-l', 'leg-r')
        self.relate('connect', 'arm-r', 'neck')
        self.relate('connect', 'arm-r', 'leg-l')
        self.relate('connect', 'arm-r', 'leg-r')
        self.relate('connect', 'leg-l', 'neck')
        self.relate('connect', 'leg-l', 'leg-r')
        self.relate('connect', 'leg-r', 'neck')
