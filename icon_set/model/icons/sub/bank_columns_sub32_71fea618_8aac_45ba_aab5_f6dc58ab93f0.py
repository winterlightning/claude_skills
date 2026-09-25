"""Independent 32px profile of bank-columns.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '71fea618-8aac-45ba-aab5-f6dc58ab93f0'
SOURCE_PATH = 'pictographic-primitives/symbol/bank_71fea618-8aac-45ba-aab5-f6dc58ab93f0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('71fea618-8aac-45ba-aab5-f6dc58ab93f0', 'pictographic-primitives/symbol/bank_71fea618-8aac-45ba-aab5-f6dc58ab93f0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bank-columns',)
SOLO_SOURCE_ICON_IDS = ('bank-columns',)
REFERENCE_EXPORT_SHA256 = 'edb4dad1f773c9cee355f25a5413489eba8bab71eaa334a4fd715f0ea00df7b8'

class Drawing(Sub32):
    icon_id = 'bank-columns-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (30, 13))
        self.add_line('p1-r1-3', (30, 13), (2, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 30), (7, 30))
        self.add_line('p2-r1-2', (7, 30), (16, 30))
        self.add_line('p2-r1-3', (16, 30), (25, 30))
        self.add_line('p2-r1-4', (25, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (7, 19), (7, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 19), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (25, 19), (25, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p2-r1-4', 'p5-r1-1')
