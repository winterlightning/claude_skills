"""Independent 32px profile of honeycomb-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f4966448-56e2-4786-a9bd-37a29a7e6a65'
SOURCE_PATH = 'pictographic-primitives/symbol/honeycomb_f4966448-56e2-4786-a9bd-37a29a7e6a65.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4966448-56e2-4786-a9bd-37a29a7e6a65', 'pictographic-primitives/symbol/honeycomb_f4966448-56e2-4786-a9bd-37a29a7e6a65.svg'),)
PROFILE_SOURCE_KEYS = ('solo/honeycomb-symbol',)
SOLO_SOURCE_ICON_IDS = ('honeycomb-symbol',)
REFERENCE_EXPORT_SHA256 = '6ecda7760ab1c0a6309b9e532b3d000063ab5c7be741a6aebdabb052ecadc8b4'

class Drawing(Sub32):
    icon_id = 'honeycomb-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 16), (13, 16))
        self.add_line('p1-r1-2', (13, 16), (10, 22))
        self.add_line('p1-r1-3', (10, 22), (5, 22))
        self.add_line('p1-r1-4', (5, 22), (2, 16))
        self.add_line('p1-r1-5', (2, 16), (5, 10))
        self.add_line('p1-r1-6', (5, 10), (10, 10))
        self.add_line('p1-r1-7', (10, 10), (13, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (19, 16), (22, 22))
        self.add_line('p2-r1-2', (22, 22), (19, 27))
        self.add_line('p2-r1-3', (19, 27), (13, 27))
        self.add_line('p2-r1-4', (13, 27), (10, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 22), (26, 22))
        self.add_line('p3-r1-2', (26, 22), (30, 16))
        self.add_line('p3-r1-3', (30, 16), (26, 10))
        self.add_line('p3-r1-4', (26, 10), (22, 10))
        self.add_line('p3-r1-5', (22, 10), (19, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (22, 10), (19, 5))
        self.add_line('p4-r1-2', (19, 5), (13, 5))
        self.add_line('p4-r1-3', (13, 5), (10, 10))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-5')
        self.relate("connect", 'p1-r1-2', 'p2-r1-4')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-6', 'p4-r1-3')
        self.relate("connect", 'p1-r1-7', 'p4-r1-3')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-5')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
