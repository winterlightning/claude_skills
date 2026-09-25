"""Independent 32px profile of shinto-torii-gate.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '348b2ccc-38d8-4cd8-8990-df8ed5666e89'
SOURCE_PATH = 'pictographic-primitives/religion/shinto_348b2ccc-38d8-4cd8-8990-df8ed5666e89.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('348b2ccc-38d8-4cd8-8990-df8ed5666e89', 'pictographic-primitives/religion/shinto_348b2ccc-38d8-4cd8-8990-df8ed5666e89.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shinto-torii-gate',)
SOLO_SOURCE_ICON_IDS = ('shinto-torii-gate',)
REFERENCE_EXPORT_SHA256 = 'd4892fdd901dcb4f4fb5eb26d03e6d857a33548e29929d7cc21dfae4d0e0f96c'

class Drawing(Sub32):
    icon_id = 'shinto-torii-gate-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'religion'
    categories = ('religion', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 2), (30, 2), radius_x=44, radius_y=44, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 2), (28, 10))
        self.add_line('p2-r1-2', (28, 10), (23, 10))
        self.add_line('p2-r1-3', (23, 10), (9, 10))
        self.add_line('p2-r1-4', (9, 10), (4, 10))
        self.add_line('p2-r1-5', (4, 10), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (9, 10), (7, 18))
        self.add_line('p3-r1-2', (7, 18), (5, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (23, 10), (25, 18))
        self.add_line('p4-r1-2', (25, 18), (27, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 18), (7, 18))
        self.add_line('p5-r1-2', (7, 18), (25, 18))
        self.add_line('p5-r1-3', (25, 18), (30, 18))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-5')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-2')
        self.relate("connect", 'p3-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p5-r1-2')
        self.relate("connect", 'p4-r1-1', 'p5-r1-2')
        self.relate("connect", 'p4-r1-1', 'p5-r1-3')
        self.relate("connect", 'p4-r1-2', 'p5-r1-2')
        self.relate("connect", 'p4-r1-2', 'p5-r1-3')
