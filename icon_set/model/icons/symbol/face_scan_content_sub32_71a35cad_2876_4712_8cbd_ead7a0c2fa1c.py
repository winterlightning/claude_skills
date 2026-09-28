"""Independent 32px profile of face-scan-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '71a35cad-2876-4712-8cbd-ead7a0c2fa1c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/71a35cad-2876-4712-8cbd-ead7a0c2fa1c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('71a35cad-2876-4712-8cbd-ead7a0c2fa1c', 'icon_set/dist/gallery/combination-originals/71a35cad-2876-4712-8cbd-ead7a0c2fa1c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/face-scan-content',)
SOLO_SOURCE_ICON_IDS = ('face-scan-content',)
REFERENCE_EXPORT_SHA256 = '1f31041a349fd210186d421546cfafd69f04fe67355586277f1cf368182e3d3e'

class Drawing(Sub32):
    icon_id = 'face-scan-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (25, 2), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (30, 7))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (7, 30), (2, 30))
        self.add_line('p3-r1-2', (2, 30), (2, 25))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (25, 30), (30, 30))
        self.add_line('p4-r1-2', (30, 30), (30, 25))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (11, 14), (11, 14))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 14), (21, 14))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_arc('p7-r1-1', (11, 21), (21, 21), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
