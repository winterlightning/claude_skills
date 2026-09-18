"""Independent 32px profile of document.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22698c1f-48fd-44ce-b5f2-9ebee17ac2f8'
SOURCE_PATH = 'pictographic-primitives/content/document_22698c1f-48fd-44ce-b5f2-9ebee17ac2f8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22698c1f-48fd-44ce-b5f2-9ebee17ac2f8', 'pictographic-primitives/content/document_22698c1f-48fd-44ce-b5f2-9ebee17ac2f8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/document',)
SOLO_SOURCE_ICON_IDS = ('document',)
REFERENCE_EXPORT_SHA256 = '691d59ac9b29c0d50e3b52c9d0b9a380d5678681575e327798cd84427e393a31'

class Drawing(Sub32):
    icon_id = 'document-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 21), (15, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 12), (21, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 28), (5, 4))
        self.add_arc('p3-r1-2', (5, 4), (7, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (7, 2), (25, 2))
        self.add_arc('p3-r1-4', (25, 2), (27, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (27, 4), (27, 28))
        self.add_arc('p3-r1-6', (27, 28), (25, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (25, 30), (7, 30))
        self.add_arc('p3-r1-8', (7, 30), (5, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
