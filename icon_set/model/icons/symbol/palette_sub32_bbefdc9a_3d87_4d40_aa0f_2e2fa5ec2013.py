"""Independent 32px profile of palette.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013'
SOURCE_PATH = 'pictographic-primitives/design/palette_bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013', 'pictographic-primitives/design/palette_bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013.svg'),)
PROFILE_SOURCE_KEYS = ('solo/palette',)
SOLO_SOURCE_ICON_IDS = ('palette',)
REFERENCE_EXPORT_SHA256 = '6091d2add239c58375e77aedc57cfb29c270dda070e2407932b64dd8bba8b9a4'

class Drawing(Sub32):
    icon_id = 'palette-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((24, 2), (30, 7), (30, 14)))
        self.add_bezier('p1-r1-2', (30, 14), ((30, 19), (27, 21), (22, 21)))
        self.add_bezier('p1-r1-3', (22, 21), ((18, 21), (17, 30), (11, 30)))
        self.add_bezier('p1-r1-4', (11, 30), ((6, 30), (2, 25), (2, 18)))
        self.add_bezier('p1-r1-5', (2, 18), ((2, 9), (7, 2), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (9, 18), (9, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 10), (13, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 11), (21, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
