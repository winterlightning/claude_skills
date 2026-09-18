"""Independent 32px profile of square-root-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9981fb9d-4558-4c15-acfa-90f0340e9617'
SOURCE_PATH = 'pictographic-primitives/interface-essential/square root_9981fb9d-4558-4c15-acfa-90f0340e9617.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9981fb9d-4558-4c15-acfa-90f0340e9617', 'pictographic-primitives/interface-essential/square root_9981fb9d-4558-4c15-acfa-90f0340e9617.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-root-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('square-root-interface-essential',)
REFERENCE_EXPORT_SHA256 = '68caf84f86ad723214c402a28fa3b8901031d2f3e9d2ebea90a520480791d451'

class Drawing(Sub32):
    icon_id = 'square-root-interface-essential-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 5), (13, 5))
        self.add_line('p1-r1-2', (13, 5), (6, 27))
        self.add_line('p1-r1-3', (6, 27), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (29, 14), (23, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (17, 14), (23, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (18, 26), (23, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (29, 26), (23, 20))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
