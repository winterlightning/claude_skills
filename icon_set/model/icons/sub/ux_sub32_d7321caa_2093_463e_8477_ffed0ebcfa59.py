"""Independent 32px profile of ux.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd7321caa-2093-463e-8477-ffed0ebcfa59'
SOURCE_PATH = 'pictographic-primitives/symbol/ux_d7321caa-2093-463e-8477-ffed0ebcfa59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d7321caa-2093-463e-8477-ffed0ebcfa59', 'pictographic-primitives/symbol/ux_d7321caa-2093-463e-8477-ffed0ebcfa59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ux',)
SOLO_SOURCE_ICON_IDS = ('ux',)
REFERENCE_EXPORT_SHA256 = 'e4791256cac662bffeb3abef74df6e60ed63f48ad248a46cba9b2175b75be838'

class Drawing(Sub32):
    icon_id = 'ux-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 18), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (25, 2), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (30, 7))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (7, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 7))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (14, 2), (18, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 25), (2, 30))
        self.add_line('p5-r1-2', (2, 30), (7, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (30, 18), (30, 14))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (30, 25), (30, 30))
        self.add_line('p7-r1-2', (30, 30), (25, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (14, 30), (18, 30))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
