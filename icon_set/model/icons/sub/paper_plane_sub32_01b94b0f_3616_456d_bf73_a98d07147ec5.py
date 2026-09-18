"""Independent 32px profile of paper-plane.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '01b94b0f-3616-456d-bf73-a98d07147ec5'
SOURCE_PATH = 'pictographic-primitives/symbol/paper plane_01b94b0f-3616-456d-bf73-a98d07147ec5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('01b94b0f-3616-456d-bf73-a98d07147ec5', 'pictographic-primitives/symbol/paper plane_01b94b0f-3616-456d-bf73-a98d07147ec5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paper-plane',)
SOLO_SOURCE_ICON_IDS = ('paper-plane',)
REFERENCE_EXPORT_SHA256 = '173aaab2d36f786be99715d94ce571dad58f55691f819f722e4c0194659f7848'

class Drawing(Sub32):
    icon_id = 'paper-plane-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (30, 2))
        self.add_line('p1-r1-2', (30, 2), (24, 28))
        self.add_line('p1-r1-3', (24, 28), (16, 24))
        self.add_line('p1-r1-4', (16, 24), (11, 30))
        self.add_line('p1-r1-5', (11, 30), (10, 19))
        self.add_line('p1-r1-6', (10, 19), (2, 14))
        self.add_line('p1-r1-7', (2, 14), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (30, 2), (10, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
