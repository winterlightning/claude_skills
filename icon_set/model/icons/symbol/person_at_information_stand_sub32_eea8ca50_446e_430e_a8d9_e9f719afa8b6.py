"""Independent 32px profile of person-at-information-stand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'eea8ca50-446e-430e-a8d9-e9f719afa8b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/watcher_eea8ca50-446e-430e-a8d9-e9f719afa8b6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eea8ca50-446e-430e-a8d9-e9f719afa8b6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/watcher_eea8ca50-446e-430e-a8d9-e9f719afa8b6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-at-information-stand',)
SOLO_SOURCE_ICON_IDS = ('person-at-information-stand',)
REFERENCE_EXPORT_SHA256 = 'a5bdca289e73309b96f7a49f64abf7e1eb7b46ca88ca564f0a7828ad1ded8a07'

class Drawing(Sub32):
    icon_id = 'person-at-information-stand-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (7, 2))
        self.add_line('p1-r1-2', (7, 2), (10, 2))
        self.add_arc('p1-r1-3', (10, 2), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (11, 4), (11, 8))
        self.add_arc('p1-r1-5', (11, 8), (10, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 10), (7, 10))
        self.add_line('p1-r1-7', (7, 10), (4, 10))
        self.add_arc('p1-r1-8', (4, 10), (2, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 8), (2, 4))
        self.add_arc('p1-r1-10', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (7, 10), (7, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (22, 5), (25, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (25, 2), (28, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (28, 5), (25, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (25, 8), (22, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (25, 14), (25, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (25, 14), (19, 18))
        self.add_line('p5-r1-2', (19, 18), (16, 14))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (18, 30), (25, 22))
        self.add_line('p6-r1-2', (25, 22), (30, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-2')
