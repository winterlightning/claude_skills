"""Independent 32px profile of qr-code.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '15a95f5f-69dc-4853-b36a-97fec97a9e68'
SOURCE_PATH = 'pictographic-primitives/design/qr code_15a95f5f-69dc-4853-b36a-97fec97a9e68.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('15a95f5f-69dc-4853-b36a-97fec97a9e68', 'pictographic-primitives/design/qr code_15a95f5f-69dc-4853-b36a-97fec97a9e68.svg'),)
PROFILE_SOURCE_KEYS = ('solo/qr-code',)
SOLO_SOURCE_ICON_IDS = ('qr-code',)
REFERENCE_EXPORT_SHA256 = '00b2598b4f685362505804aa0d164d70d395d89fdfce1c9baf69d897b35afbf2'

class Drawing(Sub32):
    icon_id = 'qr-code-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    categories = ('design', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 4), (2, 4))
        self.add_line('p1-r1-2', (2, 4), (2, 24))
        self.add_line('p1-r1-3', (2, 24), (12, 24))
        self.add_line('p1-r1-4', (12, 24), (12, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, 4), (20, 4))
        self.add_line('p2-r1-2', (20, 4), (20, 28))
        self.add_line('p2-r1-3', (20, 28), (30, 28))
        self.add_line('p2-r1-4', (30, 28), (30, 4))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
