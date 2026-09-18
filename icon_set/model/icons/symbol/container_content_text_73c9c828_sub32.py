"""Independent 32px profile of container-content-text-73c9c828.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-73c9c828.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-73c9c828',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '83cf091d3fe61b23574b3796acea056e1bb922d0d3546f7a13988c2e05b46fe7'

class Drawing(TextSub32):
    icon_id = 'container-content-text-73c9c828-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 32
    text_ink_bounds = (0.0, 0.0, 32.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (30, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (11, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (7, 2), (7, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
