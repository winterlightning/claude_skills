"""Independent 32px profile of interlocking-chain-links-solo-batch-025-13.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '55bd9f6e-12a9-4d3a-9646-c1852d270efe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('55bd9f6e-12a9-4d3a-9646-c1852d270efe', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/interlocking-chain-links-solo-batch-025-13',)
SOLO_SOURCE_ICON_IDS = ('interlocking-chain-links-solo-batch-025-13',)
REFERENCE_EXPORT_SHA256 = '255b5cf6706b5579fb609ae8eeb0e056e10694d84b9778038f253825d4acebe3'

class Drawing(Sub32):
    icon_id = 'interlocking-chain-links-solo-batch-025-13-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 2), (22, 2))
        self.add_bezier('p1-r1-2', (22, 2), ((27, 2), (30, 5), (30, 10)))
        self.add_bezier('p1-r1-3', (30, 10), ((30, 12), (29, 14), (28, 15)))
        self.add_line('p1-r1-4', (28, 15), (21, 21))
        self.add_bezier('p1-r1-5', (21, 21), ((20, 22), (19, 23), (18, 23)))
        self.add_bezier('p1-r1-6', (18, 23), ((17, 23), (15, 22), (14, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (13, 30), (10, 30))
        self.add_bezier('p2-r1-2', (10, 30), ((5, 30), (2, 27), (2, 22)))
        self.add_bezier('p2-r1-3', (2, 22), ((2, 20), (3, 18), (4, 17)))
        self.add_line('p2-r1-4', (4, 17), (11, 11))
        self.add_bezier('p2-r1-5', (11, 11), ((12, 10), (13, 9), (14, 9)))
        self.add_bezier('p2-r1-6', (14, 9), ((15, 9), (17, 10), (18, 11)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
