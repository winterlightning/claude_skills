"""Independent 32px profile of measurement-marker-draft-batch-024-15.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e331499-062d-4a4a-965e-e100d55ce756', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'),)
PROFILE_SOURCE_KEYS = ('solo/measurement-marker-draft-batch-024-15',)
SOLO_SOURCE_ICON_IDS = ('measurement-marker-draft-batch-024-15',)
REFERENCE_EXPORT_SHA256 = '87c7e406c9b43dd8ea797baabb748d1eb350ef001b0658e1a16b8ee683f20445'

class Drawing(Sub32):
    icon_id = 'measurement-marker-draft-batch-024-15-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 5), (13, 5))
        self.add_line('p1-r1-2', (13, 5), (6, 5))
        self.add_bezier('p1-r1-3', (6, 5), ((4, 5), (2, 6), (2, 8)))
        self.add_bezier('p1-r1-4', (2, 8), ((2, 10), (4, 12), (6, 12)))
        self.add_line('p1-r1-5', (6, 12), (10, 12))
        self.add_line('p1-r1-6', (10, 12), (13, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (13, 20), (6, 20))
        self.add_bezier('p2-r1-2', (6, 20), ((4, 20), (2, 22), (2, 24)))
        self.add_bezier('p2-r1-3', (2, 24), ((2, 26), (4, 27), (6, 27)))
        self.add_line('p2-r1-4', (6, 27), (10, 27))
        self.add_line('p2-r1-5', (10, 27), (13, 20))
        self.add_line('p2-r1-6', (13, 20), (30, 20))
        self.add_line('p2-r1-7', (30, 20), (30, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (20, 13), (30, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
